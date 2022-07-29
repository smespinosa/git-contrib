
import datetime
import falcon
import json
from data_context import db_context as db


class ContribHandler:

    async def on_get(self, req: falcon.Request, resp: falcon.Response):
        contributor = req.get_param("email")

        year: int = int(req.get_param("year"))
        
        start_date = datetime.date(year, 1, 1)
        end_date   = datetime.date(year + 1, 1, 1)

        days_of_year_count = [ start_date + datetime.timedelta(n) for n in range(int ((end_date - start_date).days))]

        aggregate_days_count = {}
        for day in days_of_year_count:
            aggregate_days_count[day.strftime("%Y-%m-%d")] = 0
        
        contributions = db.get_contributions_by_contributor(contributor, year)

        for contribution in contributions:
            aggregate_days_count[contribution[0].strftime("%Y-%m-%d")] = contribution[1]

        result = []
        for aggregate_day in aggregate_days_count:
            result.append({
                "date": aggregate_day,
                "count": aggregate_days_count[aggregate_day]
            })

        resp.status = falcon.HTTP_200
        resp.text = json.dumps(result)

