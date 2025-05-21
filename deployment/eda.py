# eda.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    st.title("🧠 Exploratory Data Analysis")
    st.caption("Dataset: heart_2020_cleaned.csv")

    # Load data
    df = pd.read_csv('heart_2020_cleaned.csv')  # asumsi file ada di folder yang sama
#nomer 1
    st.subheader("📌 Pertanyaan 1")
    st.markdown("### 1. Analisis jumlah orang dengan dan tanpa penyakit jantung")

    # Visualisasi
    fig, ax = plt.subplots()
    sns.countplot(x='HeartDisease', data=df, ax=ax)
    ax.set_title("Distribusi HeartDisease")
    st.pyplot(fig)

    # Insight
    st.markdown("**Insight:**")
    st.info("Terdapat jauh lebih banyak yang tidak memiliki penyakit jantung pada data ini.")
    st.markdown("")

#nomer 2
    st.subheader("📌 Pertanyaan 2")
    st.markdown("### 2. Mengetahui proporsi persepsi kesehatan secara umum (Excellent, Good, Fair, dll.).")

    # Visualisasi
    fig, ax = plt.subplots()
    sns.countplot(x='HeartDisease', data=df, ax=ax)
    ax.set_title("Distribusi HeartDisease")
    st.pyplot(fig)
    plt.figure(figsize=(6, 6))
    df['GenHealth'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.ylabel('')
    plt.title("Distribusi GenHealth")
    plt.show()

    # Insight
    st.markdown("**Insight:**")
    st.info("Dilakukan Pengecekan persepsi kesehatan menggunakan piechart agar mempermudah melihat persentase persepsi dari GenHealth itu sendiri.")

#nomer 3
    st.subheader("📌 Pertanyaan 3")
    st.markdown("### 3. Korelasi antar variabel numerik (BMI, PhysicalHealth, MentalHealth, SleepTime).")

    # Visualisasi
# Pilih hanya kolom yang diinginkan
    st.title("Exploratory Data Analysis (EDA)")

    st.subheader("Korelasi: BMI, Physical Health, Mental Health, dan Sleep Time")

    # Hitung korelasi
    corr = df[['BMI', 'PhysicalHealth', 'MentalHealth', 'SleepTime']].corr()

    # Buat plot
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Korelasi: BMI, Physical Health, Mental Health, dan Sleep Time')

    # Tampilkan plot di Streamlit
    st.pyplot(fig)

    # Insight
    st.markdown("**Insight:**")
    st.info("Digunakan matriks hanya untuk numerik, karena kategorik tidak dapat di gunakan matrix correlation. BMI paling berkorelasi dengan PhysicalHealth namun sangat sedikit korelasinya. MentalHealth paling berkorelasi dengan PhysicalHealth namun sangat sedikit korelasinya. Sleeptime yang paling berkorelasi adalah MentalHealth namun sangat sedikit korelasinya.")


#nomer 4
    st.subheader("📌 Pertanyaan 4")
    st.markdown("### 4. Analisis Fitur Kategorikal terhadap HeartDisease")

    # Visualisasi

    # Plot boxplot menggunakan matplotlib dan seaborn
    fig, ax = plt.subplots()
    sns.boxplot(x='HeartDisease', y='BMI', data=df, ax=ax)
    ax.set_title('Perbandingan BMI berdasarkan HeartDisease')

    # Tampilkan plot di Streamlit
    st.pyplot(fig)

    # Insight
    st.markdown("**Insight:**")
    st.info("BMI yang lebih tinggi cenderung berhubungan dengan adanya penyakit jantung, meskipun perbedaannya tidak terlalu besar secara visual. Durasi tidur tampaknya tidak menjadi pembeda utama antara kelompok yang memiliki penyakit jantung dan yang tidak.")

#nomer 5
    st.subheader("📌 Pertanyaan 5")
    st.markdown("### 5.  Analisis AgeCategory dan GenHealth terhadap HeartDisease")

    # Visualisasi
    plt.figure(figsize=(14, 5))

    # Distribusi HeartDisease per AgeCategory

    # Buat figure dan axis
    fig, ax = plt.subplots(figsize=(10, 5))

    # Buat countplot
    sns.countplot(
        x='AgeCategory',
        hue='HeartDisease',
        data=df,
        order=sorted(df['AgeCategory'].unique()),
        ax=ax
    )

    # Set judul dan rotasi label
    ax.set_title('Distribusi Heart Disease per Age Category')
    ax.set_xlabel('Age Category')
    ax.set_ylabel('Jumlah')
    plt.xticks(rotation=45)

        # Tampilkan plot di Streamlit
    st.pyplot(fig)

    # Insight
    st.markdown("**Insight:**")
    st.info("Terlihat bahwa semakin tua umur dari seseorang semakin besar juga potensi dia terkena penyakit jantung.")


#nomer 6
    st.subheader("📌 Pertanyaan 6")
    st.markdown("### 6. Analisis hubungan merokok berdasarkan HeartDisease.")


    # Buat figure dan axis
    fig, ax = plt.subplots(figsize=(6, 4))

    # Buat countplot
    sns.countplot(data=df, x='Smoking', hue='HeartDisease', ax=ax)

    # Set judul
    ax.set_title("Smoking vs Heart Disease")

    # Tampilkan plot di Streamlit
    st.pyplot(fig)


    # Insight
    st.markdown("**Insight:**")
    st.info("Merokok tampaknya menjadi faktor risiko signifikan terhadap penyakit jantung. Meskipun jumlah perokok mungkin lebih sedikit daripada non-perokok, proporsi penderita penyakit jantung di antara perokok lebih tinggi.")

#nomer 7
    st.subheader("📌 Pertanyaan 7")
    st.markdown("### 7. Distribusi SleepTime yang dibedakan berdasarkan status HeartDisease")

    # Visualisasi

    # Buat figure dan axis
    fig, ax = plt.subplots(figsize=(6, 4))

    # Plot histogram
    sns.histplot(
        data=df,
        x='SleepTime',
        bins=24,
        kde=True,
        hue='HeartDisease',
        multiple='stack',
        ax=ax
    )

    # Tambahkan judul dan label
    ax.set_title("Distribusi SleepTime berdasarkan HeartDisease")
    ax.set_xlabel("SleepTime (jam)")
    ax.set_ylabel("Jumlah")

    # Tambahkan legend manual (opsional)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles, labels=['Tidak', 'Ya'], title='HeartDisease')

    # Tampilkan di Streamlit
    st.pyplot(fig)

    # Insight
    st.markdown("**Insight:**")
    st.info("Tidur dengan durasi 6–8 jam tampaknya merupakan pola tidur yang paling umum, terutama pada orang tanpa penyakit jantung. Sementara itu, penderita penyakit jantung memiliki pola tidur yang lebih menyebar, dengan indikasi jumlah yang lebih tinggi pada waktu tidur yang kurang dari ideal. Hal ini mengindikasikan bahwa durasi tidur yang tidak optimal bisa berhubungan dengan risiko penyakit jantung.")

