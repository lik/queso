import time
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()
db = sqlite3.connect('queso.db')
cursor = db.cursor()

for row in cursor.execute('''SELECT nick, compound FROM "poo" group by nick ORDER BY compound ASC LIMIT 3'''):
    print(row[0])