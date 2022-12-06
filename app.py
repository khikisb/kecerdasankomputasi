import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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
        df_selected_team = pd.read_excel("datadiabetes.xlsx")
        df = df_selected_team.astype(str)
        
        train = df.loc[:, ['Usia']].values 
        
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler(feature_range = (0, 1))
        train_scaled = scaler.fit_transform(train)
        
        X_train = []
        y_train = []
        timesteps = 1

        for i in range(timesteps, 50):
            X_train.append(train_scaled[i - timesteps:i, 0])
            y_train.append(train_scaled[i, 0])
    
        X_train, y_train = np.array(X_train), np.array(y_train)
        
        #Reshaping:
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        
        
        #read csv Data 2
        df_selected_team1 = pd.read_excel(uploaded_file)
        data_baru = df_selected_team1.astype(str)
    
        st.table(data_baru)
        
        st.title("Pre Processing Fitur Usia dengan MinMaxScaler")
             
        # Data 1    
        temp=[]
        for i in df['Usia']:
            temp.append(i)
        
        # Data 2
        temp1 = []
        for j in data_baru['Usia']:
            temp1.append(j)
        
        databaruu = [temp1]
        databaruu2 = [temp]
        # print(databaruu2)

        df1 = pd.DataFrame(databaruu)        
        df2 = pd.DataFrame(databaruu2)
        
        dataset_total = pd.concat((df1, df2), axis=0)
        inputs = dataset_total[len(dataset_total)-len(df2) - timesteps:].values.reshape(-1,1)
        inputs = scaler.transform(inputs) #minmax scaler
        inputs

        st.title("Jumlah Banyaknya Data")
        inputs.shape
        
        X_test = []
        for i in range(timesteps, 51):
            X_test.append(inputs[i-timesteps:i,0])
            X_test = np.array(X_test)
            X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
            predicted_umur = regressor.predict(X_test)
            predicted_umur = scaler.inverse_transform(predicted_umur)
            
         plt.plot(train, color='red', label='Umur Pasien Asli')
         plt.plot(predicted_umur, color='blue', label='Umur Prediksi Pasien')
         plt.title('Prediksi Umur Pasien')
         plt.xlabel('Jumlah Pasien')
         plt.ylabel('Umur Pasien')
         plt.legend()
         plt.show()
