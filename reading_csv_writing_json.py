import json
from csv import DictReader
# from openpyxl import Workbook, load_workbook

kanji_from_csv = []
def read_from_csv_file():
    with open('kanji.csv', 'r', encoding='utf-8-sig') as f:
        csv_reader = DictReader(f)
        for i in csv_reader:
            kanji_from_csv.append({
                    "character" : i["kanji"],
                    "meanings": i["meanings"].split(','),
                    "k_readings": i["kun"].split(','),
                    "o_readings": i["on"].split(','),
                    "n_level": i["level"].upper()
                })
    
def write_to_json_file():
    with open('kanji_level.json', 'w', encoding='utf-8-sig', newline='') as f:
        json.dump(kanji_from_csv, f, indent= 4, ensure_ascii=False)
    
# def write_to_excel():
#     wb = Workbook()
#     ws = wb.active
#     ws.title = "Kanji Data"
    
#     for i in range(1,6):
#         wb.create_sheet(f'N{i}')
    
#     for i in wb.sheetnames:
#         ws = wb[i]
#         ws.append(list(kanji_from_csv[0].keys()))
#     # for row in kanji_from_csv:
#     #     level = row['n_level']
#     #     ws = wb[level]
        
    
#     wb.save('JLPT_kanji_dataset.xlsx')
    
    
      
read_from_csv_file()
# write_to_excel()
# write_to_json_file()

