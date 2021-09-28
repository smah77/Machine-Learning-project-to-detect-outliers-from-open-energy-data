
# Code of my thesis Topic:“Outlier Detection on Open Energy Data”

The thesis was based on:
•       Analyzing Machine Learning and statistical methods to find out the best approach for “Outlier Detection on Open Energy Data”
•	ML Approaches: DBSCAN, SNN Clustering, KNN,  local outlier factor(LOF-a variant of KNN)
•	Statistical Methods: Box plot rule, Static histogram-based approach, Dynamic histogram-based approach

"Open Energy Data" is part of the project, “openFRED” funded by “The Federal Ministry for Economic Affairs and Energy” (BMWi). This "open_FRED" project was jointly run by Reiner Lemoine Institut, Otto-von-Guericke University Magdeburg (OvGU) and The Helmholtz-Zentrum Geesthacht. Open_eGo is an older project from which the new project "open_FRED" was started [1, 39]. In open_eGo, there was an open energy database (oedb). Users could upload their data and look at data via a website [2]. The goals of "open_FRED" [1, 39] are to create and maintain a database on weather data which is accessible by everyone, to make it more user-friendly and add more functionality, and to ensure transparency of using funds from the state.

"open_FRED" [1] data consists of temperature, air pressure, perpendicular sunlight and inclined sunlight collected from different geographical positions of sensors of windmills in Germany. Another goal of "open_FRED" is to provide a facility to research future energy and to compare the output of those researches [1]. Much data from different sources will be added or integrated into this database. It is necessary to keep the database free from outliers for any model or application to be built based on this database to be more faultless and more efficient and effective.

