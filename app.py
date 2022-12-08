import pandas as pd
import pickle
import streamlit as st

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
    
    # NaN values of 0 for Glucose, Blood Pressure, Skin Thickness, Insulin, BMI
    # We can write Nan instead of 0
    cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for col in cols:
        df[col].replace(0,np.NaN,inplace=True)
     
    # now we can see missing values
    st.write("Missing Value")
    st.image("MissingValue.png")
    
    # We can fill in NaN values with a median according to the target
    for col in df.columns:
        df.loc[(df["Outcome"]==0) & (df[col].isnull()),col] = df[df["Outcome"]==0][col].median()
        df.loc[(df["Outcome"]==1) & (df[col].isnull()),col] = df[df["Outcome"]==1][col].median()
    
    df.isnull().sum()
    st.image("missingvalueupdate.png")
    
    def outlier_thresholds(dataframe, variable):
        quartile1 = dataframe[variable].quantile(0.10)
        quartile3 = dataframe[variable].quantile(0.90)
        interquantile_range = quartile3 - quartile1
        up_limit = quartile3 + 1.5 * interquantile_range
        low_limit = quartile1 - 1.5 * interquantile_range
        return low_limit, up_limit
    
    def has_outliers(dataframe, variable):
        low_limit, up_limit = outlier_thresholds(dataframe, variable)
        if dataframe[(dataframe[variable] < low_limit) | (dataframe[variable] > up_limit)].any(axis=None):
            print(variable, "yes")
            
    for col in df.columns:
        has_outliers(df, col)
        
    def replace_with_thresholds(dataframe, numeric_columns):
        for variable in numeric_columns:
            low_limit, up_limit = outlier_thresholds(dataframe, variable)
            dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
            dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit
            
    replace_with_thresholds(df, df.columns)
    
    for col in df.columns:
        has_outliers(df, col)
    
    df.describe([0.05,0.25,0.50,0.75,0.90,0.95,0.99]).T
    
    st.image("describe.png")

    
with tab3:
    st.write("Salahh bro")

with tab4:
    st.write("Salahh bro")
