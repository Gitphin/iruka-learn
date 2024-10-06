import requests
from bs4 import BeautifulSoup

url = "https://www3.nhk.or.jp/news/easy/ne2024100212311/ne2024100212311.html"

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
txt_body = soup.find(id="js-article-body")

fname = 'nhk-body-text.txt'
if txt_body:
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(txt_body.get_text()) 
    print(f"Written to {fname}")
else:
    print(f"Could not write to {fname}")

