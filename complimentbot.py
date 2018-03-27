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
                    client_id="RLzYlFQNy9qKdw",
                    username=creds[0],
                    password=creds[1],
                    client_secret="jSEhZZ0-HNf0ig9N6pi7pogk7GQ")
    return r

def run_bot(r):
    for comment in r.subreddit(creds[2]).comments(limit=25):
        if "!compliment" in comment.body:
            if comment.id not in used:
                i = random.randint(0,25)
                comment.reply(strs[i])
                used.append(comment.id)

r = login_bot()
run_bot(r)
