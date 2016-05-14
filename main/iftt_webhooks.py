import requests

__author__ = 'charlie'
maker_url= "https://maker.ifttt.com/trigger/{event}/with/key/{secret_key}"


def do_email(key, event, payload):
    url = maker_url.replace("{event}", event).replace("{secret_key}",key)
    result = requests.post(url, data=payload)
    print("Result of request to %s : %s" % (url, result))
    return result