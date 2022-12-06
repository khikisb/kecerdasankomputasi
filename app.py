import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

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
        
        X_train = []
        y_train = []
        timesteps = 1

        for i in range(timesteps, 50):
            X_train.append(train_scaled[i - timesteps:i, 0])
            y_train.append(train_scaled[i, 0])
    
        X_train, y_train = np.array(X_train), np.array(y_train)
        
        #Reshaping:
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        
        #import libraries and packages:
        from keras.models import Sequential
        from keras.layers import Dense
        from keras.layers import SimpleRNN
        from keras.layers import Dropout
        
        #Initialize RNN:
        regressor = Sequential()
        #Adding the first RNN layer and some Dropout regularization
        regressor.add(SimpleRNN(units = 10, activation='tanh', return_sequences=True, input_shape= (X_train.shape[1],1)))
        regressor.add(Dropout(0.2))

        #Adding the second RNN layer and some Dropout regularization
        regressor.add(SimpleRNN(units = 10, activation='tanh', return_sequences=True))
        regressor.add(Dropout(0.2))

        #Adding the third RNN layer and some Dropout regularization
        regressor.add(SimpleRNN(units = 10, activation='tanh', return_sequences=True))
        regressor.add(Dropout(0.2))

        #Adding the fourth RNN layer and some Dropout regularization
        regressor.add(SimpleRNN(units = 10))
        regressor.add(Dropout(0.2))

        #Adding the output layer
        regressor.add(Dense(units = 1))

        #Compile the RNN
        regressor.compile(optimizer='adam', loss='mean_squared_error')

        #Fitting the RNN to the Training set
        regressor.fit(X_train, y_train, epochs=100, batch_size=32)
        
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
        
        dataset_total = pd.concat((df, df1), axis=0)
        inputs = dataset_total[len(dataset_total)-len(df1) - timesteps:].values.reshape(-1,1)
        inputs = scaler.transform(inputs) #minmax scaler
        inputs

