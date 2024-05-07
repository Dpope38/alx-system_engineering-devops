#!/usr/bin/python3
"""Function to query list of all hot title subreddit"""

import requests

def recurse(subreddit, h_list=[], after="", count=0):
    """Return list of all hot title subreddit"""
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    params = {
            "after": after,
            "count": count,
            "limit": 10
            }
    response = requests(url, headers=headers, params=params)
    if response.status_code != 200:
            return None
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    
    for c in results.get("children"):
        h_list.append(c.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, h_list, after, count)
        return h_list

    
    
