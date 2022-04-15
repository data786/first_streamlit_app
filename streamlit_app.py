import streamlit

streamlit.title("My Mom\'s New Healthy Diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# change index
my_fruit_list = my_fruit_list.set_index('Fruit')

# pick list for fruits
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display table of fruits
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruit_choice = streamlit.text_input("What fruit would you like information about?", "Kiwi")
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) # just writes data to the screen

# take json response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fuit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
