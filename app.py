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
    
    Pregnancies = st.slider('Pregnancies ?', 0, 17, 25)
    
    Glucose= st.slider('Glucose ?', 0, 199, 25)
    
    BloodPressure = st.slider('BloodPressure ?', 0, 122, 25)
    
    SkinThickness = st.slider('SkinThickness ?', 0, 99, 25)
    
    Insulin = st.slider('Insulin ?', 0, 846, 25)
    
    BMI = st.slider('BMI ?', 0, 67, 25)

    DiabetesPedigreeFunction = st.slider('DiabetesPedigreeFunction ?', 0.78, 2.42)
    
    Age = st.slider('Berapa umur anda ?', 0, 81, 25)
    st.write("I'm ", Age, 'years old')

    if st.button('Prediksi'):
        prediksi = predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        st.success(f'Tingkat Kesadaran Pelecehan Seksual Terhadap Anak, yaitu {prediksi}')
