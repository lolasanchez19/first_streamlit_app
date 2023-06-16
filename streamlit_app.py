import streamlit
streamlit.title ('My parents New Healty List')
streamlit.header ('Breakfast Menu')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Crea tu propio batido de frutas 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv ("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index ('Fruit')
  
#Vamos a hacer una pick list para que puedan elegir la fruta que quieren elegir
streamlit.multiselect ("Pick some fruits:", list(my_fruit_list.index))

#Ponemos la tabla en la pagina
#streamlit.dataframe(my_fruit_list)


#Vamos a crear una lista donde se puede poner la fruta que queremos añadir

fruits_selected = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected] 

#Mostramos la tabla en la pagina
streamlit.dataframe(fruits_to_show)  


#NUEVA SECCION PARA LA APP

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import request

fruityvice_response = request.get( "https://fruityvice.com/api/fruit/+fruit_choice")
streamlit.text(fruityvice_response)
                                                                                          
# SACAMOS EL JSON

# ENSEÑAMOS EL DATAFRAME
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                                                                          

                                                                                          
                                                                                          
                                                                                          
