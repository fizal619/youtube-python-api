import os
from apiclient.discovery import build


DEV_KEY = open("api-key.txt", "r").read()
API_NAME = "youtube"
API_VERSION= "v3"


def youtubeSearch(query):
    youtube = build(API_NAME,
                    API_VERSION,
                    developerKey=DEV_KEY)
    search_response = youtube.search().list(
        maxResults=1,
        part="id,snippet",
        q=query
    ).execute()

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video = {'Title:' : search_result["snippet"]["title"], 'Link:' : "http://youtu.be/"+search_result["id"]["videoId"]}
        else:
            return "Video not found."

    return video