test_list = []

from csv import DictReader
with open('kanji.csv', 'r', encoding='utf-8-sig') as f:
    csv_reader = DictReader(f)
    for i in csv_reader:
        test_list.append()

print(test_list)

'''
in the scrape jisho file, you can join the lists together with commas to write to the kanji.csv file then when reading from it,
you can refer to each dict item that was a list and split it into a list again
'''
