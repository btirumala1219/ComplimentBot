import praw
import time
import requests
import random

strs = ["" for x in range(50)]
for x in range(0,25):
    strs[x] = requests.get("https://spreadsheets.google.com/feeds/list/1eEa2ra2yHBXVZ_ctH4J15tFSGEu-VTSunsrvaCAV598/od6/public/values?alt=json").json()['feed']['entry'][x]['title']['$t']
    #print(strs[x])

f = open("credentials.txt","r")
creds = f.read().splitlines()

used = []

def login_bot():
    print(creds)
    r = praw.Reddit(user_agent="ComplimentBot by Barath",
                    client_id=creds[0],
                    username=creds[1],
                    password=creds[2],
                    client_secret=creds[3])
    return r

def run_bot(r):
    for comment in r.subreddit('test').comments(limit=25):
        if "!compliment" in comment.body:
            if comment.id not in used:
                i = random.randint(0,25)
                comment.reply(strs[i])
                used.append(comment.id)

r = login_bot()
run_bot(r)
