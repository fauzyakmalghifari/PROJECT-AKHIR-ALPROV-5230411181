import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()


id_fauna = 4

#Gunakan query UPDATE SET
kursor.execute(f"UPDATE FAUNA SET asal = 'Kalimantan  Timur' WHERE id_fauna = {id_fauna}")
koneksi.commit()

#cek apakah data berhasil di ubah atau belum
if kursor.rowcount > 0: #cek berdasarkan adanya baris atau tidak
   print(f"Data Dengan ID {id_fauna} Berhasil Diubah!")
else:
   print(f"Tidak Ada data pegawai dengan ID{id_fauna}!")
   
#putuskan kkoneksi
koneksi.close()