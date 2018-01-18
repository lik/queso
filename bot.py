import time
import pydle
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()
db = sqlite3.connect('queso.db')
cursor = db.cursor()
base = pydle.featurize(pydle.features.RFC1459Support, pydle.features.CTCPSupport, pydle.features.TLSSupport)

class MyOwnBot(base):
    def on_connect(self):
        self.logger.setLevel(20)
        f = open('pass', 'r')
        self.message('NickServ', 'IDENTIFY ' + f.readline())
        f.close()
        self.join('#homescreen')

    def on_channel_message(self, target, by, message):
        msg = message
        if msg.startswith(".rank"):
            most_pos = "Most positive users: "
            posusers = []
            for row in cursor.execute('''SELECT nick, compound FROM "poo" group by nick ORDER BY compound DESC LIMIT 3'''):
                posusers.append(row[0] + " (" + str(row[1]) + ")")
            self.message(target, most_pos + ", ".join(posusers))

            most_neg = "Most negative users: "
            negusers = []
            for row in cursor.execute('''SELECT nick, compound FROM "poo" group by nick ORDER BY compound ASC LIMIT 3'''):
                negusers.append(row[0] + " (" + str(row[1]) + ")")
            self.message(target, most_neg + ", ".join(negusers))

        nick = by
        if nick.endswith("bot"):
            return

        compound = analyser.polarity_scores(message).get('compound')
        if not compound:
            return

        unix = int(time.time())
        cursor.execute('''INSERT INTO poo(nick, compound, time) VALUES(:nick, :compound, :time)''', {'nick':nick, 'compound':compound, 'time':unix})
        db.commit()

client = MyOwnBot('queso', realname='queso')
client.connect('irc.rizon.net', 6697, tls=True, tls_verify=False)
client.handle_forever()
