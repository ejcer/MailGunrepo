__author__ = 'emcenrue'

import urllib
import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v2/sandboxb92d03f6871d45f5912fbbec26d53347.mailgun.org/messages",
        auth=("api", "key-1c688c575c10981bd02726990837d3bd"),
        data={"from": "Excited User <mailgun@sandboxb92d03f6871d45f5912fbbec26d53347.mailgun.org>",
              "to": ["bar@example.com", "edward.mcenrue@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})