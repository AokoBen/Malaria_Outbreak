Malaria Prediction Web App

Malaria is a life-threatening disease worldwide as the leading cause of illness and death. In Kenya however, malaria lacks comprehensive documentation on its incidences at both the national and county levels. There is therefore, need to develop systems that capture national and regional trends of malaria incidence, infection, and outbreak, so as to provide tailored intervention for prevention, monitoring of possible outbreak of malaria, and provision of mitigative measures against devastating effects of malaria in Kenya.

According to 2021 World Malaria Report, Malaria is one of the most severe public health problems worldwide, especially in poor tropical and subtropical areas of the world. Malaria is a leading cause of death and disease in many developing countries, where young children who have not developed immunity to malaria and pregnant women whose immunity have been decreased by pregnancy are most affected. Nearly half the world’s population live in areas at risk of malaria transmission in 87 countries and territories, which includes Kenya.

In 2020, malaria caused an estimated 241 million clinical episodes, and 627,000 deaths. Africa being the most affected due to a combination of factors such as:
•	Predominant and efficient mosquito parasite species Plasmodium falciparum responsible for high transmission and cause severe malaria and deaths.
•	Favorable local weather conditions which allow both vector and parasite development, and encourage malaria parasite transmission to occur year-round.
•	Scarce resources and socio-economic instability which hinder efficient malaria control interventions.

Malaria surveillance is therefore, a core component of an effective system to support elimination of malaria. Surveillance will not only enable countries to monitor progress towards elimination of malaria and develop targeted interventions for at-risk groups, but also boost efforts towards early detection of malaria outbreak and trigger a prompt response to malaria epidemics to minimise the impact of the illness including deaths and the socio-economic burden of malaria epidemics for the at-risk groups and regions of the population.

About Malaria Outbreak Prediction Model
Malaria Outbreak Prediction Model
This app is primed to assist public health workers to detect possibility of an early outbreak of malaria and suggest measures to mitigate the risks associated with an outbreak of the disease.

App Architecture Framework
The malaria outbreak prediction app is web based and acts as an early warning system for occurrence of malaria. Malaria outbreak is determined by calculating threshold for likely outbreak of malaria based on three frameworks namely; climatic variables, mosquito vector population and reported malaria cases.

i. Vector Based Framework
Malaria outbreak is attributed to plasmodium falciparum and plasmodium vivax parasites. This framework is based on meeting threshold for mosquito vector population as hosts for these disease causing parasites. In a herd of mosquito, the number of the two species of mosquito as host for the plasmodium parasites determines the likelihood of a malaria outbreak.

ii. Climate Based Framework
This framework emphasises how climate variability influence the growth of mosquitoes hence, their population. Favourable climatic condition is known to have an influence on growth of mosquito vector and parasites by offering perfect conditions for both to grow in number. Climate variables used in this app are: rainfall, maximum and minimum temperature, relative humidity (at 0800 and 14000hrs).

iii. Case Based Framework
The focus in this framework is the reported malaria cases in an area. Reported malaria cases is a direct indicator of malaria outbreak threat in a target area as a pointer to the presence of the disease within community.

App Usage
The model is built using machine learning pipeline and trained by decision tree algorithm. Prediction is done by analyzing aspects of the dataset which include malaria population, malaria cases and climate variables. The weather API is used to gather data for live climatic conditions of counties in Kenya, and users asked to provide herd mosquito vector population and number of reported malaria cases.

The algorithm then uses the supplied data to make prediction of the likelihood of a malaria outbreak. Prediction can be made even with some parameter values being zero and classified into three outcomes: HIGH ALERT, MILD ALERT and NO THREAT, and provides suggestions for control measures to address a possible malaria outbreak. The app is a two-stage application with the main page providing predictions and analysis of tables for prediction and train-test variables. The second stage provides visualization of graphs showing relationship between the different variables used to train and test the model.

Streamlit Dashboard Malaria Outbreak app url

https://aokoben-malaria-outbreak-app-7q8jpy.streamlit.app/
