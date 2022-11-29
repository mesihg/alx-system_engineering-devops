#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """parses the title of all hot articles of given keywords"""
    url = 'http://www.reddit.com/r/{}/hot.json?after={}'
    .format(subreddit, after)
    header = {'User-Agent': '0x16-api_advanced/mg1020'}
    response = requests.get(url, headers=header)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if response.status_code == 200:
        result_data = response.json()['data']
        after = result_data['after']
        articles = result_data['children']
        for article in articles:
            title = article['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if after is not None:
            count_words(subreddit, word_list, found_list, after)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
