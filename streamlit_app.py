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

import request

fruityvice_response = request.get( "https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                                                                          
                                                                                          

                                                                                          
                                                                                          
                                                                                          
