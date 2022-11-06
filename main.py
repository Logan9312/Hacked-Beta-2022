import numpy as np
import pandas as pd
import streamlit as st
import geolocation


def main():
    with st.sidebar:
        map_data = {"lat":[], "lon":[]}
        start = geolocation.get_location(st.text_input("Location 1:"))
        if start is not None:
            map_data["lat"].append(start.latitude)
            map_data["lon"].append(start.longitude)
        end = geolocation.get_location(st.text_input("Location 2:"))
        if end is not None:
            map_data["lat"].append(end.latitude)
            map_data["lon"].append(end.longitude)

        df = pd.DataFrame(data=map_data)

    st.map(df)
    


if __name__ == "__main__":
    main()