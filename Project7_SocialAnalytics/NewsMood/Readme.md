
# Name:  Ashwini Devkota
# News Mood

## Analysis

    This program utilizes a Python Script to perform a sentiment analysis of the Twitter 
    activity of various news organizations: BBC, CBS, CNN, Fox and New York Times.  Then 
    it presents those findings visually using a scatterplot and a bar graph.  
    
    Here are the three observable trends based on data:
    
    (1) All five news organizations have overall negative polarity scores.
    
    (2) BBC had the highest negative polarity scores followed by CBS.  On the other hand, 
        New York Times had the overall least negative polarity scores.
    
    (3) The polarity scores of total tweets analyzed for all news organizations were  
        distributed fairly equally among positive, neutral and negative polarity scores  
        (slightly skewed towards negative)


```python
# Dependencies
import tweepy
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import time
import seaborn as sns
```


```python
# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
```


```python
# Twitter API Keys
from config import consumer_key, consumer_secret, \
    access_token, access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
# Target news sources
target_users = ("BBCWorld", "CBSNews", "CNN", "FOXNews", "nytimes")

# Variables for holding sentiments
sentiments = []
```


```python
# Loop through all news sources
for user in target_users:
    
    # Counter variable
    counter = 1
    
    # Get all tweets from home feed (total = 100 tweets)
    public_tweets = api.user_timeline(user, count = 100)
    
    # Loop through all tweets
    for tweet in public_tweets:
        
        # Run Vader Analysis on each tweets
        compound = analyzer.polarity_scores(tweet["text"])["compound"]
        pos = analyzer.polarity_scores(tweet["text"])["pos"]
        neu = analyzer.polarity_scores(tweet["text"])["neu"]
        neg = analyzer.polarity_scores(tweet["text"])["neg"]
        tweets_ago = counter
        
        # Add sentiments for each tweets into an array
        sentiments.append({"Compound": compound,
                           "Positive": pos,
                           "Neutral": neu,
                           "Negative": neg,
                           "Tweets Ago": counter,
                           "User": user,
                           "Date": tweet["created_at"],
                           "Tweet Text": tweet["text"]})
    
        # Add to counter
        counter = counter + 1
        
# sentiments     
```


```python
# Convert sentiments to DataFrame
sentiments_df = pd.DataFrame.from_dict(sentiments)

sentiments_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Date</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweet Text</th>
      <th>Tweets Ago</th>
      <th>User</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0000</td>
      <td>Wed Mar 07 09:01:50 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.00</td>
      <td>Coca-Cola plans Japan foray into alcohol https...</td>
      <td>1</td>
      <td>BBCWorld</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0000</td>
      <td>Wed Mar 07 08:26:06 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.00</td>
      <td>RT @SallyBundockBBC: #Mattel is marking #Inter...</td>
      <td>2</td>
      <td>BBCWorld</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.4019</td>
      <td>Wed Mar 07 08:17:45 +0000 2018</td>
      <td>0.252</td>
      <td>0.748</td>
      <td>0.00</td>
      <td>Terminal illness led to Australia's first same...</td>
      <td>3</td>
      <td>BBCWorld</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.3818</td>
      <td>Wed Mar 07 08:17:43 +0000 2018</td>
      <td>0.245</td>
      <td>0.755</td>
      <td>0.00</td>
      <td>Blackberry sues Facebook in fight over app pat...</td>
      <td>4</td>
      <td>BBCWorld</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.1531</td>
      <td>Wed Mar 07 08:12:47 +0000 2018</td>
      <td>0.268</td>
      <td>0.352</td>
      <td>0.38</td>
      <td>Fyre Festival co-founder Billy McFarland admit...</td>
      <td>5</td>
      <td>BBCWorld</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Export dataframe to a csv
sentiments_df.to_csv("csv_data.csv")
```


```python
date = time.strftime("%m/%d/%Y")

colors = ["lightblue", "green", "red", "blue", "orange"]

# counter
i = 0

# Loop through all target users and plot scatterplot
for user in target_users:
    new_df = sentiments_df.loc[sentiments_df["User"] == user]   
    plt.scatter(new_df["Tweets Ago"], new_df["Compound"], label = user, 
                s = 100, color = colors[i], edgecolors = "black", alpha = 0.8)
    i = i + 1

# x-limit, y-limit, Grid and Legends for scatterplot
plt.xlim(105, -5)
plt.ylim(-1.05, 1.05)
plt.grid()
plt.legend(bbox_to_anchor = (1,1), title = "Media Sources", edgecolor = "black")

# Chart Title, x-label and y-label
plt.title("Sentiment analysis of Media Tweets (%s)" % date)
plt.xlabel("Tweets Ago")
plt.ylabel("Tweet Polarity")

# Export and save Bar plot
plt.savefig("Scatterplot_SentimentAnalysis.png", bbox_inches = "tight")

# Print chart to the screen
plt.show()
```


![png](output_9_0.png)



```python
ave_sentiment_by_source = sentiments_df.groupby("User")["Compound"].mean()
ave_sentiment_by_source
```




    User
    BBCWorld   -0.103437
    CBSNews    -0.094567
    CNN        -0.031231
    FOXNews    -0.039542
    nytimes    -0.009563
    Name: Compound, dtype: float64




```python
# Define x-axis and xlabels
x_axis = np.arange(len(ave_sentiment_by_source))
x_labels = ave_sentiment_by_source.index

# Plot bar graph and assign appropriate parameters
plt.bar(x_axis, ave_sentiment_by_source, width = 1, tick_label = x_labels,
        color = colors, alpha = 0.75, align = "edge", edgecolor = "black")
tick_locations = [i+0.5 for i in x_axis]
plt.xticks(tick_locations, ["BBC", "CBS", "CNN", "FOX", "NYT"])

# Chart Title, x-label and y-label
plt.title("Overall Media Sentiment based on Twitter (%s)" % date)
plt.xlabel("Media Sources")
plt.ylabel("Tweet Polarity")

# Export and save Bar plot
plt.savefig("Barplot_OverallSentiment.png")

# Print chart to the screen
plt.show()
```


![png](output_11_0.png)

