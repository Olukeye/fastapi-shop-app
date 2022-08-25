from typing import Dict
import requests
import pprint


def send_to_flutterwave(endpoint: str=None, data: Dict={}):
    url = "https://api.flutterwave.com/v3/bill-categories" + str(endpoint)

    headers = {
        'Authorization': 'FLWSECK_TEST-2510cd57eebd62d8a20e1c344a0943f5-X'
    }

    parameters: {
    "id": 1,
    }

    response  = requests.get(url, headers=headers)

    return response.json()

print(send_to_flutterwave())
# def call_fluf():
#     data: {
#         'country': 'NG',
#         'customer': '+2348037705238',
#         'amount': '100',
#         'recurrence': 'ONCE',
#         'type': 'AIRTIME',
#         'reference': '9300049404444',
#         'biller_name': 'DSTV, MTN VTU, TIGO VTU, VODAFONE VTU, VODAFONE POSTPAID PAYMENT'
#     }
#     return send_to_flutterwave(endpoint="", data=data)
    