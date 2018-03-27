import praw
import time
import requests

requests.get("https://spreadsheets.google.com/feeds/list/1eEa2ra2yHBXVZ_ctH4J15tFSGEu-VTSunsrvaCAV598/od6/public/values?alt=json").json()['feed']['entry'][0]['title']['$t']
strs = ["" for x in range(50)]
for x in range(0,25):
    strs[x] = requests.get("https://spreadsheets.google.com/feeds/list/1eEa2ra2yHBXVZ_ctH4J15tFSGEu-VTSunsrvaCAV598/od6/public/values?alt=json").json()['feed']['entry'][x]['title']['$t']
    #print(strs[x])

r = praw.Reddit(user_agent = "ComplimentBot by Barath",
                client_id="ID",
                username="ComplimentForAll",
                password="Test1234",
                client_secret="CLIENT_SECRET")


def run_bot():
    subreddit = r.subreddit("test")
    comments = subreddit.comments(limit=25)
    for comment in comments:
        print(comment)

run_bot()