import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Prediksi Jumlah Pasien",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")


st.title("Prediksi Jumlah Pasien Penyakit Dalam Di RSUD Syarifah Ambami Ratu Ebu")

    
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
    ax.hist(train_scaled, bins=50)
    st.pyplot(fig)

    
with tab3:
   st.image("firza.png")

with tab4:
    uploaded_file = st.file_uploader("Masukkan Data Pasien")
    if uploaded_file is not None:
        #read csv
        df_selected_team1 = pd.read_excel(uploaded_file)
        df1 = df_selected_team1.astype(str)
    
        st.table(df1)
        
        st.title("Pre Processing Fitur Usia ddengan MinMaxScaler")
        databaruu = [df1]

        temp=[]
        for h in df['Usia']:
            temp.append(h)
        
        temp1=[]
        for i in df1['Usia']:
            temp.append(i)
    
        databaru2 = [temp,temp1]
        databaru2

