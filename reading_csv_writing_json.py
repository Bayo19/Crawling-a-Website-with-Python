import json
from csv import DictReader

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
                    "n_level": i["level"]
                })
            
def write_to_json_file():
    with open('kanji_level.json', 'w', encoding='utf-8-sig', newline='') as f:
        json.dump(kanji_from_csv, f, indent= 4, ensure_ascii=False)
    
    
read_from_csv_file()
write_to_json_file()
print('written to json file')


