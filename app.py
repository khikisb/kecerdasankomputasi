import pandas as pd
import pickle
import streamlit as st


# load the model from disk
model = pickle.load(open('finalized_model.sav', 'rb'))

st.set_page_config(
    page_title="Prediksi Diabetes",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")


st.title("Prediksi Diabetes")

    
tab1, tab2 = st.tabs(["Deskripsi Data", "Tab Implementasi"])

with tab1:
    df =pd.read_csv("diabetes.csv")

    st.table(df)

    # Define the prediction function
    def predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
        
        #Predicting
        prediction = model.predict(pd.DataFrame([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]], columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']))
        
        if prediction == 1:
            prediction = "Diabetes"
        elif prediction == 0:
            prediction = "Tidak Diabetes"
            
        return prediction

with tab2:
    st.header('Jawablah Semua Pertanyaan Berikut :')
    
    Pregnancies = st.slider('Masukkan jumlah kehamilan anda ? (Pregnancies) ', 0, 17, 6)
    
    Glucose= st.slider('Berapa tingkat Glukosa dalam darah anda ? (Glucose)', 0, 199, 148)
    
    BloodPressure = st.slider('Berapa tekanan darah anda ? (BloodPressure)', 0, 122, 72)
    
    SkinThickness = st.slider('Berapa ketebalan kulit anda ? (SkinThickness) ', 0, 99, 35)
    
    Insulin = st.slider('Berapa tingkat insulin pada darah anda ? (Insulin)', 0, 846, 0)
    
    BMI = st.slider('Masukkan indeks tubuh anda ? (BMI)', 0.000 , 33.07)

    DiabetesPedigreeFunction = st.slider('Berapa presentase diabetes anda ? (DiabetesPedigreeFunction)', 0.078, 0.62)
    
    Age = st.slider('Berapa umur anda ? (Age)', 0, 81, 50)

    if st.button('Prediksi'):
        prediksi = predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        st.success(f'Anda Di Prediksi {prediksi}')
        

