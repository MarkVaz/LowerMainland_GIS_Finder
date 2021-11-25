# -*- coding: utf-8 -*-
import streamlit as st
import webbrowser

#Designated Areas for app to be seperated by
header = st.container()
buttons = st.container()

#Displaying title and then a little information about how to run the app 
with header:
    st.title('Welcome to the regional GIS finder!')
    st.text('This project is a quick app to save time when looking for local GIS utility maps')
    st.text('Simply select the city from the dropdown box and then hit the "Click me button"')
    st.text('Cheers - M.V.')
    
    
dict_of_cities = {'Surrey' : 'https://cosmos.surrey.ca/external/',
                  'Vancouver' : 'https://maps.vancouver.ca/vanmap-viewer/',
                  'North Vancouver' : 'http://gisext2.cnv.org/citymap/',
                  'New Westminister' : 'http://arcgis.newwestcity.ca/Html5Viewer4122/index.html?viewer=CNWPublicMap',
                  'Burnaby' : 'https://gis.burnaby.ca/burnabymap/index.html',
                  'Abbotsford' : 'https://maps.abbotsford.ca/Html5Viewer/',
                  'Langley Township' : 'https://mapsvr.tol.ca/geosource3/',
                  'Langley City' : 'https://map.langleycity.ca/html5viewer/?viewer=ext',
                  'Delta' : 'https://maps.delta.ca/Html5Viewer/index.html?viewer=DeltaMapExternal.viewer/',
                  'Coquitlam' : 'https://www.arcgis.com/apps/webappviewer/index.html?id=2d58aee859754918ae54d30da4bbba49',
                  'Port Moody' : 'https://view.portmoody.ca/portal/apps/webappviewer/index.html?id=bb8dde24dcef4b06b1e66c4465a3b80c',
                  'Port Coquitlam' : 'https://maps.portcoquitlam.ca/Html5Viewer/index.html?viewer=Public.v1',
                  'West Vancouver' : 'https://westmap.westvancouver.ca/html5Viewer/?viewer=WestMap_2019.Default_Viewer'}

cities_items = dict_of_cities.items()
    
    
List_of_cities = ['Surrey',
                  'Vancouver',
                  'North Vancouver',
                  'New Westminister',
                  'Burnaby',
                  'Abbotsford',
                  'Langley City',
                  'Langley Township',
                  'Delta',
                  'Port Coquitlam',
                  'Port Moody',
                  'Coquitlam',
                  'West Vancouver']

with buttons:
    selection = st.selectbox('Select City', List_of_cities)    
    
    result = st.button('Click Me')
    
for city , value in cities_items:
    if city == selection:
        selected_city = value    
    
if result:
    
    webbrowser.open(selected_city)
    
        

