#!/usr/bin/python3
"""Function to query top ten hot post on subreddit"""

import requests

def top_ten(subreddit):
    """Return top ten hot post on subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    params = {
            "limit": 10
            }
    response = requests(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        print(None)
        return
    results = response.json().get('data')
    [print(c.get("data").get("title")) for c  in results.get("children")]
