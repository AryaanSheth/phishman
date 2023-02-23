import json


class FetchData:

    def __init__(self, request: str):
        self.REQUEST = request
        self.DATA = "database/output.json"

    def fetch_data(self):
        with open(self.DATA, "r") as f:
            data = json.load(f)
            for i in data:
                if i["url"] == self.REQUEST:
                    return i
            return None
