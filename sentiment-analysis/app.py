import streamlit as st
from transformers import pipeline
print("Transformers pipeline imported successfully!")
# Load the sentiment analysis pipeline
@st.cache_resource
def load_pipeline():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

sentiment_analyzer = load_pipeline()

# Streamlit App
st.title("Sentiment Analysis App")
st.write("Enter a sentence or paragraph, and the app will predict if the sentiment is positive or negative.")

# Input box for user
user_input = st.text_area("Enter your text here:", placeholder="Type something...")

if st.button("Analyze"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            result = sentiment_analyzer(user_input)
        sentiment = result[0]["label"]
        confidence = result[0]["score"]
        st.success(f"Sentiment: **{sentiment}** with confidence **{confidence:.2f}**")
    else:
        st.error("Please enter some text!")
