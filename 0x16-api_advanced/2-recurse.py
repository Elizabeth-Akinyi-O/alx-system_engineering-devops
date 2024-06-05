#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles
    for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    payload = {'after': after}
    response = requests.get(url, allow_redirects=False,
                            params=payload,
                            headers={'User-Agent': 'Pear'})
    if resp and resp.status_code == 200:
        after = resp.json().get('data').get('after')
        if (after is None):
            return hot_list
        post_list = resp.json().get('data').get('children')
        for children in post_list:
            hot_list.append(children.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    else:
        return None
