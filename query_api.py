import json
import requests
from topcharts import topapps

RANKS_EP = "https://data.42matters.com/api/v2.0/android/apps/ranks.json?"
 
def get_key():
    with open("notebook.conf") as f:
        return [line.split("=")[1].strip() for line in f.readlines() if "apikey" in line][0]

def get_ranks(package, days=10, cache=True):
    params = {
        "p": package,
        "days": days,
        "access_token": get_key(),
    }
    r = requests.get(RANKS_EP, params=params)
    if cache:
        fname = package + "_rank.json"
        with open(fname, 'w') as outfile:
            json.dump(r.json(), outfile) 
    else:
        return r.json()

if __name__ == "__main__":
    for package in topapps():
        get_ranks(package=package, days=18, cache=True)
