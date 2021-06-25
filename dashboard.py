import streamlit as st
import pandas as pd
import numpy as np
from database_operations import db_execute_fetch

def main():
    st.title("Dashboard")

#    st.write('''
#    # Explore different classifier
#    Which one is the best?
#    ''')

    app_mode = st.sidebar.selectbox("Choose what you want to see from this box.", ("Visualize Data","Topic Modelling", "Sentiment Analysis"))
    if app_mode == 'Visualize Data':
        st.write('''
        # Explore The Data
        Do you like the presentation?
        ''')
        dataframe = db_execute_fetch("Select * from cleantweetinfo where (id < 6);", tablename='cleantweetinfo', dbName = 'tweets')
        st.table(dataframe)
    elif app_mode == 'Topic Modelling':
        st.write('''
        # Explore Topic Modelling
        Do you like the performance?
        ''')
        st.image('wordcl.png')
    elif app_mode == 'Sentiment Analysis':
        st.write('''
        # Explore Sentiment Analysis
        Do you like the Accuracy?
        ''')
        st.image('confusion_matrix.png')
if __name__ == "__main__":
    main()