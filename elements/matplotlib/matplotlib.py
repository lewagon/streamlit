import numpy as np
import streamlit as st


def run():

    with st.echo():

        import matplotlib.pyplot as plt

        x = np.arange(-1,1.00001,0.1)
        y = x**3

        fig, ax = plt.subplots()

        ax.plot(x, y, label="A curve")
        ax.plot(x, x, label="Identity function")
        ax.legend()

        st.pyplot(fig)
