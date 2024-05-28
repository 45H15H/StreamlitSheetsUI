import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title = "Useful Phrases", 
    layout = "wide", 
    initial_sidebar_state = "auto", 
    menu_items = None,
    page_icon="🔖"
)

connection = st.connection("gsheets", type = GSheetsConnection)

from datetime import datetime
today = datetime.today().strftime("%m/%d/%Y")


data = connection.read(worksheet = "Sheet5", usecols = [0, 1, 2, 3, 4])
# data = pd.read_csv("Useful-Phrases-Sheet2.csv")

with st.form(key="update"):
    st.markdown("""
        Phrase :red[*]
        """)
    phrase = st.text_input("Phrase", placeholder="Enter the phrase", label_visibility="collapsed", key = "phrase")
    st.markdown("""
        Meaning :red[*]
        """)
    meaning = st.text_input("Meaning", placeholder="Enter its meaning", label_visibility="collapsed", key = "meaning")
    st.markdown("""
        Example :red[*]
        """)
    example = st.text_input("Example", placeholder="Enter an example", label_visibility="collapsed", key = "example")

    if st.form_submit_button("Update", use_container_width=True, type="primary"):
        if phrase == "" or meaning == "" or example == "":
            st.warning("Please fill all the fields marked with [*]")
        else:
            st.success("Data updated successfully!")
            # Get the length of the data that contains values
            length = len(data['Phrase'].loc[data['Phrase'].notna() & (data['Phrase'] != '')])
            
            data = data.iloc[:length]
            
            data = data.append(
                {   
                    "S. No.": length + 1,
                    "Date": today,
                    "Phrase": phrase,
                    "Meaning": meaning,
                    "Example": example
                }
                ,
                ignore_index=True
            )
    
            connection.update(
                worksheet="Sheet5",
                data=data,
            )
        
        # in the end clear the input fields
        st.experimental_rerun()

length = len(data['Phrase'].loc[data['Phrase'].notna() & (data['Phrase'] != '')])

st.dataframe(data.iloc[:length], width=1200, height=200, hide_index=True)