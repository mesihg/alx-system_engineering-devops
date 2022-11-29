#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """returns a list containing the titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {'User-Agent': '0x16-api_advanced/mg1020'}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    result_data = response.json().get("data")
    after = result_data.get("after")
    count += result_data.get("dist")
    for item in result_data.get("children"):
        hot_list.append(item.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
