import streamlit as st

st.header("Weather Forecast for the Next 5 Days")

place = st.text_input('Place')

days = st.slider('Forecast', min_value=1, max_value=5, step=1,
                 help='Select the number of forecasted days')

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")