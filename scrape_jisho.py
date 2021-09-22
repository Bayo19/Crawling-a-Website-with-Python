import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

jisho_base_url = 'https://jisho.org/search/%23kanji%20'
kanji_list = []

def scrape_jisho(base_url, n_level):
    
    url = f'{base_url}{n_level}'
    while True:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        
        for element in soup.find_all('div', {'class': 'entry kanji_light clearfix'}):
            character = element.find('span', {'class': 'character literal japanese_gothic'}).text
            meanings = element.find('div', {'class': 'meanings english sense'}).find_all('span')
            
            if element.find('div', {'class': 'kun readings'}):
                kun_readings = element.find('div', {'class': 'kun readings'}).find_all(class_='japanese_gothic')
            if element.find('div', {'class': 'on readings'}):
                on_readings = element.find('div', {'class': 'on readings'}).find_all(class_='japanese_gothic')

            kanji_list.append({
                "character" : character,
                "meanings": [i.get_text().replace(', ', '') for i in meanings],
                "k_readings": [i.get_text().replace('、 ', '') for i in kun_readings],
                "o_readings": [i.get_text().replace('、 ', '') for i in on_readings],
                "kanji_level": n_level
            })
        
        url_tag = soup.find('a', {'class': 'more'})
        if url_tag != None:
            url = 'https:' + url_tag.get('href')
            sleep(2)
        else: break
        

def crawler(num):
    for level in range(1, num):
        scrape_jisho(jisho_base_url, f'n{level}')
        sleep(3)

crawler(6)

#writing scraped info to the csv file       
with open('kanji.csv', 'w', encoding='utf-8-sig', newline='') as f:
    headers = ['kanji', 'meanings', 'kun', 'on', 'level']
    csv_writer = DictWriter(f, fieldnames=headers)
    csv_writer.writeheader()
    for kanj_char in kanji_list:
        csv_writer.writerow({
            "kanji": kanj_char["character"],
            "meanings": ",".join(kanj_char["meanings"]),
            "kun": ",".join(kanj_char["k_readings"]),
            "on": ",".join(kanj_char["o_readings"]),
            "level": kanj_char["kanji_level"]
        })
        
print('data written to csv file, bro')
