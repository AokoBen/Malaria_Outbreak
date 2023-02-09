Malaria Prediction Web App

Malaria is a life-threatening disease worldwide as the leading cause of illness and death. In Kenya however, malaria lack comprehensive documentation on its incidences at the national and county levels. There is need to develop systems that capture national and regional trends of malaria incidence, infection, and outbreak, to provide tailored intervention for prevention, monitoring of possible outbreak of malaria, and provision of mitigative measures against devastating effects of malaria in Kenya.

According to 2021 World Malaria Report, Malaria is one of the most severe public health problems worldwide, especially in poor tropical and subtropical areas of the world. Malaria is a leading cause of death and disease in many developing countries, where young children who have not developed immunity to malaria and pregnant women whose immunity have been decreased by pregnancy are most affected. Nearly half the world’s population live in areas at risk of malaria transmission in 87 countries and territories, which include Kenya.

In 2020, malaria caused an estimated 241 million clinical episodes, and 627,000 deaths. Africa being the most affected due to a combination of factors such as:
•	Predominant and efficient mosquito parasite species Plasmodium falciparum responsible for high transmission and cause severe malaria and deaths.
•	Favorable local weather conditions which allow both vector and parasite development, and encourage malaria parasite transmission to occur year-round.
•	Scarce resources and socio-economic instability which hinder efficient malaria control interventions.

Malaria surveillance is therefore, a core component of an effective system to support elimination of malaria. Surveillance will not only enable countries to monitor progress towards elimination of malaria and develop targeted interventions for at-risk groups, but also boost efforts towards early detection of malaria outbreak and trigger a prompt response to malaria epidemics to minimise the impact of the illness including deaths and the socio-economic burden of malaria epidemics for at-risk groups and regions of the population.

This app is primed to assist public health workers in their effort to detect possibility of an early outbreak of malaria and line up appropriate intervention measures to mitigate the risks associated with an outbreak of the disease.

Architecture framework

The malaria prediction app is a web based up designed to act as an early warning system for malaria outbreak occurrence. Malaria outbreak is determined through calculating the threshold limit for which past that an outbreak is likely to occur. Climate change is known to have an influence on growth of parasites by either offering perfect conditions for parasites to increase in number or reduce in number. The malaria web app works based on three frameworks from which its architecture is built from:

i.	Vector Based Framework
Malaria is caused by plasmodium falciparum and plasmodium vivax which are the common threats attributed to malaria. This framework works based on mosquito population. In a herd of mosquitos, the number of the two species of mosquito will determine if there is a likelihood of a malaria outbreak.

ii.	Climate Based Framework
In this framework, the main emphasis is on how climate variability influence the growth of mosquitoes hence increasing or decreasing their population. Climate variables used for this web app are, rainfall, max and min temperature, relative humidity (at 0800 and 14000hrs).

iii.	Case Based Framework
For this framework, our focus is in the cases reported. The cases reported is a direct indicator of the threat species in the area.

App Usage

The app is built using machine learning where the dataset is collected, cleaned and undergo feature engineering and is trained using different machine learning algorithms. One important thing to be noted is, the algorithm uses the above discussed framework to predict the likelihood of an outbreak. The algorithm used for this is decision tree, the prediction is done from analyzing the vector aspect of the dataset, the climate variables and cases. This means that the prediction can be made even with some parameter values as zero. A weather api is used to gather live climatic conditions of counties of Kenya and the user is asked to give herd population and number of cases reported then the algorithm can do the prediction. The prediction is classified into three outcomes, ‘HIGH ALERT’, ‘MILD ALERT’ and NO THREAT for which control measure approaches are provide to the users.
The app is a two-page application with the main page for the prediction purpose while the second page is the visualization page where graphs that show the different relationship of variables is used. The graphs are built using plotly which makes them interactive with zoom in and zoom out features available as well as the employing different themes. 

Streamlit Dashboard Malaria Outbreak app url

https://aokoben-malaria-outbreak-app-7dwpxn.streamlit.app/
