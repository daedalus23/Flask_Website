from youtubesearchpython import VideosSearch
from pprint import pprint

videosSearch = VideosSearch('earth', limit = 1)

pprint(videosSearch.result())