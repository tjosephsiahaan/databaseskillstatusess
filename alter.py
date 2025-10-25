import sqlite3

# Menghubungkan ke database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Variabel dengan nama tabel
table_name = 'projects'

# Memberi nama kolom baru dan menentukan tipe datanya
new_column_name = 'image'
new_column_type = 'TEXT'

# Melakukan query yang menambahkan kolom baru
alter_query = f"ALTER TABLE {table_name} ADD COLUMN {new_column_name} {new_column_type}"
cursor.execute(alter_query)

# Menyimpan perubahan dan menutup koneksi
conn.commit()
conn.close()