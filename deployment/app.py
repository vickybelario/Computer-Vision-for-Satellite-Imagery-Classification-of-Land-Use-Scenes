import streamlit as st
import pandas as pd
import numpy as np
import eda
import prediction


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediction'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Graded Challenge 7')
    st.write('Nama      : Vicky Belario')
    st.write('Batch     : 017')
    st.write('Tujuan    : Graded Challenge 7 ini dilakukan untuk mengimplementasikan konsep Deep Learning terutama Convolutional Neural Network dengan model Computer Vision pada dataset Land use scene')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Di era digital saat ini, laptop telah menjadi alat yang tak tergantikan bagi konsumen di seluruh dunia, digunakan untuk pekerjaan, pendidikan, dan hiburan.  Dengan teknologi yang berkembang pesat, beragam model dan fitur laptop tersedia dengan banyak pilihan. konsumen dihadapkan pada berbagai pilihan laptop yang sangat beragam. proses pengambilan keputusan pembelian menjadi rumit ketika konsumen memilih laptop yang sesuai dengan kebutuhan mereka maupun sesuai dengan anggaran yang ada atau spesifikasi yang diinginkan, karena harga laptop dapat bervariasi berdasarkan spesifikasi, merek, dan tren pasar.')

    with st.expander("Goal"):
        st.caption('Tujuan utama dari proyek ini adalah mengembangkan model regresi multilinear untuk memprediksi harga laptop berdasarkan fitur-fitur laptop seperti kecepatan prosesor dan kapasitas penyimpanan. Dengan mencapai tujuan ini, konsumen dapat mendapatkan perkiraan harga laptop yang informatif, sehingga membantu mereka membuat keputusan saat membeli laptop ')

    with st.expander("Kesimpulan"):
        st.caption('lorem ipsum')
    st.write('')
elif page == 'Exploration Data Analysis':
    eda.run()
elif page == 'Model Prediction':
    prediction.run()
else:
    st.write('') 
