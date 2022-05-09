from collections import namedtuple
import altair as alt
import math
import streamlit as st
import pandas as pd 
import geopandas as gpd

#Import folium and related plugins
import folium 
from folium import Marker
from folium.plugins import MarkerCluster

#Geopy's Nominatim
from geopy.geocoders import Nominatim

#Scipy's Spatial
from scipy import spatial
#Extra Imports
import requests
from io import StringIO
from io import BytesIO
import json

datapad = geopandas.datasets.get_path("nybb")
data = geopandas.read_file(datapad)
data = data.set_index("BoroName")
data["area"] = data.area
%config IPCompleter.greedy = True
%matplotlib inline

#Alle bestanden inlezen, alleen een .shp bestand is niet genoeg, je hebt alle bestanden nodig.
zipfile = "zip:///Users/bramv/Data Science/Politie/Week 2/Geopandas/WijkBuurtkaart_2021_v1.zip/gemeente_2021_v1.shp"
dataG = geopandas.read_file(zipfile)
dataG.drop(dataG.columns[2:35], axis=1, inplace=True)
dataG = dataG.rename(columns={"Shape_Leng,N,19,11": "Shape_Leng", "Shape_Area,N,19,11": "Shape_Area"})
dataG.set_index("GM_NAAM")
dataG['Shape_Leng'] = dataG.area
dataG.explore("GM_NAAM", legend=False)
st.map(data=dataG)



# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))

    
    
