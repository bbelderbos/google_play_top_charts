import json
from pprint import pprint as pp
import sys

def read_json(fname):
    json_data=open(fname).read()
    return json.loads(json_data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("provide file")
    fname = sys.argv[1]
    data = read_json(fname)
    pp(data)
