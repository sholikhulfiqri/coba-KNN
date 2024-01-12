import pickle 
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Diabetes')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Age = st.number_input('Input Nilai Age')

with col2 :
    Gender = st.number_input('Input Nilai Gender')

with col1 :
    BMI = st.number_input('Input Nilai BMI')

with col2 :
    SBP = st.number_input('Input Nilai SBP (Systolic Blood Pressure)')

with col1 :
    DBP = st.number_input('Input Nilai DBP (Diastolic Blood Pressure)')

with col2 :
    FPG = st.number_input('Input Nilai FPG (Fasting Plasma Glucose)')
    
with col1 :
    Chol = st.number_input('Input Nilai Cholesterol')

with col2 :
    FFPG = st.number_input('Input Nilai FFPG (Final Fasting Plasma Glucose)')


#code untuk prediksi
diabetes_diagnosis = ''

#membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diabetes_prediction = diabetes_model.predict([[Age, Gender, BMI, SBP, DBP, FPG, Chol, FFPG]])
    
    if(diabetes_prediction[0] == 0):
        diabetes_diagnosis = 'Pasien Tidak Terkena Diabates'
    else:
        diabetes_diagnosis = 'Pasien Terkena Diabetes'        
    
    st.success(diabetes_diagnosis)