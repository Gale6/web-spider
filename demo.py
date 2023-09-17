import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

kw = {'q': 'br870'}
r = requests.get('https://www.google.com/search?',params=kw, headers = headers)
r.encoding = 'utf-8'
print (r)

