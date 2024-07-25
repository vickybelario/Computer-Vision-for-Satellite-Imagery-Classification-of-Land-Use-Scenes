# Land-Use-Scene-Classification-using-Computer-Vision

# i. Introduction
- Nama  : Vicky Belario
- Batch : 017 HCK

Graded Challenge 7 ini dilakukan untuk mengimplementasikan konsep Deep Learning terutama Convolutional Neural Network dengan model Computer Vision pada dataset Land use scene

### **Objective**
- Memahami konsep Computer Vision.
- Dapat mempersiapkan data untuk digunakan dalam model Computer Vision.
- Bisa menerapkan Convolutional Neural Network dengan pada dataset Land use scene.
- Sanggup melakukan analisis  dan menjelaskan performansi dari arsitektur Convolutional Neural Network.
- Mampu melakukan Model Deployment.

### **Background**

Land use scene classification adalah tugas penting dalam bidang penginderaan jauh dan geographic information systems (GIS). Dengan perkembangan pesat daerah perkotaan meningkatkan manajemen lahan yang efisien dari gambar satelit menjadi sangat penting. Metode tradisional dalam klasifikasi penggunaan lahan sering melibatkan interpretasi manual, yang memakan waktu dan rentan terhadap kesalahan manusia. Namun, kemajuan dalam deep learning, khususnya Convolutional Neural Networks (CNN), telah menunjukkan kemajuan signifikan dalam mengotomatisasi dan meningkatkan akurasi tugas ini.

### **Goal**

Tujuan dari proyek ini adalah memanfaatkan Computer Vision untuk mengembangkan model dalam klasifikasi scene penggunaan lahan. Dengan demikian, sehingga berkontribusi pada praktik perencanaan perkotaan yang lebih baik dan manajemen lahan yang lebih efektif. implementasi proyek ini dapat membuka jalan bagi inovasi lebih lanjut dalam bidang remote sensing dan environmental monitoring.

### **Dataset Overview**

Dataset ini berisi citra satelit dari 21 kelas seperti bangunan, lapangan bisbol, jalan tol, dll. Dataset citra penggunaan lahan ini dimaksudkan untuk keperluan penelitian. Ukuran asli dari gambar-gambar ini adalah 256x256 piksel. Awalnya ada 100 gambar per kelas. Setelah melakukan augmentasi pada setiap gambar sebanyak 4 kali, ukuran setiap kelas meningkat menjadi 500 gambar. Ini memungkinkan untuk membuat model yang lebih kuat.

Gambar-gambar ini secara manual diekstraksi dari gambar besar koleksi USGS National Map Urban Area Imagery untuk berbagai area perkotaan di seluruh negeri. Resolusi piksel dari citra domain publik ini adalah 1 foot.

