from requests import post
from json import dump
import threading
import time


class UpdateData:

    def __init__(self):
        self.FETCH_URL = "http://data.phishtank.com/data/online-valid.json"
        self.OUTPUT = "database/output.json"

    # SAMPLE OUTPUT
    # {"phish_id": "8038529",
    #  "url": "https://my-orico-co-jp.ghnb3.com/?ok2l.jl8jwf2",
    #  "phish_detail_url": "http://www.phishtank.com/phish_detail.php?phish_id=8038529",
    #  "submission_time": "2023-02-16T00:47:40+00:00",
    #  "verified": "yes",
    #  "verification_time": "2023-02-16T00:52:33+00:00",
    #  "online": "yes",
    #  "details": [{"ip_address": "104.21.5.145", "cidr_block": "104.21.0.0/19", "announcing_network": "13335", "rir": "arin", "country": "US", "detail_time": "2023-02-16T00:52:46+00:00"}],
    #  "target": "Other"}

    def post_request(self):
        return post(self.FETCH_URL).json()

    def write_to_database(self):
        with open(self.OUTPUT, "w") as f:
            dump(self.post_request(), f, indent=4)
