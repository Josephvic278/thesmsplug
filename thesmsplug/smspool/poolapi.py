import requests
from dotenv import load_dotenv
import os
load_dotenv()
payload = {}
files = {}
smspool_apikey = os.getenv('APIPOOL_APIKEY')
headers = {
    'Authorization': f'Bearer {smspool_apikey}',
    'Content-Type': 'application/json'
}

def check_request(response):
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code, response.json())

def get_balance():
    end_point = "https://api.smspool.net/request/balance"

    response = requests.post(url=end_point, headers=headers, data=payload, files=files)
    return check_request(response)['balance']

def service_list():
    end_point = "https://api.smspool.net/service/retrieve_all"

    response = requests.post(url=end_point, headers=headers, data=payload, files=files)
    serviceList = []
    for get_id in check_request(response):
        serviceList.append(get_id['ID'])
    #print(check_request(response))
    return serviceList
    
def country_success_rate():
    servie_id = service_list()[0]
    end_point = f'https://api.smspool.net/request/success_rate'
    params = {
        'service': servie_id
    }
    response = requests.post(url=end_point, params=params, headers=headers, data=payload, files=files)
    print(response.json())

country_success_rate()