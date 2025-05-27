
import requests

def fetch_public_records(url):
    response = requests.get(url)
    data = response.json()
    return data
