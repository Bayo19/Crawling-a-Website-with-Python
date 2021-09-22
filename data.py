import json
import mysql.connector
from reading_csv_writing_json import kanji_from_csv
db = mysql.connector.connect(
    host="localhost",
    user="Bayostn",
    passwd="SteinSQL191?",
    database="kanji_db"
)

# mycursor = db.cursor()

# command = "INSERT INTO kanji_table (kanji, meanings, kun_readings, on_readings, n_level ) VALUES (%s, %s, %s, %s, %s)"

# for item in kanji_from_csv:
#     entry = (item["character"].encode(encoding='UTF-8',errors='strict'), json.dumps(item["meanings"]), json.dumps(item["k_readings"]), json.dumps(item["o_readings"]), item["n_level"],)
#     mycursor.execute(command, entry)
    
# db.commit()




    
