import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

#mengambil semua data dalam tabel dan tampilkan
kursor.execute("SELECT *FROM FAUNA ORDER BY jml_skrng DESC ")

#Tampilkan dalam bentuk
baris_tabel = kursor.fetchall()

print("Data Fauna")
print("=" *100)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}". format("ID Fauna", "Nama Fauna", "Jenis", "Asal", "Jumlah Saat ini", "Tahun Terakhir Ditemukan"))
print("-"*100)

#Tampilkan data sesuai format tabel dengan perluagan
for baris in baris_tabel:
   print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}". format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
   
koneksi.close()