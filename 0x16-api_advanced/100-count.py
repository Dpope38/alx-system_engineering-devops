#!/usr/bin/python3
"""Function to count word in subreddit"""
import requests


def count_word(subreddit, words, instance={}, after="", count=0):
    """Return count of word in subreddit
        Args:
            subreddit: subreddit to search
            words: list of word to search
            instance: dictionary of word and count
            after: after page
            count: count of word
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {
            "after": after,
            "count": count,
            "limit": 10
            }
    response = requests(url, headers=headers, params=params)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return
    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for w in words:
            if w.lower() in title:
                time = len([t for t in title if t == w.lower()])
                if instance.get(w) is None:
                    instance[w] = time
                else:
                    instance[w] += time
    if after is not None:
        if len(instance) == 0:
            print("")
            return
        instances = sorted(instance.items(), key=lambda x: x[1], reverse=True)
    else:
        return count_word(subreddit, words, instance, after, count)
