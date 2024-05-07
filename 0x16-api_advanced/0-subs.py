#!/usr/bin/python3
"""Function to query subscriber on subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers on subreddit"""
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(url, header=header, allow_redirects=False)
    data = response.json()

    if 'data' in data and 'subscribers' in data['data']:
        return data['data']['subscribers']
    else:
        return 0
