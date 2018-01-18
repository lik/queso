import time
import pydle
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()
db = sqlite3.connect('queso.db')
cursor = db.cursor()

class MyOwnBot(pydle.Client):
    def on_connect(self):
        f = open('pass', 'r')
        self.message('NickServ', 'IDENTIFY ' + f.readline())
        f.close()
        self.join('#homescreen')

    def on_channel_message(self, target, by, message):
        nick = by
        if nick.endswith("bot"):
            return
        compound = analyser.polarity_scores(message).get('compound')
        if compound == 0:
            return
        unix = int(time.time())
        cursor.execute('''INSERT INTO poo(nick, compound, time) VALUES(:nick, :compound, :time)''', {'nick':nick, 'compound':compound, 'time':unix})
        db.commit()

client = MyOwnBot('queso', realname='queso')
client.connect('irc.rizon.net', 6697, tls=True, tls_verify=False)
client.handle_forever()
