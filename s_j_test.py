# import requests
# from bs4 import BeautifulSoup

# kanji_list = []
# url = 'https://jisho.org/search/%23kanji%20n1'
# while True:
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, 'html.parser')
    
#     for element in soup.find_all('div', {'class': 'entry kanji_light clearfix'}):
#         character = element.find('span', {'class': 'character literal japanese_gothic'}).text
#         meanings = element.find('div', {'class': 'meanings english sense'}).find_all('span')
        
#         if element.find('div', {'class': 'kun readings'}):
#             kun_readings = element.find('div', {'class': 'kun readings'}).find_all(class_='japanese_gothic')
#         if element.find('div', {'class': 'on readings'}):
#             on_readings = element.find('div', {'class': 'on readings'}).find_all(class_='japanese_gothic')

#         kanji_list.append({
#             "character" : character,
#             "meanings": [i.get_text().replace(', ', '') for i in meanings],
#             "k_readings": [i.get_text().replace('、 ', '') for i in kun_readings],
#             "o_readings": [i.get_text().replace('、 ', '') for i in on_readings],
#             "kanji_level": 'N'
#         })
    
#     url_tag = soup.find('a', {'class': 'more'})
#     if url_tag != None:
#         url = 'https:' + url_tag.get('href')
#     else: break
        
# print(kanji_list)
# print(len(kanji_list))