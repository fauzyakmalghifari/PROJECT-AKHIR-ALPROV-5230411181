import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Menjalankan query DELETE
cursor.execute(f"DELETE FROM FAUNA WHERE asal = 'Kalimantan'")
conn.commit()

# Menampilkan pesan setelah penghapusan berhasil
if cursor.rowcount > 0:
    print(f"Data fauna dengan asal berhasil dihapus.")
else:
    print(f"Tidak ada data fauna dengan yang anda maksud.")

# Menutup koneksi
conn.close()
