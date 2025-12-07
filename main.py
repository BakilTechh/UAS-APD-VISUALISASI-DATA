import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

chess_data = pd.read_csv("D:/UAS-APD/chess_games.csv")


#============================================================
# VISUALISASI DATA PERTAMA (HEATMAP KORELASI)

# # Ganti nama kolom ke Bahasa Indonesia hanya untuk tampilan grafik
# translated_cols = {
#     'rated': 'Permainan Rated',
#     'turns': 'Jumlah Giliran',
#     'white_rating': 'Rating Putih',
#     'black_rating': 'Rating Hitam'
# }

# # Ambil kolom numerik
# num_cols = list(translated_cols.keys())
# chess_data_num = chess_data[num_cols]

# # Hitung matriks korelasi
# corr_matrix = chess_data_num.corr()

# # Ubah nama indeks & kolom pada matriks untuk Bahasa Indonesia
# corr_matrix.index = [translated_cols[col] for col in corr_matrix.index]
# corr_matrix.columns = [translated_cols[col] for col in corr_matrix.columns]

# # Buat heatmap korelasi
# fig, ax = plt.subplots(figsize=(10, 8))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)

# # Judul grafik
# plt.title('Matriks Korelasi Fitur Permainan Catur')
# plt.tight_layout()
# plt.show()

#============================================================
# VISUALISASI DATA KEDUA (COUNTPLOT HASIL PERMAINAN)

# # cek nilai unik awal (opsional, untuk debugging)
# print("Unique sebelum replace:", chess_data['winner'].unique())

# # Standarisasi nama kategori dan perbaiki kemungkinan typo
# chess_data['winner'] = chess_data['winner'].replace({
#     'White': 'Putih Menang',
#     'Black': 'Hitam Menang',
#     'Draw': 'Seri',
#     'putih': 'Putih Menang',
#     'hitam menang': 'Hitam Menang',
#     'seri': 'Seri',
#     'Putin': 'Putih Menang',   # contoh apabila ada typo 'Putin'
#     'Putin Menang': 'Putih Menang'
# })

# # cek lagi setelah replace (pastikan sudah berubah)
# print("Unique setelah replace:", chess_data['winner'].unique())

# # Buat countplot tanpa menampilkan label 'winner' di bawah
# plt.figure(figsize=(8,6))
# ax = sns.countplot(x='winner', data=chess_data,
#                    palette={'Putih Menang': 'blue', 'Hitam Menang': 'red', 'Seri': 'green'},
#                    order=['Putih Menang','Hitam Menang','Seri'])

# # Hilangkan label sumbu-x (yang tertulis 'winner')
# ax.set_xlabel('')          # kosongkan label sumbu-x
# ax.set_ylabel('Jumlah Pertandingan')
# ax.set_title('Distribusi Hasil Pertandingan Catur')

# # Opsional: buat tick label lebih rapi (kapitalisasi dan jarak)
# plt.xticks(rotation=0)     # ubah rotasi jika perlu
# plt.tight_layout()
# plt.show()

# ============================================================
# VISUALISASI DATA KETIGA (DISTRIBUSI JUMLAH LANGKAH PERMAINAN)

# sns.histplot(chess_data['turns'], kde=False, color='purple')
# plt.xlabel('Jumlah Langkah Permainan')
# plt.ylabel('Jumlah Pertandingan')
# plt.title('Distribusi Banyaknya Langkah dalam Pertandingan')
# plt.show()

# ============================================================
# VISUALISASI DATA KEEMPAT (SCATTER PLOT JUMLAH LANGKAH VS STATUS KEMENANGAN)

# chess_data['winner'] = chess_data['winner'].replace({
#     'White': 'Putih Menang',
#     'Black': 'Hitam Menang',
#     'Draw': 'Seri'
# })

# sns.scatterplot(
#     x='turns',
#     y='victory_status',
#     hue='winner',
#     data=chess_data,
#     palette={
#         'Putih Menang': 'blue',
#         'Hitam Menang': 'red',
#         'Seri': 'green'
#     }
# )
# plt.title('Hubungan Jumlah Langkah dan Status Kemenangan')
# plt.xlabel('Jumlah Langkah (turns)')
# plt.ylabel('Status Kemenangan')
# plt.show()



