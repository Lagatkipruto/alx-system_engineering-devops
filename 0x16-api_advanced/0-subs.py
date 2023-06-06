#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Set a custom User-Agent header to avoid errors"""
    headers = {'User-Agent': 'MyBot/1.0'}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0