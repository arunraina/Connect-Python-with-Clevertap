import pandas as pd
import numpy as np

import requests

headers = {
    'X-CleverTap-Account-Id': 'xxx-xxx-xxxx', #credientals ar ein your clevertap account
    'X-CleverTap-Passcode': 'xxx-xxx-xxxx',
    'Content-Type': 'application/json',
}

data = '{"event_name": "HS_Popular", "event_properties": [{"name": "Language Name","operator": "contains","value": "English"}],"from": 20191201,"to": 20191231}'
response = requests.post('https://api.clevertap.com/1/counts/events.json', headers=headers, data=data)


print(response.text.encode('utf8'))
