#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Gets the top ten hot posts of a subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    resp = requests.get(url, allow_redirects=False,
                        headers={'User-Agent': 'Pear'})
    if resp:
        post_list = resp.json().get('data').get('children')
        for a, children in enumerate(post_list):
            if (a == 10):
                break
            print(children.get('data').get('title'))
    else:
        print(None)
