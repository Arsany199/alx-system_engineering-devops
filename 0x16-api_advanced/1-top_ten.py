#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit"""
    res = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if res.status_code == 200:
        for mydata in res.json().get("data").get("children"):
            dat = mydata.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
