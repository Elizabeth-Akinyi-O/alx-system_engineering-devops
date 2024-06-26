#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
"""
import requests


def count_words(subreddit, word_list, after=None, my_dict={}):
    """
    Parses the title of all hot articles, and prints a sorted count
    of given keywords (case-insensitive, delimited by spaces)
    - Javascript should count as javascript, but java should not
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    payload = {'after': after}
    response = requests.get(url,
                            allow_redirects=False,
                            params=payload,
                            headers={'User-Agent': 'Pear'})
    if response and response.status_code == 200:
        post_list = response.json().get('data').get('children')
        for children in post_list:
            title1 = children.get('data').get('title')
            for word in word_list:
                try:
                    my_dict[word] += title1.lower().split().count(word.lower())
                except KeyError:
                    my_dict[word] = title1.lower().split().count(word.lower())
        after = response.json().get('data').get('after')
        if (after is None):
            for key, val in sorted(my_dict.items(),
                                   key=lambda x: (-1*x[1], -1*x[0])):
                if (val != 0):
                    print("{}: {}".format(key.lower(), val))
            return
        return count_words(subreddit, word_list, after, my_dict)
    else:
        return
