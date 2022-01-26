from youtubesearchpython import VideosSearch, ChannelSearch
from configreader import Configuration
from pprint import pprint


class VariableNotFilled(Exception):
    """Raised when variable entry is not filled from config file"""
    pass


configFilePath = "space_db.ini"
sections = {
    0: "planet",
    1: "constellation",
    2: "planet_channels",
    3: "constellation_channels"
}

db = {}
for section in sections:
    db[sections[section]] = Configuration(configFilePath, sectionNames=sections[section]).__dict__


youTubeUrl = "https://www.youtube.com"

search = "saturn"
youtubeChannel = None
videoSearch = None
try:
    for item in db:
        if search.lower() in db[item]:
            youtubeChannel = db[f"{item}_channels"]
            if "planet" in item:
                search = search + "101"
    if youtubeChannel is None:
        raise VariableNotFilled("Raised when variable entry is not filled from config file.")
except VariableNotFilled as e:
    print(e)
    exit()

try:
    videoSearch = ChannelSearch(query=search, browseId=list(youtubeChannel.values())[0])
except KeyError:
    print("Could not find video from approved channels.")
    exit()

print(youTubeUrl + videoSearch.response[0]["uri"])
