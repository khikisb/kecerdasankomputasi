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


st.title("Prediksi Diabets")

    
tab1, tab2, tab3, tab4 = st.tabs(["Deskripsi Data", "Tab Pre-Processing", "Tab Modeling", "Tab Implementasi"])

with tab1:
    df =pd.read_csv("diabetes.csv")

    st.table(df)

with tab2:
    st.title("Pre-Processing")
    
with tab3:
    st.write("Salahh bro")
    
with tab4:
    st.write("Salahh bro")

    # Define the prediction function
    def predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
        
        #Predicting
        prediction = model.predict(pd.DataFrame([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]], columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']))
        return prediction

with tab4:
    st.header('Jawablah Semua Pertanyaan Berikut :')
    
    Pregnancies = st.slider('Pregnancies ?', 0, 17, 1)
    
    Glucose= st.slider('Glucose ?', 0, 199, 1)
    
    BloodPressure = st.slider('BloodPressure ?', 0, 122, 1)
    
    SkinThickness = st.slider('SkinThickness ?', 0, 99, 1)
    
    Insulin = st.slider('Insulin ?', 0, 846, 1)
    
    BMI = st.slider('BMI ?', 0.000 , 67.10)

    DiabetesPedigreeFunction = st.slider('DiabetesPedigreeFunction ?', 0.078, 2.42)
    
    Age = st.slider('Berapa umur anda ?', 0, 81, 25)

    if st.button('Prediksi'):
        prediksi = predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        st.success(f'Anda Di Prediksi {prediksi}')
        #if prediksi == 0:
            #prediksi1 = "Diabetes"
            #st.success(f'Anda Di Prediksi {prediksi1}')
        #else:
            #prediksi2 = "Tidak Diabetes"
            #st.success(f'Anda Di Prediksi {prediksi2}')
