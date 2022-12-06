import pandas as pd
import pickle
import streamlit as st

st.set_page_config(
    page_title="Prediksi Jumlah Pasien Diabetes",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")


st.title("Prediksi Jumlah Pasien Diabetes Di RSUD Syarifah Ambami Ratu Ebu")

    
tab1, tab2, tab3, tab4 = st.tabs(["Deskripsi Data", "Tab Pre-Processing", "Tab Modeling", "Tab Implementasi"])

with tab1:
    uploaded_file = st.file_uploader("datadiabetes.xlsx", type="xlsx")

    if uploaded_file:
        df = pd.read_excel(uploaded_file)

        st.dataframe(df)
        st.table(df)

with tab2:
   st.image("farid.png")
    
with tab3:
   st.image("firza.png")

with tab4:
   st.image("firza.png")
