import requests
import re
import random


def list2dict(x):
    """
    Utility to convert list to dictionary
    """
    return {
        "ip": x[0],
        "port": x[1],
        "country": {
            "code": x[2],
            "name": x[3]
        },
        "anonymity": x[4],
        "google": True if x[5] == "yes" else False,
        "https": True if x[6] == "yes" else False,
        "last_update": x[7],
        "url":
        "%s://%s:%s" % ("https" if x[6] == "yes" else "http", x[0], x[1])
    }


def make_request() -> list:
    """
	Function to extract proxy data. 
    
    `returns` 
    list
	"""
    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Encoding': 'gzip',
        'Content-Type': 'text/html; charset=utf-8',
    }

    response = requests.get(  # getting the response
        'https://free-proxy-list.net/',
        headers=headers).text

    # scraping all the tuples
    return list(  # converting to list
        map(  # mapping each element 
            lambda x: tuple(re.findall(r"<td[^>]*>(.+?)</td>", x)
                            ),  # to this lambda
            re.findall(  # from this list
                r"<tr><td>[^<]*</td><td>[^<]*</td><td>[^<]*</td><td class='hm'>[^<]*</td><td>[^<]*</td><td class='hm'>[^<]*</td><td class='hx'>[^<]*</td><td class='hm'>[^<]*</td></tr>",
                response)))


def fetch(count=300, **kwargs) -> list:
    """
    Function to fetch and filter proxies
    
    `params:`
    
        + count     -- number of proxies to retrieve (default: 300)
        + country   -- country code to filter
        + anonymity -- proxy anonymity (choose from: transparent, anonymous, elite proxy)
        + google    -- set true for google proxies, otherwise false
        + https     -- set true for https proxies, otherwise false

    `returns`
    
        list -- list of filtered proxies




    ```py

    # for example
    print(fetch(count=10, google=True, https=False, country="BR", anonymity="anonymous"))
    ```
    """

    # building data
    data = list(map(list2dict, make_request()))

    # filtering by country code
    try:
        cc = kwargs["country"]
        data = filter(lambda x: x["country"]["code"] == cc, data)
    except KeyError:
        pass

    # filtering by anonymity
    try:
        anonymity = kwargs["anonymity"]
        data = filter(lambda x: x["anonymity"] == anonymity, data)
    except KeyError:
        pass

    try:
        google = kwargs["google"]
        data = filter(lambda x: x["google"] == google, data)
        pass
    except KeyError:
        pass

    try:
        https = kwargs["https"]
        data = filter(lambda x: x["https"] == https, data)
        pass
    except KeyError:
        pass

    if count > 300:
        raise ValueError("Count can not exceed 300")

    # returning sliced list
    return list(data)[:count]


fetch