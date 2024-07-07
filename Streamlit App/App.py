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

#-----------------------------------------------------------

abalone_df = pd.read_csv("abalone.csv")

def showDatasetInfo():
    shapeColumn, featuresColumn, descriptiveStatsColumn = st.columns(3)

    shapeColumn.subheader("Shape")
    shapeColumn.write(abalone_df.shape)

    featuresColumn.subheader("Features")
    featuresColumn.write(pd.DataFrame({"Column Name" : abalone_df.columns}))

    descriptiveStatsColumn.subheader("Descriptive Statistics")
    descriptiveStatsColumn.dataframe(abalone_df.describe())

    st.subheader("Data Sample")
    st.dataframe(abalone_df.sample(20))

def showDataDistributions():
    st.subheader("Bar Plots")
    st.plotly_chart(plotBars(abalone_df))

    st.subheader("Histograms")
    st.plotly_chart(plotHistograms(abalone_df))

def showCorrelations():
    st.subheader("Pair Plot")
    st.plotly_chart(plotPairPlots(abalone_df))

    st.subheader("Heat Map")
    st.plotly_chart(plotHeatMap(abalone_df))

st.sidebar.title("EDA Options")

box_values = st.sidebar.selectbox(" ", options = ["About the dataset", "Data Distributions", "Correlations"])

if box_values == "About the dataset":
    showDatasetInfo()

if box_values == "Data Distributions":
    showDataDistributions()

if box_values == "Correlations":
    showCorrelations()