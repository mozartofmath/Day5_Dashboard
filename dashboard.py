import streamlit as st

def main():
    st.title("Dashboard")

#    st.write('''
#    # Explore different classifier
#    Which one is the best?
#    ''')

    app_mode = st.sidebar.selectbox("My Models", ("Topic Modelling", "Sentiment Analysis"))
    if app_mode == 'Topic Modelling':
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