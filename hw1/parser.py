import requests
from bs4 import BeautifulSoup as BS

s = requests.Session()

auth_html = s.get('https://github.com/Skylore?tab=repositories')
auth_bs = BS(auth_html.content, 'html.parser')

for i in auth_bs.select('a[itemprop="name codeRepository"]'):
    print(i.attrs['href'].split('/')[2])
