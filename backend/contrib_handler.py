
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

        year_tuple = {}
        for day in days_of_year_count:
            year_tuple[day.strftime("%Y-%m-%d")] = 0
        
        contributions = db.get_contributions_by_contributor(contributor, year)

        for contribution in contributions:
            year_tuple[contribution[0].strftime("%Y-%m-%d")] = contribution[1]

        resp.status = falcon.HTTP_200
        resp.text = json.dumps(year_tuple, default=str)

