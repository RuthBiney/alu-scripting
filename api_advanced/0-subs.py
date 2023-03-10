#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of subscribers"""
import request

def number_of_subscribers(subreddit):

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        subscriber_number = json_data.get('data').get(
            'children')[0].get('data').get('subreddit_subscribers')
        return subscriber_num
    else:
        return 0
