from nltk.classify import NaiveBayesClassifier
import pydle

pos = []
with open("./pos_tweets.txt") as f:
    for i in f:
        pos.append([format_sentence(i), 'pos'])

neg = []
with open("./neg_tweets.txt") as f:
    for i in f:
        neg.append([format_sentence(i), 'neg'])

classifier = NaiveBayesClassifier.train(training)

# Simple echo bot.
class MyOwnBot(pydle.Client):
    def on_connect(self):
         self.message('NickServ', 'IDENTIFY queso123')
         self.join('#effay')

    def on_channel_message(self, target, by, message):
         self.message(target, message)

client = MyOwnBot('queso', realname='queso')
client.connect('irc.rizon.net', 6697, tls=True, tls_verify=False)
client.handle_forever()