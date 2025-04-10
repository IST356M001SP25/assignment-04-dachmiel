'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py

file = st.file_uploader("Upload a file", type=["csv", "xlsx", "json"])
if file is not None:
    ext = pl.get_file_extension(file.name)
    df = pl.load_file(file, ext)
    
    # Display column names
    column_names = pl.get_column_names(df)

    # Select columbs to display
    st.subheader("Select Columns to Display")
    selected_columns = st.multiselect("Select columns", column_names, default=column_names)
    
    if st.toggle("Filter Data"):
        st.subheader("Filter Data")
        filter_column = st.selectbox("Select column to filter", column_names)
        if filter_column:
            unique_values = pl.get_unique_values(df, filter_column)
            selected_value = st.selectbox("Select value to filter on", unique_values)
            filtered_df = df[df[filter_column] == selected_value]
            st.dataframe(filtered_df[selected_columns])
        else:
            st.write("No column selected for filtering.")
    else:
        st.write("Filtering is disabled.")
    # Display dataframe
    st.subheader("Dataframe")
    st.dataframe(df[selected_columns])
    # Display description
    st.subheader("Description")
    st.dataframe(df.describe())
else:
    st.write("Please upload a file.")