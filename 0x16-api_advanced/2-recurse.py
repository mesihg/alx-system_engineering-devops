#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all hot articles"""
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': '0x16-api_advanced/mg1020'}
    param = {'after': after}
    response = requests.get(url, headers=header, params=param)
    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", {})
        after = response.json().get("data", {}).get("after", {})
        if data is None or after is None:
            return None
        for item in data:
            hot_list.append(item.get('data').get('title'))
        return hot_list

    else:
        return recurse(subreddit, hot_list, after)
