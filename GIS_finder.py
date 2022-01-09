# -*- coding: utf-8 -*-
import streamlit as st


#Designated Areas for app to be seperated by
header = st.container()#header region holds title, and instructions
buttons = st.container()
footer = st.container()

#Displaying title and then a little information about how to run the app 
with header:
    st.title('Welcome to the Lower Mainland GIS finder!')
    st.text('This project is a quick app to save time when looking for local GIS utility maps')
    st.text('Simply select the city from the dropdown box and then hit the "Click me button"')
    st.text('Then click on the link provided')
    st.text('Cheers - M.V.')
    
#Due to interaction with Streamlit a dictionary is used to hold the values of the URL, to help with UI interaction   
#Dictionary filled with the municipality names along with their URL values    
dict_of_cities = {'Surrey' : 'https://cosmos.surrey.ca/external/',
                  'Vancouver' : 'https://maps.vancouver.ca/vanmap-viewer/',
                  'City of North Vancouver' : 'http://gisext2.cnv.org/citymap/',
                  'New Westminister' : 'http://arcgis.newwestcity.ca/Html5Viewer4122/index.html?viewer=CNWPublicMap',
                  'Burnaby' : 'https://gis.burnaby.ca/burnabymap/index.html',
                  'Abbotsford' : 'https://maps.abbotsford.ca/Html5Viewer/',
                  'Langley Township' : 'https://mapsvr.tol.ca/geosource3/',
                  'Langley City' : 'https://map.langleycity.ca/html5viewer/?viewer=ext',
                  'Delta' : 'https://maps.delta.ca/Html5Viewer/index.html?viewer=DeltaMapExternal.viewer/',
                  'Coquitlam' : 'https://www.arcgis.com/apps/webappviewer/index.html?id=2d58aee859754918ae54d30da4bbba49',
                  'Port Moody' : 'https://view.portmoody.ca/portal/apps/webappviewer/index.html?id=bb8dde24dcef4b06b1e66c4465a3b80c',
                  'Port Coquitlam' : 'https://maps.portcoquitlam.ca/Html5Viewer/index.html?viewer=Public.v1',
                  'West Vancouver' : 'https://westmap.westvancouver.ca/html5Viewer/?viewer=WestMap_2019.Default_Viewer',
                  'Pitt Meadows': 'https://pittmeadows.myplanworx.com/public.aspx?apikey=f50d9903-5f23-4203-bacb-facb31f565f0',
                  'Mission':'Unavailable at the moment',
                  'Maple Ridge':'https://gis.mapleridge.ca/ridgeview/',
                  'District of North Vancouver':'https://geoweb.dnv.org/properties/',
                  'Chilliwack':'https://maps.chilliwack.com/b/',
                  'Central Okanagan':'https://www.rdcogis.com/GIS_App_public/index.html'}

cities_items = dict_of_cities.items()
    
    
List_of_cities = ['Surrey',
                  'Vancouver',
                  'City of North Vancouver',
                  'District of North Vancouver',
                  'New Westminister',
                  'Burnaby',
                  'Abbotsford',
                  'Langley City',
                  'Langley Township',
                  'Delta',
                  'Port Coquitlam',
                  'Port Moody',
                  'Coquitlam',
                  'West Vancouver',
                  'Pitt Meadows',
                  'Mission',
                  'Maple Ridge',
                  'Chilliwack',
                  'Central Okanagan']

with open("count.txt", "r") as f:
    a = f.readline()  # starts as a string
    a = 0 if a == "" else int(a)  # check if its an empty string, otherwise should be able to cast using int()

    
#This selectbox will give all options in List_of_Cities
with buttons:
    selection = st.selectbox('Select City', List_of_cities)    
    
    result = st.button('Click Me')
#Iterating over cities_items assigning the designated city's URL to the variable "selected_city"   
for city , value in cities_items:
    if city == selection:
        selected_city = value    
#Finally the result is displayed in markdown as a clickable link    
if result:
    a += 1  
    with open("file.txt", "w") as f:
        f.truncate()
        f.write(f"{a}")
        
    st.markdown(selected_city,unsafe_allow_html=True)
    

with footer:
    st.text('Any feedback, let me know at mark@quadralocating.com')
    st.text('Thanks for stopping by! Hope it saved you a couple seconds!')
    
    
    
        

