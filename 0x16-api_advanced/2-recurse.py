#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit"""
    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if r.status_code == 200:
        for mydata in r.json().get("data").get("children"):
            dat = mydata.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = r.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
