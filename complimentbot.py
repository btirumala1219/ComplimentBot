import praw
import time

r = praw.Reddit(user_agent = "Bot made by Barath /u/username")
r.login()

def run_bot():
    subreddit = r.get_subreddit("test")
    comments = subreddit.get_comments(limit=25)