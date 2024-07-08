
# from newspaper import Article

# url='https://en.wikipedia.org/wiki/Mathematics'
# article=Article(url)
# article.download()
# article.parse()
# article.nlp()

# text=article.summary
import streamlit as st
from textblob import TextBlob

# Streamlit interface
st.title("Sentiment Analysis with TextBlob")

st.write("Enter a text below to analyze its sentiment:")

user_input = st.text_area("Text input", "I am so much happy. I am so much sad. I am so much angry. I am so much excited. I am so much scared. I am so much disgusted. I am so much surprised")

if st.button("Analyze Sentiment"):
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        sentiment_text = "Positive"
    elif sentiment < 0:
        sentiment_text = "Negative"
    else:
        sentiment_text = "Neutral"

    st.write(f"Sentiment Polarity: {sentiment}")
    st.write(f"Sentiment: {sentiment_text}")
