
import streamlit as st

import numpy as np
import pandas as pd


def run():

    with st.echo():

        @st.cache_data
        def get_slider_data():

            return pd.DataFrame({
                  'first column': list(range(1, 11)),
                  'second column': np.arange(10, 101, 10)
                })

        df = get_slider_data()

        option = st.slider('Select a modulus', 1, 10, 3)

        filtered_df = df[df['first column'] % option == 0]

        st.write(filtered_df)
