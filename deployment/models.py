import streamlit as st
import pandas as pd
import pickle
from PIL import Image

def run():
    # Load All Files
    with open('best_model.pkl', 'rb') as file:
        full_process = pickle.load(file)

    st.title("Prediksi Penyakit Jantung")
    
    # Form input berdasarkan fitur dalam dataset
    BMI = st.number_input("BMI", min_value=10.0, max_value=60.0, step=0.1)
    Smoking = st.selectbox("Merokok?", ["Yes", "No"])
    AlcoholDrinking = st.selectbox("Konsumsi Alkohol?", ["Yes", "No"])
    Stroke = st.selectbox("Pernah Stroke?", ["Yes", "No"])
    PhysicalHealth = st.slider("Hari dalam sebulan tidak sehat secara fisik", 0, 30)
    MentalHealth = st.slider("Hari dalam sebulan tidak sehat secara mental", 0, 30)
    DiffWalking = st.selectbox("Kesulitan berjalan?", ["Yes", "No"])
    Sex = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    AgeCategory = st.selectbox("Kategori Umur", [
        '18-24', '25-29', '30-34', '35-39', '40-44', '45-49',
        '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older'
    ])
    Race = st.selectbox("Ras", ['White', 'Black', 'Asian', 'American Indian/Alaskan Native', 'Other', 'Hispanic'])
    Diabetic = st.selectbox("Diabetes", ['Yes', 'No', 'No, borderline diabetes', 'Yes (during pregnancy)'])
    PhysicalActivity = st.selectbox("Aktivitas fisik?", ["Yes", "No"])
    GenHealth = st.selectbox("Kesehatan Umum", ['Excellent', 'Very good', 'Good', 'Fair', 'Poor'])
    SleepTime = st.slider("Jam tidur rata-rata per hari", 0, 24)
    Asthma = st.selectbox("Asma?", ["Yes", "No"])
    KidneyDisease = st.selectbox("Penyakit ginjal?", ["Yes", "No"])
    SkinCancer = st.selectbox("Kanker kulit?", ["Yes", "No"])

    # Data frame input
    data_inf = pd.DataFrame({
        'BMI': [BMI],
        'Smoking': [Smoking],
        'AlcoholDrinking': [AlcoholDrinking],
        'Stroke': [Stroke],
        'PhysicalHealth': [PhysicalHealth],
        'MentalHealth': [MentalHealth],
        'DiffWalking': [DiffWalking],
        'Sex': [Sex],
        'AgeCategory': [AgeCategory],
        'Race': [Race],
        'Diabetic': [Diabetic],
        'PhysicalActivity': [PhysicalActivity],
        'GenHealth': [GenHealth],
        'SleepTime': [SleepTime],
        'Asthma': [Asthma],
        'KidneyDisease': [KidneyDisease],
        'SkinCancer': [SkinCancer],
    })

    st.write('Berikut data yang Anda masukkan:')
    st.table(data_inf)

    if st.button(label='Prediksi'):
        y_pred_inf = full_process.predict(data_inf)

        if y_pred_inf[0] == 'Yes':
            st.error("Pasien kemungkinan menderita penyakit jantung.")
            st.markdown("[Cara Hidup Sehat Sehabis Terkena Serangan Jantung](https://lifestyle.kompas.com/read/2021/11/09/101744620/7-pola-hidup-sehat-setelah-mengalami-serangan-jantung)")
        else:
            st.success("Pasien kemungkinan tidak menderita penyakit jantung.")
            st.markdown("[Cara Cegah Serangan Jantung](https://www.siloamhospitals.com/informasi-siloam/artikel/cara-cegah-serangan-jantung-di-usia-muda)")
