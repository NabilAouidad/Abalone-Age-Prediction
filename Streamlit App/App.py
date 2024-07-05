import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from distributions import plotBars, plotHistograms
from correlations import plotPairPlots, plotHeatMap

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout = "wide", page_title = "Abalone EDA")

style = """
    <style>
    button[data-baseweb="tab"] {
        margin: 0 auto;
    }

    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.3rem;
    }
    </style>
    """

st.markdown(style, unsafe_allow_html = True)

container = st.container(height = 125, border = False)
container.write('<h1 style="text-align: center;">Exploratory Data Analysis of the Abalone Dataset</h1>', 
         unsafe_allow_html=True)

st.empty()