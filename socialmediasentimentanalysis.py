import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
posts = [
    "The new laptop I bought is super fast and lightweight, totally worth it!",
    "Terrible customer support… waited 2 hours and no response.",
    "The weather today is fine, nothing special.",
    "Wow! The movie exceeded my expectations, absolutely loved it!",
    "I’m not sure if this update is good or bad, feels confusing.",
    "This restaurant served cold food, really disappointed.",
    "Best weekend trip ever, the views were breathtaking!",
    "The app keeps crashing after the update, so frustrating!",
    "It’s an average product, does the job but nothing amazing.",
    "Finally achieved my fitness goal, feeling proud and motivated!"
]



sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = sia.polarity_scores(text)
    if score["compound"] >= 0.05:
        return "Positive"
    elif score["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

results = [(text, get_sentiment(text)) for text in posts]

for text, sentiment in results:
    print(f"{text} --> {sentiment}".encode("utf-8", errors="ignore").decode("utf-8"))

sentiments = [s for _, s in results]

plt.figure(figsize=(6,4))
sns.countplot(x=sentiments, palette="Set2")
plt.title("Sentiment Distribution of Social Media Posts")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
