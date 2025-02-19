import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# ---------------- Dummy Login ---------------- #
def check_user(username, password):
    return username == "admin" and password == "admin"

def login():
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            if check_user(username, password):
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success("Logged in successfully!")
            else:
                st.error("Incorrect username or password")

# ---------------- Overview ---------------- #
def overview():
    st.subheader("Dataset Overview")
    # Dummy summary metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Tweets", "1,000")
    col2.metric("Active Users", "150")
    col3.metric("Hashtags Tracked", "50")
    
    # Dummy line chart: Tweets over time
    dates = pd.date_range(end=datetime.today(), periods=30)
    tweets = np.random.randint(50, 200, size=30)
    df = pd.DataFrame({"Date": dates, "Tweets": tweets})
    fig = px.line(df, x="Date", y="Tweets", title="Tweets Over Time", markers=True)
    st.plotly_chart(fig)

# ---------------- User Analysis ---------------- #
def user_analysis():
    st.subheader("User Analysis")
    # Dummy user list
    users = ["alice", "bob", "charlie", "dave"]
    selected_user = st.selectbox("Select a User", users)
    
    # Dummy user details
    user_details = {
        "Username": selected_user,
        "User ID": random.randint(1000, 9999),
        "Description": f"This is a dummy description for {selected_user}.",
        "Followers": random.randint(100, 1000),
        "Following": random.randint(50, 500),
        "Tweets": random.randint(100, 1000)
    }
    
    st.markdown(f"""
        <div style="background-color:#f1f1f1; padding:10px; border-radius:10px;">
            <h3>User Details</h3>
            <p><strong>Username:</strong> {user_details['Username']}</p>
            <p><strong>User ID:</strong> {user_details['User ID']}</p>
            <p><strong>Description:</strong> {user_details['Description']}</p>
            <p><strong>Followers:</strong> {user_details['Followers']}</p>
            <p><strong>Following:</strong> {user_details['Following']}</p>
            <p><strong>Tweets:</strong> {user_details['Tweets']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Dummy sentiment distribution for the user
    sentiments = ["Positive", "Negative", "Neutral"]
    sentiment_counts = [random.randint(10, 100) for _ in sentiments]
    df_sent = pd.DataFrame({"Sentiment": sentiments, "Count": sentiment_counts})
    fig_pie = px.pie(df_sent, names="Sentiment", values="Count", title="Sentiment Distribution")
    st.plotly_chart(fig_pie)
    
    # Dummy bar chart for user engagement
    metrics = ["Tweets", "Retweets"]
    counts = [random.randint(50, 300), random.randint(20, 150)]
    df_bar = pd.DataFrame({"Metric": metrics, "Count": counts})
    fig_bar = px.bar(df_bar, x="Metric", y="Count", title="User Engagement")
    st.plotly_chart(fig_bar)

# ---------------- Hashtag Analysis ---------------- #
def hashtag_analysis():
    st.subheader("Hashtag Analysis")
    hashtags = ["COVID", "Tech", "Sports", "News", "Music"]
    selected_hashtag = st.selectbox("Select a Hashtag", hashtags)
    
    # Dummy hashtag details
    total_used = random.randint(100, 500)
    frequently_used_with = random.sample([tag for tag in hashtags if tag != selected_hashtag], k=2)
    
    st.markdown(f"""
        <div style="background-color:#f1f1f1; padding:10px; border-radius:10px;">
            <h3>Hashtag Details</h3>
            <p><strong>Hashtag:</strong> #{selected_hashtag}</p>
            <p><strong>Total Times Used:</strong> {total_used}</p>
            <p><strong>Frequently Used With:</strong> {', '.join(frequently_used_with)}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Dummy line chart: Hashtag usage over time
    dates = pd.date_range(end=datetime.today(), periods=30)
    usage = np.random.randint(5, 50, size=30)
    df_usage = pd.DataFrame({"Date": dates, "Usage": usage})
    fig_line = px.line(df_usage, x="Date", y="Usage", title=f"Usage of #{selected_hashtag} Over Time", markers=True)
    st.plotly_chart(fig_line)
    
    # Dummy sentiment distribution pie chart
    sentiments = ["Positive", "Negative", "Neutral"]
    sentiment_counts = [random.randint(10, 100) for _ in sentiments]
    df_sent = pd.DataFrame({"Sentiment": sentiments, "Count": sentiment_counts})
    fig_sent = px.pie(df_sent, names="Sentiment", values="Count", title="Sentiment Distribution")
    st.plotly_chart(fig_sent)
    
    # Dummy emotion distribution bar chart
    emotions = ["Joy", "Anger", "Sadness", "Fear", "Surprise"]
    emotion_counts = [random.randint(5, 50) for _ in emotions]
    df_emotion = pd.DataFrame({"Emotion": emotions, "Count": emotion_counts})
    fig_emotion = px.bar(df_emotion, x="Emotion", y="Count", title="Emotion Distribution")
    st.plotly_chart(fig_emotion)
    
    # Dummy language distribution pie chart
    languages = ["en", "es", "fr", "de", "it"]
    lang_counts = [random.randint(20, 80) for _ in languages]
    df_lang = pd.DataFrame({"Language": languages, "Count": lang_counts})
    fig_lang = px.pie(df_lang, names="Language", values="Count", title="Language Distribution")
    st.plotly_chart(fig_lang)

# ---------------- Tweet Analysis ---------------- #
def tweet_analysis():
    st.subheader("Tweet Analysis")
    search_query = st.text_input("Enter search query for tweets", value="dummy")
    if st.button("Search"):
        # Create dummy tweet data
        tweet_data = [
            {
                "Tweet ID": random.randint(100000, 999999),
                "User": random.choice(["alice", "bob", "charlie", "dave"]),
                "Text": f"This is a dummy tweet about {search_query}.",
                "Created At": (datetime.today() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d"),
                "Sentiment": random.choice(["Positive", "Negative", "Neutral"]),
                "Emotion": random.choice(["Joy", "Anger", "Sadness", "Fear", "Surprise"]),
                "Language": random.choice(["en", "es", "fr"])
            }
            for _ in range(10)
        ]
        df_tweets = pd.DataFrame(tweet_data)
        st.dataframe(df_tweets)
        
        # Dummy line chart: Tweets per day
        tweet_counts = df_tweets.groupby("Created At").size().reset_index(name="Count")
        fig_line = px.line(tweet_counts, x="Created At", y="Count", title="Tweets Per Day", markers=True)
        st.plotly_chart(fig_line)
        
        # Dummy pie chart: Sentiment distribution
        sentiment_counts = df_tweets["Sentiment"].value_counts().reset_index()
        sentiment_counts.columns = ["Sentiment", "Count"]
        fig_pie = px.pie(sentiment_counts, names="Sentiment", values="Count", title="Sentiment Distribution")
        st.plotly_chart(fig_pie)
        
        # Dummy bar chart: Emotion distribution
        emotion_counts = df_tweets["Emotion"].value_counts().reset_index()
        emotion_counts.columns = ["Emotion", "Count"]
        fig_bar = px.bar(emotion_counts, x="Emotion", y="Count", title="Emotion Distribution")
        st.plotly_chart(fig_bar)

# ---------------- Main App ---------------- #
def main():
    st.set_page_config(page_title="Dummy Twitter Data App", layout="wide")
    st.markdown("""
        <style>
            /* Custom sidebar styling */
            .sidebar .sidebar-content {
                background-color: #1e3d58;
                color: #ffffff;
            }
            /* Custom styling for main content */
            .css-1kyxreq {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Initialize login state if not set
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    
    # Sidebar Navigation
    with st.sidebar:
        st.image("logo.png", width=100)  # Optional logo
        if st.session_state["logged_in"]:
            nav = st.radio("Navigation", ["Overview", "User Analysis", "Hashtag Analysis", "Tweet Analysis"])
        else:
            nav = "Login"
    
    # Login screen
    if not st.session_state["logged_in"]:
        st.header("Please Log In")
        login()
        st.stop()
    
    # Render selected page
    if nav == "Overview":
        overview()
    elif nav == "User Analysis":
        user_analysis()
    elif nav == "Hashtag Analysis":
        hashtag_analysis()
    elif nav == "Tweet Analysis":
        tweet_analysis()

if __name__ == "__main__":
    main()
