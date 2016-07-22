from pprint import pprint as pp
from read_json import read_json

def topapps():
    return [app["package_name"] for app in read_json("topgooglecharts.json")["app_list"]]

if __name__ == "__main__": 
    pp(topapps())
