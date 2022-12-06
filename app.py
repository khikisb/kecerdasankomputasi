import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Prediksi Jumlah Pasien Diabetes",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")


st.title("Prediksi Jumlah Pasien Diabetes Di RSUD Syarifah Ambami Ratu Ebu")

    
tab1, tab2, tab3, tab4 = st.tabs(["Deskripsi Data", "Tab Pre-Processing", "Tab Modeling", "Tab Implementasi"])

with tab1:
    df_selected_team = pd.read_excel("datadiabetes.xlsx")
    df = df_selected_team.astype(str)

    st.table(df)

with tab2:
    st.title("Seleksi Fitur Usia Dari Data")
    train = df.loc[:, ['Usia']].values 
    train
    
    st.title("Pre Processing Fitur Usia dengan MinMaxScaler")
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range = (0, 1))
    train_scaled = scaler.fit_transform(train)
    train_scaled
    
    st.title("Grafik dari MinMaxScaler Fitur Usia")
    fig, ax = plt.subplots()
    # ...
    st.pyplot(fig)
    
with tab3:
   st.image("firza.png")

with tab4:
   st.image("firza.png")
