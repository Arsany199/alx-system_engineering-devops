#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API"""
    r = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0
