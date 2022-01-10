import requests

url = 'https://by.wildberries.ru/catalog/1111111/detail.aspx?targetUrl=MI'
response = requests.get(url)

print(response.headers)