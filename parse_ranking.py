from pprint import pprint as pp
from read_json import read_json

LIST_NAMES = ("topselling_free", "topselling_paid", "movers_shakers",
    "topgrossing", "topselling_new_free", "topselling_new_paid", )

def get_ranking(package_json, country, list_name):
    data = read_json(package_json)
    for r in data["ranks"]:
        if r["country"] == country and r["list_name"] == list_name:
            return r["positions"]

def count_top_position(ranking):
    days_top = 0
    for day in ranking:
        if day["position"] and day["position"] == 1:
            days_top += 1
    return days_top

if __name__ == "__main__":
    for co in ("ES", "US", "AU", "NL"):
        print "\n" + co
        for p in ("com.facebook.katana", "com.nianticlabs.pokemongo", "com.snapchat.android" ):
            print "\n-" + p
            for ln in LIST_NAMES:
                inp = p + "_rank.json"
                ranking = get_ranking(package_json=inp, country=co, list_name=ln)
                if ranking:
                    print ln + " => " + str(count_top_position(ranking))
