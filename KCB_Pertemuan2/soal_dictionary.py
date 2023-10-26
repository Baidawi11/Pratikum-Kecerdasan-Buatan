# Membuat dictionary tentang buku
buku = {
    "judul": "Harry Potter and the Sorcerer's Stone",
    "penulis": "J.K. Rowling",
    "tahun_terbit": 1997
}

# Mengakses nilai berdasarkan kunci
judul_buku = buku["judul"]
penulis_buku = buku["penulis"]
tahun_terbit_buku = buku["tahun_terbit"]

# Menampilkan informasi buku
print("Judul Buku:", judul_buku)
print("Penulis Buku:", penulis_buku)
print("Tahun Terbit Buku:", tahun_terbit_buku)

# Mengganti nilai dengan kunci yang sudah ada
buku["judul"] = "Harry Potter and the Chamber of Secrets"

# Sekarang, dictionary memiliki nilai yang telah diganti
print("Judul Buku (setelah perubahan):", buku["judul"])
