
from datetime import date, timedelta
import falcon
import json
from data_context import db_context as db


class ContribHandler:

    async def on_get(self, req: falcon.Request, resp: falcon.Response):
        contributor = req.get_param("email")

        year: int = int(req.get_param("year"))
        
        start_date = date(year, 1, 1)
        end_date   = date(year + 1, 1, 1)

        days_of_year_count = [ start_date + timedelta(n) for n in range(int ((end_date - start_date).days))]

        aggregate_days_count = {}
        for day in days_of_year_count:
            aggregate_days_count[day.strftime("%Y-%m-%d")] = 0
        
        contributions = db.get_contributions_by_contributor(contributor, year)        

        for contribution in contributions:
            aggregate_days_count[contribution[0].strftime("%Y-%m-%d")] = contribution[1]

        heatmap_result = [[None for x in range(7)] for y in range(53)]

        for day in aggregate_days_count:
            iso_date = date.fromisoformat(day)
            week_of_year, day_of_week = self.get_week_and_day(iso_date)
            heatmap_result[week_of_year][day_of_week] = aggregate_days_count[day]

        response = {
            "weeks": heatmap_result,
            "contributions": []
        }

        for aggregate_day in aggregate_days_count:
            response["contributions"].append({
                "date": aggregate_day,
                "count": aggregate_days_count[aggregate_day]
            })


        resp.status = falcon.HTTP_200
        resp.text = json.dumps(response)

    def get_week_and_day(self, isodate: date):
        day_of_week = int(isodate.strftime("%w"))
        week_of_year = int(isodate.strftime("%U"))
        return week_of_year, day_of_week