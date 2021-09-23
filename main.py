import requests
from helpers import make_url_by_search

print(requests.get(make_url_by_search(s="pog", type="movie")).content)
