#!/usr/bin/python3
"""Function to query top ten hot post on subreddit"""


import requests


def top_ten(subreddit):
    """Return top ten hot post on subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    param = {"limit": 10}
    response = requests(url, header=header, param=param, allow_redirects=False)
    if response.status_code == 404:
        print(None)
        return
    results = response.json().get('data')
    [print(c.get("data").get("title")) for c in results.get("children")]
