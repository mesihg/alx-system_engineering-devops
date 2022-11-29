#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for subreddit"""
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': '0x16-api_advanced/mg1020'}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        subscriber_no = response.json().get("data", {}).get("subscribers", 0)
        return subscriber_no
    else:
        return 0
