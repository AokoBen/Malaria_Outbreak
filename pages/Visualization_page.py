import streamlit as st
import pandas as pd
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import dash
import plotly.figure_factory as ff 
   
   
st.title('Visualization Page')  
@st.cache
def load_data(nrows):
    data = pd.read_csv('malaria_outbreak.csv', nrows=nrows)
    return data

df = load_data(72)



fig = px.scatter(df, x="MVP", y="Malarial Cases", color="Rainfall", trendline='ols',trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
        st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
with tab2:
        st.plotly_chart(fig, theme=None, use_conatiner_width=True)

fig = px.scatter(df, x="Relative Humidity 2(1400hrs)", y="Rainfall", color="Malarial Cases", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
        st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
with tab2:
        st.plotly_chart(fig, theme=None, use_conatiner_width=True)



#comparativve analysis of the effect of temperature on malarial cases
st.subheader(f"Comparative analysis of effect of temperature on malarial cases")
fig = px.scatter(df, x="Max-Temperature", y="Malarial Cases", color="MVP", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
        st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
with tab2:
        st.plotly_chart(fig, theme=None, use_conatiner_width=True)

fig = px.scatter(df, x="Min-Temperature", y="Malarial Cases", color="MVP", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
        st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
with tab2:
        st.plotly_chart(fig, theme=None, use_conatiner_width=True)
        

#comparativve analysis of the effect of humidity on malarial cases
st.subheader(f"Comparative analysis of effect of humidity on malarial cases")
fig = px.scatter(df, x="Relative Humidity 1(0800hrs)", y="Malarial Cases", color="Rainfall", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
        st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
with tab2:
        st.plotly_chart(fig, theme=None, use_conatiner_width=True)

fig = px.scatter(df, x="Relative Humidity 2(1400hrs)", y="Malarial Cases", color="Rainfall", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
        st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
with tab2:
        st.plotly_chart(fig, theme=None, use_conatiner_width=True)
        


#comparativve analysis of effect of rainfall and vector population on malarial cases
st.subheader(f"Comparative analysis of effect of rainfall and vector population on malarial cases")
fig = px.scatter(df, x="Rainfall", y="Malarial Cases", color="Max-Temperature", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
        st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
with tab2:
        st.plotly_chart(fig, theme=None, use_conatiner_width=True)

fig = px.scatter(df, x="MVP", y="Malarial Cases", color="Max-Temperature", trendline='ols', trendline_color_override = 'red', title = 'Malaria Outbreak Prediction')
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
        st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
with tab2:
        st.plotly_chart(fig, theme=None, use_conatiner_width=True)



