###Malon 100chart
#

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.melon.com/chart/index.htm'
header_dict = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
res = requests.get(url, headers=header_dict)

if res.ok:
    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    a = soup.select("div#tb_list tr a[href*='playSong']")
    for idx, a in enumerate(a, 1):
        title = a.text
        href_value = a['href']
        print(idx, title)
        print(href_value)
        matched = re.search(r'(\d+)\);', href_value)
        if matched:
            song_id = matched.group(1)
            song_detail_url = f'https://www.melon.com/song/detail.htm?songId={song_id}'
            print(song_id, title, song_detail_url)
