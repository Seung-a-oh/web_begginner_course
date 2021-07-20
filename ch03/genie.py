import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('.list-wrap > tbody > tr')

for tr in trs:
    number = tr.select_one('.number').text[0:2].strip()
    title = tr.select_one('.info > a.title.ellipsis').text.strip()
    artist = tr.select_one('.info > a.artist.ellipsis').text.strip()
    print(number,".", title, artist)

