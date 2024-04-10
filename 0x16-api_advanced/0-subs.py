#!/usr/bin/python3
"""function that queries the Reddit API and returns number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API"""
    res = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            )

    if res.status_code == 200:
        return res.json().get("data").get("subscribers")
    else:
        return 0
