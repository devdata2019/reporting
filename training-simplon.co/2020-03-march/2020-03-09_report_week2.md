# report week 2 

# Monday 09 February 

- Stage start at Cerema as a deeplearner trainie 
- Getting dataset
- Start Murex project

# Thuesday 10 February 

https://towardsdatascience.com/loading-data-from-openstreetmap-with-python-and-the-overpass-api-513882a27fd0

https://www.data.gouv.fr/fr/datasets/parkings/

https://www.twilio.com/blog/2017/08/geospatial-analysis-python-geojson-geopandas.html

https://www.youtube.com/watch?v=BHs_2ttLRXk&list=PLpEPgC7cUJ4b1ARx8PyIQa_sdZRL2GXw5&index=5

https://www.youtube.com/watch?v=JogUFFcfIYg

Install qgis : 
https://www.gis-blog.com/how-to-install-qgis-3-on-ubuntu/

```
sudo gedit /etc/apt/sources.list
```

Add :

```
deb     http://qgis.org/debian raring main
deb-src http://qgis.org/debian raring main
```

Save, then : 

```
gpg --keyserver keyserver.ubuntu.com --recv 47765B75
gpg --export --armor 47765B75 | sudo apt-key add -
sudo apt-get update
```

purge broken packages:

```
sudo apt-get autoremove
sudo apt-get autoclean
sudo apt-get -f install
sudo apt-get autoremove qgis
sudo apt-get --purge remove qgis
```
Grass plugin : 

```
sudo apt-get install grass
sudo apt-get install qgis-plugin-grass
```

qgis:

```
sudo apt-get install qgis python-qgis
```

if it don't work : 

```
sudo apt install qgis
```

# Wednesday 11 Frabruary



# Thursday 12 February 



# Friday 13 February

