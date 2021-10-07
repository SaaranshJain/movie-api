import requests
from helpers import make_url_by_search
from pprint import pprint

url = make_url_by_search(s="pog", type="movie")
print(url)
pprint(requests.get(url).content)
