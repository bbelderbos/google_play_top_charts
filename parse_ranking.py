from pprint import pprint as pp
from read_json import read_json

LIST_NAMES = ("topselling_free", "topselling_paid", "movers_shakers",
    "topgrossing", "topselling_new_free", "topselling_new_paid", )

def get_ranking(package_json, country, list_name):
    data = read_json(package_json) 
    for r in data["ranks"]:
        if r["country"] == country and r["list_name"] == list_name:
            return r["positions"]

if __name__ == "__main__":
    for co in ("ES", "US", "AU", "NL"):
        print "\n" + co
        for p in ("com.facebook.katana", "com.nianticlabs.pokemongo"):
            print "\n-" + p
            for ln in LIST_NAMES:
                inp = p + "_rank.json"
                ranking = get_ranking(package_json=inp, country="ES", list_name=ln)
                if ranking:
                    print "\n--" + ln
                    pp(ranking)
