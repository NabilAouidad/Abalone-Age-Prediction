import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from distributions import plotBars, plotHistograms
from correlations import plotPairPlots, plotHeatMap
import joblib 

#st.set_option('deprecation.showPyplotGlobalUse', False)
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

def eda():
    tab1, tab2, tab3 = st.tabs(["About the dataset", "Data Distributions", "Data Relationships"])

    with tab1:
        shapeColumn, featuresColumn, descriptiveStatsColumn = st.columns(3)

        shapeColumn.subheader("Shape")
        shapeColumn.write(abalone_df.shape)

        featuresColumn.subheader("Features")
        featuresColumn.write(pd.DataFrame({"Column Name" : abalone_df.columns}))

        descriptiveStatsColumn.subheader("Descriptive Statistics")
        descriptiveStatsColumn.dataframe(abalone_df.describe())

        st.subheader("Data Sample")
        st.dataframe(abalone_df.sample(20))

    with tab2:
        st.subheader("Bar Plots")
        st.plotly_chart(plotBars(abalone_df))

        st.subheader("Histograms")
        st.plotly_chart(plotHistograms(abalone_df))

    with tab3:
        st.subheader("Pair Plot")
        st.plotly_chart(plotPairPlots(abalone_df))

        st.subheader("Heat Map")
        st.plotly_chart(plotHeatMap(abalone_df))

st.sidebar.title("Options")

box_values = st.sidebar.selectbox(" ", options = ["EDA", "Make Predictions"])

if box_values == "EDA":
    eda()

model = joblib.load("AbalonePredictor.pkl")

if box_values == "Make Predictions":
    length = st.number_input("Length", 0.0, 0.815)
    diam = st.number_input("Diameter", 0.0, 0.65)
    height = st.number_input("Height", 0.0, 1.15)
    whole = st.number_input("Whole Weight", 0.0, 3.0)
    shucked = st.number_input("Shucked Weight", 0.0, 1.5)
    viscera = st.number_input("Viscera Weight", 0.0, 0.8)
    shell = st.number_input("Shell Weight", 0.0, 1.0)
    sex_selectbox = st.selectbox("Sample Sex", options = ["M", "F", "I"])

    if sex_selectbox == "M":
        st.subheader("Sample Age")
        st.write(model.predict([[length, diam, height, whole, shucked, viscera, shell, 1.0, 0.0, 0.0]]))

    if sex_selectbox == "F":
        st.subheader("Sample Age")
        st.write(model.predict([[length, diam, height, whole, shucked, viscera, shell, 0.0, 1.0, 0.0]]))

    if sex_selectbox == "I":
        st.subheader("Sample Age")
        st.write(model.predict([[length, diam, height, whole, shucked, viscera, shell, 0.0, 0.0, 1.0]]))
