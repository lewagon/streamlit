import pandas as pd
import streamlit as st


def title():
    return 'File uploader 🎥'


def run():

    with st.echo():

        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            st.write(data)
