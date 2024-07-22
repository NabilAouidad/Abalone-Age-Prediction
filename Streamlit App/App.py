import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from distributions import plotBars, plotHistograms
from correlations import plotPairPlots, plotHeatMap

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout = "wide", page_title = "Abalone Age Prediction")

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
container.write('<h1 style="text-align: center;">Abalone Age Prediction Web App</h1>', 
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

    return 

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

def eda():
    tab1, tab2, tab3 = st.tabs(["About the dataset", "Data Distributions", "Data Relationships"])

    with tab1:
        st.write(showDatasetInfo())

    with tab2:
        st.write(showDataDistributions())

    with tab3:
        st.write(showCorrelations())

st.sidebar.title("Options")

box_values = st.sidebar.selectbox(" ", options = ["EDA", "Make Predictions"])

if box_values == "EDA":
    eda()

if box_values == "Make Predictions":
    st.write("Nothing to predict for the moment!")