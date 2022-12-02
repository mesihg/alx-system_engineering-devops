#!/usr/bin/python3
"""Parses all hot articles title and prints count of given keyword"""
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    '''Prints a sorted count of given keywords'''
    user_agent = {'User-agent': '0x16-api_advanced/mg1020'}
    articles = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                            .format(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if articles.status_code == 200:
        articles = articles.json()['data']
        aft = articles['after']
        articles = articles['children']
        for post in articles:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
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
