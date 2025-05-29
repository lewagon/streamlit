
import streamlit as st

import numpy as np
import pandas as pd


def title():
    return 'Hiding index'


def run():

    with st.echo():

        @st.cache_data
        def get_dataframe_data():

            return pd.DataFrame(
                    np.random.randn(10, 5),
                    columns=('col %d' % i for i in range(5))
                )

        df = get_dataframe_data()

        hdf = df.assign(hack='').set_index('hack')

        st.write(hdf.head())
