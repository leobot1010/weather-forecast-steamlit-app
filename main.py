import streamlit as st
import plotly.express as px
from backend import get_user_data

# HEADER
st.header("Weather Forecast for the Next 5 Days")

# GET USER CHOICES
place = st.text_input('Place')
days = st.slider('Forecast', min_value=1, max_value=5, step=1,
                 help='Select the number of forecasted days')
temp_or_sky = st.selectbox("Select data to view", ("Temperature", "Sky"))

# SUB-HEADER

# SEND USER CHOICES TO FUNCTION, RETRIEVE BACK THE DATA
# we use 'if place block' to prevent error, since place box is empty on page load

if place:
    try:
        filtered_data = get_user_data(place, days)

        st.subheader(f"{temp_or_sky} for the next {days} days in {place}")

        if temp_or_sky == 'Temperature':
            # CREATE A TEMPERATURE PLOT
            temperatures = [i['main']['temp'] / 10 for i in filtered_data]
            # print(temperatures)
            dates = [i["dt_txt"] for i in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if temp_or_sky == 'Sky':
            # CREATE SKY IMAGES
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky = [i['weather'][0]['main'] for i in filtered_data]

            image_paths = [images[i] for i in sky]

            st.image(image_paths, width=115)
    except KeyError:
        st.write("")
        st.text(f"{place} does not exist in the  data")

# filtered_data = get_user_data("zxzx", 3)
# print(filtered_data)
