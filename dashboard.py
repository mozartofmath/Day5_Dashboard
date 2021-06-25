import streamlit as st
import pandas as pd
import numpy as np
from database_operations import db_execute_fetch
import matplotlib.pyplot as plt

def main():
    st.title("Dashboard")

#    st.write('''
#    # Explore different classifier
#    Which one is the best?
#    ''')

    app_mode = st.sidebar.selectbox("Choose what you want to see from this box.", ("Visualize Data","Topic Modelling", "Sentiment Analysis"))
    if app_mode == 'Visualize Data':
        st.write('''
        ## Explore The Data
        Here are the first 5 tweets in my database.
        ''')
        dataframe = db_execute_fetch("Select * from cleantweetinfo where (id < 6);", tablename='cleantweetinfo', dbName = 'tweets')
        st.table(dataframe)
        #dataframe = db_execute_fetch("Select polarity from cleantweetinfo where (id < 200)", tablename='cleantweetinfo', dbName = 'tweets')
        def summerize(polarity):
            pos, neu, neg = 0, 0, 0
            for x in polarity:
                if x < 0:
                    pos += 1
                elif x == 0:
                    neu += 1
                elif x > 0:
                    neg += 1
            return pos, neu, neg
        

        #st.table(dataframe)
    elif app_mode == 'Topic Modelling':
        st.write('''
        ## Topic Modelling
        Here's a visualization of my topic model using wordclouds.
        ''')
        st.image('wordcl.png')
    elif app_mode == 'Sentiment Analysis':
        st.write('''
        ## Sentiment Analysis
        In the sentiment analysis project, my SGDClassifier model achieved an accuracy of 97.9%, a precision of 0.987, a recall of 0.958, and an fscore of 0.971.
        Here is a plot of the confusion matrix.
        ''')
        st.image('confusion_matrix.png')
if __name__ == "__main__":
    main()