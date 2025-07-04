import requests

url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1783/dados?formato=json'
response = requests.get(url)
print(response.json())