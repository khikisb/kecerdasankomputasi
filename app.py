import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Prediksi Diabetes",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")


st.title("Prediksi Diabets")

    
tab1, tab2, tab3, tab4 = st.tabs(["Deskripsi Data", "Tab Pre-Processing", "Tab Modeling", "Tab Implementasi"])

with tab1:
    df =pd.read_csv("diabetes.csv")

    st.table(df)

with tab2:
    st.title("Pre-Processing")
    #Observation units for variables with a minimum value of zero are NaN, except for the pregnancy variable.
    df.describe([0.05,0.25,0.50,0.75,0.90,0.95,0.99]).T

    
with tab3:
    st.write("Salahh bro")

with tab4:
    st.write("Salahh bro")
