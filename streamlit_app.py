import streamlit as st
import pandas as pd

st.title("My Mom's New Healthy Diner!")
st.header("Breakfast Favorites")
st.text("🥣 Omega 3 & Blueberry Oatmeal")
st.text("🥗 Kale, Spinach & Rocket Smoothie")
st.text("🐔 Hard Boiled Free-Range Egg")
st.text("🥑🍞 Avocado Toast")

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list = my_fruits_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index))
st.dataframe(my_fruits_list)
