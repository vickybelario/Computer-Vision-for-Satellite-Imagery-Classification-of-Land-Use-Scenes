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
pengambilan data melalui website kaggle : [Link](https://www.kaggle.com/datasets/apollo2506/landuse-scene-classification/data)
Dataset ini berisi citra satelit dari 21 kelas seperti bangunan, lapangan bisbol, jalan tol, dll. Dataset citra penggunaan lahan ini dimaksudkan untuk keperluan penelitian. Ukuran asli dari gambar-gambar ini adalah 256x256 piksel. Awalnya ada 100 gambar per kelas. Setelah melakukan augmentasi pada setiap gambar sebanyak 4 kali, ukuran setiap kelas meningkat menjadi 500 gambar. Ini memungkinkan untuk membuat model yang lebih kuat.

Gambar-gambar ini secara manual diekstraksi dari gambar besar koleksi USGS National Map Urban Area Imagery untuk berbagai area perkotaan di seluruh negeri. Resolusi piksel dari citra domain publik ini adalah 1 foot.

transfer learning pada website keras berikut : [Link](https://keras.io/api/applications/densenet/#densenet201-function)
deployment proyek model pada website huggingface : [Link](https://huggingface.co/spaces/vickybelario/Graded_Challenge_7)

## Kesimpulan

**Model CNN Training**<br>

Precision, Recall, F1-Score, Accuracy:
Hasil precision, recall, dan f1-score dari model CNN training menunjukkan bahwa model ini gagal memprediksi hampir semua kelas dengan benar. Hanya kelas 'airplane' yang dapat diprediksi dengan tepat.

Kelemahan:
Loss pada data training secara konsisten lebih tinggi daripada loss pada data validasi (val_loss), mengindikasikan model sedang mengalami underfitting. Underfitting terjadi ketika model terlalu sederhana untuk menangkap pola yang mendasari pada data training.

Kelebihan:<br>
Tidak ada kelebihan yang signifikan dari model ini.

Room for Improvement:
- Mengoptimalkan hyperparameter seperti learning rate, scheduler, callback.

**Model CNN Improve**<br>

Precision, Recall, F1-Score, Accuracy:
Model CNN improve juga menunjukkan hasil yang buruk, hanya mampu memprediksi kelas 'tenniscourt' dengan benar.

Kelemahan:
- Meskipun ada sedikit perbaikan, model ini masih menunjukkan performa yang sangat buruk dengan akurasi yang sama (5%).
- Overfitting bisa jadi masalah jika model hanya belajar dari data latih tanpa generalisasi yang baik.

Kelebihan:<br>
- Loss training dan loss validasi terus menurun dan akhirnya menyentuh nilai yang hampir sama, ini menunjukkan bahwa model belajar dengan baik dan menggeneralisasi dengan baik ke data yang tidak terlihat.
- Tidak Ada Overfitting atau Underfitting: Karena loss training dan loss validasi konsisten menurun dan hampir sama di akhir, ini menunjukkan bahwa model tidak mengalami overfitting atau underfitting.

Room for Improvement:
- Menambahkan lebih banyak lapisan atau mencoba arsitektur yang lebih kompleks.

**Model Transfer Learning**<br>

Precision, Recall, F1-Score, Accuracy:
Hasil precision, recall, dan f1-score menunjukkan performa yang sangat baik dengan akurasi mencapai 97%.

Kelemahan:
- Memerlukan lebih banyak sumber daya komputasi dan waktu untuk pelatihan.
- Keterbatasan dalam fleksibilitas arsitektur karena bergantung pada model pre-trained.

Kelebihan:
- Akurasi yang sangat tinggi dan performa yang jauh lebih baik dibandingkan dua model sebelumnya.
- Kemampuan untuk menangkap fitur yang lebih kompleks dari data latih.

Room for Improvement:<br>
Menggunakan lebih banyak data latih atau data augmentation untuk meningkatkan generalisasi.

## kesimpulan keseluruhan
- Model CNN Training dan Model CNN Improve menunjukkan performa yang kurang memuaskan, dengan akurasi dan kemampuan prediksi yang sangat rendah.
- Model Transfer Learning menunjukkan hasil yang sangat baik, dengan akurasi yang tinggi dan kemampuan prediksi yang solid di semua kelas.