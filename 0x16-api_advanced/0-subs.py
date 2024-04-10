#!/usr/bin/python3
"""
This module contains a function to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        print(f"Error: Unable to fetch data for subreddit '{subreddit}'. Status code: {response.status_code}")
        return 0

# Test the function
if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")  # Let user input the subreddit name
    subscribers = number_of_subscribers(subreddit)
    print(f"The number of subscribers for r/{subreddit} is: {subscribers}")
