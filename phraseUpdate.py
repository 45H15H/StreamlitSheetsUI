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


data = connection.read(worksheet = "Sheet5", usecols = [0, 1, 2, 3, 4], ttl=0)
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
            # Read latest sheet data at submit time to avoid cache-based overwrite.
            latest_data = connection.read(worksheet="Sheet5", usecols=[0, 1, 2, 3, 4], ttl=0)

            # if phrase already exists, then don't allow
            if phrase in latest_data['Phrase'].values:
                st.error("Phrase already exists!")
            else:
                # Keep only rows where Phrase exists, then append a new row.
                valid_rows = latest_data['Phrase'].notna() & (latest_data['Phrase'] != '')
                latest_data = latest_data.loc[valid_rows].copy()
                length = len(latest_data)

                new_row = pd.DataFrame([
                    {
                        "S. No.": length + 1,
                        "Date": today,
                        "Phrase": phrase,
                        "Meaning": meaning,
                        "Example": example,
                    }
                ])

                data = pd.concat([latest_data, new_row], ignore_index=True)

                connection.update(
                    worksheet="Sheet5",
                    data=data,
                )
                st.success("Data updated successfully!")
        
        

length = len(data['Phrase'].loc[data['Phrase'].notna() & (data['Phrase'] != '')])

st.dataframe(data.iloc[:length], width=1200, height=200, hide_index=True)
