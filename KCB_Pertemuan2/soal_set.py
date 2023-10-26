my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print("Menambah Set baru", my_set)

# Tidak, set tidak memungkinkan duplikasi elemen.
# mencoba menambahkan elemen yang sudah ada, elemen tersebut tidak akan ditambahkan kembali ke dalam set.
my_set.add(3)
print("mencoba menambahkan elemen 3 lagi:", my_set)

