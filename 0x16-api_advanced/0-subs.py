#!/usr/bin/python3
""" Gets the number of subscribers from a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Main execution to get the request
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    resp = requests.get(url, allow_redirects=False,
                        headers={'User-Agent': 'MyChromeBook'})
    if resp:
        suscribers_number = response.json().get('data').get('subscribers')
        return (suscribers_number)
    else:
        return (0)
