import requests
from bs4 import BeautifulSoup

jisho_base_url = 'https://jisho.org/search/%23kanji%20'

def scrape_jisho(base_url, n_level):
    kanji_list = []
    url = base_url+n_level
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
        else: break
        
        return kanji_list

N1 = scrape_jisho(jisho_base_url, 'n1')
N2 = scrape_jisho(jisho_base_url, 'n2')   
N3 = scrape_jisho(jisho_base_url, 'n3')
N4 = scrape_jisho(jisho_base_url, 'n4')
N5 = scrape_jisho(jisho_base_url, 'n5')

all_kanji_list = N5 + N4 + N3 + N2 + N1

print(all_kanji_list)


    
    