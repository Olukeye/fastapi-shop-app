from typing import Dict
import requests

def send_to_flutterwave(endpoint: str=None, data: Dict={}):
    url = "https://api.flutterwave.com/v3/" + str(endpoint)
    
    data: {
        'country': 'NG',
        'customer': '+2348037705238',
        'amount': '100',
        'recurrence': 'ONCE',
        'type': 'AIRTIME',
        'reference': '9300049404444',
        'biller_name': 'DSTV, MTN VTU, TIGO VTU, VODAFONE VTU, VODAFONE POSTPAID PAYMENT'
    }

    response  = requests.post(url, json = data)
    
    return response.json()



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
    