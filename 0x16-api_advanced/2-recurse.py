#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all hot articles"""
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': '0x16-api_advanced/mg1020'}
    param = {'after': after}
    response = requests.get(url, headers=header, params=param,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data")
    after = data.get("after")
    for item in data.get('children'):
        hot_list.append(item.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
