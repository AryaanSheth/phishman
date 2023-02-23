import json


class message_search:
    def __init__(self, message):
        self.message = message
        self.flag = False
        self.links = []

    def search(self) -> bool:
        for obj in json.load(open("database/output.json")):
            if obj["url"] in self.message:
                self.flag = True
                self.links.append(obj["url"])
        return self.flag, self.links
