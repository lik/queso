# queso
IRC bot that determines the positivity and negativity of users using sentiment analysis

## Dependencies
- pydle
- sqlite3
- vaderSentiment

## Usage
You'll need a database file to store three types of data, TEXT, REAL, and INTEGER. Substitute in IRC information.

Right now the bot won't return much useful information, but it does store the compounds<sup>1</sup> of each user's messages in the SQLite database.

<sup>1: The `compound` score is computed by summing the valence scores of each word in the lexicon, adjusted according to the rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive). This is the most useful metric if you want a single unidimensional measure of sentiment for a given sentence. Calling it a 'normalized, weighted composite score' is accurate. [Source](https://github.com/cjhutto/vaderSentiment#about-the-scoring)</sup>

### Commands
- `.rank`: returns the three most positive and negative users

## Todo
- Output a graph of some sort
- Have user-accessible commands

## Credits
This blog page helped me get started:

- [Using VADER to handle sentiment analysis with social media text](http://t-redactyl.io/blog/2017/04/using-vader-to-handle-sentiment-analysis-with-social-media-text.html)

As well as this friendly guy:
- [inexist3nce](https://github.com/inexist3nce)