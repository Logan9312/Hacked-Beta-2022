import numpy as np
import openrouteservice
import osmnx
import pandas as pd
import streamlit as st
from openrouteservice import convert
import geolocation


def main():
    with open("key.txt") as file:
        client = openrouteservice.Client(key=file.read())
        with st.sidebar:
            map_data = {"lat":[], "lon":[]}
            start = geolocation.get_location(st.text_input("Start Location:"))
            if start is not None:
                map_data["lat"].append(start.latitude)
                map_data["lon"].append(start.longitude)
            end = geolocation.get_location(st.text_input("End Location:"))
            if end is not None:
                map_data["lat"].append(end.latitude)
                map_data["lon"].append(end.longitude)
        df = pd.DataFrame(data=map_data)
        st.map(df)
        # TODO Convert direction data into a dataframe (routes)
        if end is not None and start is not None:
            routes = client.directions(((start.longitude, start.latitude), (end.longitude, end.latitude)), profile='foot-walking')
            time = routes['routes'][0]['summary']['duration']
            print(time)
            minutes, seconds = divmod(time, 60)
            hours, minutes = divmod(minutes, 60)
            st.write(f"Travel Time: {round(hours)}h, {round(minutes)}m, {round(seconds)}s")
        
        
        
        
    


if __name__ == "__main__":
    main()