import streamlit as st
import pandas as pd
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import dash
import plotly.figure_factory as ff 
import plotly.graph_objects as go


st.set_page_config(
    page_icon="✅",
    layout="wide",
)

st.title('Malaria Outbreak Prediction Model')
st.header('Visualize relationships in Train-Test dataset') 

#read dataset used for training and testing the model
#malaria_outbreak_df = pd.read_csv('malaria_outbreak.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv('malaria_outbreak.csv', nrows=nrows)
    return data

df = load_data(72)

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
        fig = px.scatter(df, x="MVP", y="MalarialCases", color="Rainfall", trendline='ols',trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_conatiner_width=True)

with fig_col2:
        fig = px.scatter(df, x="RelativeHumidity_2(1400hrs)", y="Rainfall", color="MalarialCases", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_conatiner_width=True)



#comparativve analysis of the effect of temperature on malarial cases
with fig_col1:
        st.subheader(f"Comparative analysis of effect of")
        fig = px.scatter(df, x="MaxTemperature", y="MalarialCases", color="MVP", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_conatiner_width=True)

with fig_col2:
        st.subheader(f"temperature on malarial cases")
        fig = px.scatter(df, x="MinTemperature", y="MalarialCases", color="MVP", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_conatiner_width=True)
        

#comparativve analysis of the effect of humidity on malarial cases
with fig_col1:
        st.subheader(f"Comparative analysis of effect of")
        fig = px.scatter(df, x="RelativeHumidity_1(0800hrs)", y="MalarialCases", color="Rainfall", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_conatiner_width=True)

with fig_col2:
        st.subheader(f"humidity on malarial cases")
        fig = px.scatter(df, x="RelativeHumidity_2(1400hrs)", y="MalarialCases", color="Rainfall", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_conatiner_width=True)
        

#comparativve analysis of effect of rainfall and vector population on malarial cases
with fig_col1:
        st.subheader(f"Analysis of effect of rainfall and vector")
        fig = px.scatter(df, x="Rainfall", y="MalarialCases", color="MaxTemperature", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_conatiner_width=True)

with fig_col2:
        st.subheader(f"population on malarial cases")
        fig = px.scatter(df, x="MVP", y="MalarialCases", color="MaxTemperature", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        with tab2:
                st.plotly_chart(fig, theme=None, use_conatiner_width=True)


#visualize mean, quartile ranges, min, max values of variables through box plots
trace0 = go.Box(
    y=df.MalarialCases,
    boxpoints='all',
    name = 'Malaria Cases',
    marker = dict(
        color = 'rgb(12, 122, 140)',
    )
)

data = [trace0]
with fig_col1:
        fig = go.Figure(data=data)
        fig.update_layout(
        title="Malaria Cases"  
        )
        with tab1:
                 st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        #with tab2:
                #st.plotly_chart(fig, theme=None, use_conatiner_width=True)

trace1 = go.Box(
    y=df.Rainfall,
    boxpoints='all',
    name = 'Rainfall',
    marker = dict(
        color = 'rgb(12, 12, 140)',
    )
)

#-------------------------------------
trace2 = go.Box(
    y=df.MalarialCases,
    boxpoints='all',
    name = 'Malarial Cases',
    marker = dict(
        color = 'rgb(80, 122, 190)',
    )
)
data = [trace1, trace2]
with fig_col2:
        fig = go.Figure(data=data)
        fig.update_layout(
        title="Rainfall Vs Malaria Cases"  
        )
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        #with tab2:
                #st.plotly_chart(fig, theme=None, use_conatiner_width=True)


trace3 = go.Box(
    y=df['MVP'],
    boxpoints='all',
    name = 'Mosquito Population',
    marker = dict(
        color = 'rgb(200, 28, 128)',
    )
)

trace4 = go.Box(
    y=df.MalarialCases,
    boxpoints='all',
    name = 'Malarial Cases',
    marker = dict(
        color = 'rgb(50, 100, 200)',
    )
)

data = [trace3, trace4]
with fig_col1:
        fig = go.Figure(data=data)
        fig.update_layout(
        title="Mosquito population Vs Malaria Cases"  
        )
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        #with tab2:
                #st.plotly_chart(fig, theme=None, use_conatiner_width=True)


trace5 = go.Box(
    y=df['MaxTemperature'],
    boxpoints='all',
    name = 'Maximun Temperature',
    marker = dict(
        color = 'rgb(150, 100, 100)',
    )
)

trace6 = go.Box(
    y=df['MinTemperature'],
    boxpoints='all',
    name = 'Minimum Temperature',
    marker = dict(
        color = 'rgb(15, 100, 250)',
    )
)
data = [trace5, trace6]
with fig_col2:
        fig = go.Figure(data=data)
        fig.update_layout(
        title="Temperature ranges"  
        )
        with tab1:
                st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        #with tab2:
                #st.plotly_chart(fig, theme=None, use_conatiner_width=True)

