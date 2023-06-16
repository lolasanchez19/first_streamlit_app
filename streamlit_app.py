import streamlit
import pandas
import request
import snowflake.connector
from urllib.error import URLError


streamlit.title ('My parents New Healty List')
streamlit.header ('Breakfast Menu')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Crea tu propio batido de frutas 🥝🍇')


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



fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
  streamlit.error("Please select a fruit to get information.")
  else 
  fruityvice_response = request.get( "https://fruityvice.com/api/fruit/+fruit_choice" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  streamlit.text(fruityvice_response)

except URLERROR as e:
streamlit.error()
                                                                                          
# SACAMOS EL JSON

# ENSEÑAMOS EL DATAFRAME
streamlit.dataframe(fruityvice_normalized)



streamlit.stop()



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains: ")
streamlit.dataframe(my_data_row)



my_cur.execute("insert into fruit_load_list values ('from streamlit')")
                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                                                                          

                                                                                          
                                                                                          
                                                                                          
