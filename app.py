import streamlit as st
import pandas as pd
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import dash
import plotly.figure_factory as ff
import requests
import json
import pickle
import streamlit.components.v1 as components



#set main page title  
st.title("Malaria Outbreak Prediction Model")

#load saved model
loaded_model = pickle.load(open('malaria_model.sav', 'rb'))

#define malaria prediciton function
def malaria_prediction(input_list):

    input_data_as_numpy_array = np.asarray(input_list)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==1): #and (selected_county == malaria_endemic_counties)
        text = "HIGH ALERT!!! <br/> Malaria Outbreak is anticipated in " + selected_county + " County.<br/><br/> CONTROL MEASURES: <br/>Use vector control; Indoor Residual Spraying (IRS), Insecticide-treated bed nets (ITNs), case management, vaccine administration and public sensitization. <br/><br/> MALARIA ENDEMIC COUNTIES:<br/>"+ malaria_endemic_counties
        colour = "red"
    elif (prediction[0]==0 and (case == 0 and mosqp == 0)):  
        text = 'NO THREAT... <br/> Malaria outbreak is currently NOT anticipated in ' + selected_county + ' County. <br/><br/> MALARIA ENDEMIC COUNTIES:<br/>' + malaria_endemic_counties
        colour = "green"
    else:
        text = 'MILD ALERT!!! <br/>Mild Malaria Outbreak is anticipated in ' + selected_county + ' County. <br/>Health officials in the county should be on alert and engage in public education and sensitization:<br/><br/>CONTROL MEASURES: <br/>Use antimalaria prophylaxis, Indoor Residual Spraying (IRS), Insecticide-treated bed nets (ITNs). <br/><br/> MALARIA ENDEMIC COUNTIES:<br/>' + malaria_endemic_counties
        colour = "orange"
        
    st.markdown(f"<div style='background-color: {colour}; padding: 10px;'>{text}</div>", unsafe_allow_html=True)

    return prediction

#set weather API for live weather data  
API_KEY = '10908cb3ca2b510064ad0549d8d857dc'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

#create counties
counties = ["Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu", "Taita Taveta", "Garissa", "Wajir", "Mandera", "Marsabit",
            "Isiolo", "Meru", "Tharaka Nithi", "Embu", "Kitui", "Machakos", "Makueni", "Nyandarua", "Nyeri", "Kirinyaga",
            "Murang'a", "Kiambu", "Turkana", "West Pokot", "Samburu", "Trans Nzoia", "Uasin Gishu", "Elgeyo Marakwet",
            "Nandi", "Baringo", "Laikipia", "Nakuru", "Narok", "Kajiado", "Kericho", "Bomet", "Kakamega", "Vihiga",
            "Bungoma", "Busia", "Siaya", "Kisumu", "Homa Bay", "Migori", "Kisii", "Nyamira","Nairobi"]

malaria_endemic_counties = "Kericho, Busia, Homa Bay, Kisumu, Siaya, Migori, Mombasa, Kakamega, Bungoma, Vihiga, Nairobi"
#create prompt for County data input
st.sidebar.header('User Input')
selected_county = st.sidebar.selectbox('Select or type County name or number',counties)
#url = BASE_URL+ 'appid=' + API_KEY + '&q='+ selected_county

#set url for live weather data requests for selected county
url = BASE_URL+ 'appid=' + API_KEY + '&q='+ selected_county
response = requests.get(url)

#process live weather data for the selected county & check for possible weather API request errors
if response.status_code == 200:
        data = response.json()

#store features to the main function
        main = data['main']

#process and store county weather data from  api
        rainfall = [data["rain"]["3h"] if "rain" in data else 0] #set rain to 0 if at the time of request there is no rain  
        temp_min =main['temp_min']
        temp_max = main['temp_max']
        humidity1 = main["humidity"]
        humidity2 = main["humidity"]

#display collected weather data for selected coounty 
        st.write(f"Selected County: {selected_county}")
        st.write(f"Min-temperature in kelvin: {temp_min}")
        st.write(f"Max-temperature in kelvin: {temp_max} ")
        st.write(f"Relative humidity 0800hrs in %: {humidity1}")
        st.write(f"Relative humidity 1400hrs in %: {humidity2}")
        st.write(f"Rainfall in mm: {rainfall}")


#collect additional input/parameter from user
        mosqp = st.sidebar.slider('Set Mosquito vector population',min_value=0, max_value=1000)
        case = st.sidebar.slider('Set number of reported malaria cases',min_value=0, max_value=5000)

        columns = ['rainfall','min_temp', 'max_temp', 'humidity1', 'humidity2', 'mosqp','case']
        
        #creat dataframe of the columns
        df = pd.DataFrame(columns=columns)
        df.loc[0] = ([data["rain"]["3h"] if "rain" in data else 0,main['temp_min'],main['temp_max'],main['humidity'], main['humidity'],mosqp,case])
    
    
        input_list = df

        diagnosis = ""
       
        if st.button("Predict"):
        # Pass the input values to your model and get the output
           diagnosis = malaria_prediction(input_list)
           st.success(diagnosis)


elif response.status_code == 10060: 
        st.write("ConnectionError: Connection aborted because remote server did not respond in time")
        
elif response.status_code == 10051: 
        st.write("WinError: Failed to establish a new connection")

elif response.status_code == 11001: 
        st.write("ConnectionError: Connection Failed...")

else:
        st.write("HTTP request Error: Weather data for selected County not available")




st.sidebar.header("Analytics")


menu = ['Display Data ','About']
selection = st.sidebar.selectbox("Select menu: ", menu)

if selection== 'Display Data ':

# display data for selected county
    st.markdown(f'Display prediction data for {selected_county} County.')
    st.write(df.head())


# shape of data
if st.checkbox("show shape "):
    
     st.write('Data Shape')
     st.write('{:,} rows; {:,} columns'.format(df.shape[0], df.shape[1]))


# adding html  Template

footer_temp = """
	 <!-- CSS  -->
	  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	  <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	  <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
	 <footer class="page-footer grey darken-4">
	    <div class="container" id="aboutapp">
	        <div class="row">
	            <div class="col l6 s12">
	                <h5 class="white-text">Malaria Outbreak Prediction Model</h5>
	          <p class="grey-text text-lighten-4">This app is primed to assist public health workers to detect possibility of an early outbreak of malaria and suggest measures to mitigate the risks associated with an outbreak of the disease.</br></br>

<strong>App Architecture Framework</strong></br>

The malaria outbreak prediction app is web based and acts as an early warning system for occurrence of malaria. Malaria outbreak is determined through calculating threshold for likely outbreak of malaria based on three frameworks of climate, mosquito vector population and reported malaria cases.</br></br>

<strong>i.	Vector Based Framework</strong></br>
Malaria outbreak is attributed to plasmodium falciparum and plasmodium vivax parasites. This framework is based on mosquito vector population. In a herd of mosquito, the number of the two species of mosquito will determines the likelihood of malaria outbreak.</br></br>

<strong>ii.	Climate Based Framework</strong></br>
This framework emphasises how climate variability influence the growth of mosquitoes hence increase or decrease their population. Climate change is known to have an influence on growth of mosquito vector and parasites by offering perfect conditions for parasites to grow in number. Climate variables used for this web app are: rainfall, max and min temperature, relative humidity (at 0800 and 14000hrs).</br></br>

<strong>iii.	Case Based Framework</strong></br>
The focus in this framework is reported malaria cases. Reported malaria cases is a direct indicator of malaria threat species in the area.</br></br>

<strong>App Usage</strong></br>

The app is built using machine learning pipeline and trained using decision tree algorithm. Prediction is done by analyzing aspects of the dataset which include malaria population, climate and malaria cases variables. Prediction can therefore be made even with some parameter values being zero. Weather API is used to gather live climatic conditions of counties in Kenya and users asked to provide herd mosquito vector population and number of reported malaria cases.</br></br> The algorithm then uses the framework to predict likelihood of a malaria outbreak. Prediction is classified into three outcomes: ‘HIGH ALERT’, ‘MILD ALERT’ and NO THREAT, and suggests control measures to address a possible malaria outbreak.

The app is a two-page application with the main page for the prediction purpose while the second page is the visualization of tables and graphs showing relationship between different variables. </p>
	              </div>

	              
	            </div>
	          </div>
	          <div class="footer-copyright">
	          <div class="container">
	          Right click on the link to <a class="white-text text-lighten-3" href="https://aokoben-malaria-outbreak-app-7dwpxn.streamlit.app/">View Malaria Outbreak App on Streamlit. </a><br/>
	          <a class="white-text text-lighten-3" href="https://aokoben-malaria-outbreak-app-7dwpxn.streamlit.app/"></a>
	      </div>
	    </div>
	  </footer>

	"""

if selection== 'About':
    st.subheader("About App")
    components.html(footer_temp, height=1500)



#endemicity = ""
#endemic_county = ""
#def malaria_endemicity(endemic_county):
    
#     if (selected_county == malaria_endemic_counties):
#         return selected_county + 'is malaria endemic'
#     else:
#         return 'No endemicity reports for ' + selected_county
#endemicity = malaria_endemicity(endemic_county)
 
