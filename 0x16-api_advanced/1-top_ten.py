#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for subreddit"""
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': '0x16-api_advanced/mg1020'}
    param = {'limit': 10}
    response = requests.get(url, headers=header, params=param)
    if response.status_code == 200:
        titles = response.json().get("data", {}).get("children", {})
        for title in titles:
            print(title.get('data').get('title'))
    else:
        print(None)
