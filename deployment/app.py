import streamlit as st
import eda
import models


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Ananda Karnia Amalya')
    st.write('Batch     : HCK - 027')
    st.write('Tujuan Milestone   : Mengembangkan model machine learning berbasis klasifikasi untuk memprediksi risiko penyakit jantung berdasarkan data karakteristik pasien, termasuk gaya hidup dan kondisi medis.')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Penyakit jantung merupakan salah satu penyebab kematian utama di dunia, termasuk di Indonesia. Menurut Kementerian Kesehatan Republik Indonesia (2023), penyakit jantung iskemik dan stroke menempati posisi teratas dalam penyumbang angka kematian nasional. Kondisi ini menekankan pentingnya deteksi dini sebagai langkah preventif untuk menekan tingkat kematian dan meningkatkan kualitas hidup penderita. Namun, proses diagnosis konvensional terhadap penyakit jantung sering kali membutuhkan waktu yang lama, biaya yang tinggi, dan akses ke fasilitas kesehatan yang memadai. Hal ini menjadi tantangan tersendiri, terutama di wilayah dengan keterbatasan sumber daya kesehatan. Dalam era digital saat ini, teknologi machine learning menawarkan solusi inovatif dalam membantu proses prediksi penyakit secara otomatis dan efisien. Dengan memanfaatkan data kesehatan pasien—seperti gaya hidup, riwayat medis, dan parameter klinis—algoritma klasifikasi dapat digunakan untuk mengidentifikasi risiko penyakit jantung sejak dini. Pendekatan ini berpotensi mempercepat proses skrining, menekan biaya, dan menjangkau lebih banyak individu dalam waktu singkat.')
    with st.expander("Problem Statement"):
            st.caption('Bagaimana memanfaatkan algoritma machine learning untuk memprediksi risiko penyakit jantung secara otomatis dan akurat?')

    with st.expander("Kesimpulan"):
        st.caption('Setelah dilakukan tuning, model menunjukkan peningkatan akurasi dari 85% menjadi 90%. Namun, peningkatan akurasi ini tidak disertai dengan peningkatan kemampuan dalam mengenali kasus penyakit jantung (kelas positif).')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
     models .run()