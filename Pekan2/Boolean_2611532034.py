# Buat file dengan nama Boolean_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_2034 = True
is_cumlaude_2034 = True

# Menggunakan Boolean
nilai_2034 = 85
batas_lulus_2034 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_2034 = nilai_2034 >= batas_lulus_2034 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_2034)
print("Apakah Lulus?:", status_kelulusan_2034)
if is_lulus_2034 and is_cumlaude_2034:
    print("Selamat Anda lulus dengan predikat cumlaude!")