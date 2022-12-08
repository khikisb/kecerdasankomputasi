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
    def predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, New_Glucose_Class_Prediabetes, New_BMI_Range_Healty, New_BMI_Range_Overweight, New_BMI_Range_Obese ,New_BloodPressure_HS1, New_BloodPressure_HS2, New_SkinThickness_1):
        
        #Predicting

        if New_Glucose_Class_Prediabetes == 'Iya Tentu':
            New_Glucose_Class_Prediabetes = 1
        elif New_Glucose_Class_Prediabetes == 'Tidak':
            New_Glucose_Class_Prediabetes = 0
            
        if New_BMI_Range_Healty == 'Iya Tentu':
            New_BMI_Range_Healty = 1
        elif New_BMI_Range_Healty == 'Tidak':
            New_BMI_Range_Healty = 0
        
        if New_BMI_Range_Overweight == 'Iya Tentu':
            New_BMI_Range_Overweight = 1
        elif New_BMI_Range_Overweight == 'Tidak':
            New_BMI_Range_Overweight = 0       
        
        if New_BMI_Range_Obese == 'Iya Tentu':
            New_BMI_Range_Obese = 1
        elif New_BMI_Range_Obese == 'Tidak':
            New_BMI_Range_Obese = 0  
            
        if New_BloodPressure_HS1 == 'Iya Tentu':
            New_BloodPressure_HS1 = 1
        elif New_BloodPressure_HS1 == 'Tidak':
            New_BloodPressure_HS1 = 0               
            
        if New_BloodPressure_HS2 == 'Iya Tentu':
            New_BloodPressure_HS2 = 1
        elif New_BloodPressure_HS2 == 'Tidak':
            New_BloodPressure_HS2 = 0    
 
        if New_SkinThickness_1 == 'Iya Tentu':
            New_SkinThickness_1 = 1
        elif New_SkinThickness_1 == 'Tidak':
            New_SkinThickness_1 = 0 
            
        
        prediction = model.predict(pd.DataFrame([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, New_Glucose_Class_Prediabetes, New_BMI_Range_Healty, New_BMI_Range_Overweight, New_BMI_Range_Obese ,New_BloodPressure_HS1, New_BloodPressure_HS2, New_SkinThickness_1]], columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'New_Glucose_Class_Prediabetes', 'New_BMI_Range_Healty', 'New_BMI_Range_Overweight', 'New_BMI_Range_Obese' ,'New_BloodPressure_HS1', 'New_BloodPressure_HS2', 'New_SkinThickness_1']))
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

    New_Glucose_Class_Prediabetes = st.selectbox('New_Glucose_Class_Prediabetes', ['Iya Tentu', 'Tidak'])
    
    New_BMI_Range_Healty = st.selectbox('New_BMI_Range_Healty', ['Iya Tentu', 'Tidak'])
    
    New_BMI_Range_Overweight = st.selectbox('New_BMI_Range_Overweight', ['Iya Tentu', 'Tidak'])
    
    New_BMI_Range_Obese = st.selectbox('New_BMI_Range_Obese', ['Iya Tentu', 'Tidak'])
    
    New_BloodPressure_HS1 = st.selectbox('New_BloodPressure_HS1', ['Iya Tentu', 'Tidak'])
    
    New_BloodPressure_HS2 = st.selectbox('New_BloodPressure_HS2', ['Iya Tentu', 'Tidak'])
    
    New_SkinThickness_1 = st.selectbox('New_SkinThickness_1', ['Iya Tentu', 'Tidak'])
    
    if st.button('Prediksi'):
        prediksi = predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, New_Glucose_Class_Prediabetes, New_BMI_Range_Healty, New_BMI_Range_Overweight, New_BMI_Range_Obese ,New_BloodPressure_HS1, New_BloodPressure_HS2, New_SkinThickness_1)
        st.success(f'Tingkat Kesadaran Pelecehan Seksual Terhadap Anak, yaitu {prediksi}')
