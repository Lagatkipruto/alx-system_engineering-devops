#!/usr/bin/python3
"""A function that queries the Reddit API,
Parses the title of all title of all hot articles
and prints a sorted  count of given keywords.
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit.

    Arguments:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    if instances is None:
        instances = {}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                instances[word] = instances.get(word, 0) + times        else:
        

    if after is None:
        if len(instances) == 0:
            print("No matches found")
            return
        
        sorted_instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0].lower))
        for word, count in sorted_instances:
            print(f"{word.lower()}: {count}")
    else:
        count_words(subreddit, word_list, instances, after, count)