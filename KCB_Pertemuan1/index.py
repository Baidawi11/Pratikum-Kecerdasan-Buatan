#list
#Kumpulan element yang bisa berubah didefinesikan dengan tanda kurung siki[].
my_list = [1, 2, 3, 4, 5]
fruist = ['apple', 'banana', 'cherry']
mixed_data = [1, 'hello', 3.14, True]

print(my_list)
print(fruist)
print(mixed_data)

#Tuple
#Tuple sama dengan List tetapi tidak bisa diubah. yang didefinesikan dengan tanda kurung bisa()
my_tuple = (1, 2, 3, 4, 5)
coordinates = (3.14, 2,71)

#Set
#Set kumpulan element unik dan tidak berurutan didefinisikan kurung kurawal atau fungsi set()
my_set = {1, 2, 3, 4, 5}
unique_chars = set('hello')

# Membuat tuple yang berisi beberapa nama buah
buah_tuple = ("apel", "mangga", "pisang", "jeruk", "kiwi")

buah_tuple[0] = "apel_merah"  # Ini akan menghasilkan kesalahan TypeError

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

# Membuat tuple yang berisi beberapa nama kota
kota_tuple = ("New York", "Los Angeles", "Chicago", "Houston", "Phoenix")

# Membuat dictionary yang mengaitkan kota dengan jumlah penduduk
penduduk_dict = {
    "New York": 3335837,
    "Los Angeles": 3884307,
    "Chicago": 2716000,
    "Houston": 2320268,
    "Phoenix": 1626078
}

# Menampilkan dictionary
print("Dictionary Jumlah Penduduk:", penduduk_dict)

# Menambahkan kota dan jumlah penduduk baru ke dalam dictionary
penduduk_dict["Philadelphia"] = 1584138
penduduk_dict["San Antonio"] = 1547253

# Menampilkan dictionary setelah penambahan
print("Dictionary setelah penambahan:", penduduk_dict)








#Soal OOP
# Import pustaka yang diperlukan
from abc import ABC, abstractmethod

# Definisikan kelas induk Animal
class Animal(ABC):
    # Properti
    age: int
    gender: str

    # Metode
    @abstractmethod
    def isMammal(self) -> bool:
        pass

    @abstractmethod
    def mate(self) -> None:
        pass

# Definisikan kelas turunan Duck
class Duck(Animal):
    # Properti
    beakColor: str

    # Metode
    def isMammal(self) -> bool:
        return False

    def mate(self) -> None:
        print("Duck sedang kawin")

# Definisikan kelas turunan Fish
class Fish(Animal):
    # Properti
    sizeInFt: int
    canEat: bool

    # Metode
    def isMammal(self) -> bool:
        return False

    def mate(self) -> None:
        print("Fish sedang bertelur")

# Definisikan kelas turunan Zebra
class Zebra(Animal):
    # Properti
    is_wild: bool

    # Metode
    def isMammal(self) -> bool:
        return True

    def mate(self) -> None:
        print("Zebra sedang kawin")

# Buat objek dari masing-masing kelas
duck = Duck(age=10, gender="Betina", beakColor="Kuning")
fish = Fish(age=5, gender="Jantan", sizeInFt=2, canEat=True)
zebra = Zebra(age=15, gender="Betina", is_wild=True)

# Cetak informasi tentang masing-masing objek
print("Duck:", duck.age, duck.gender, duck.beakColor)
print("Fish:", fish.age, fish.gender, fish.sizeInFt, fish.canEat)
print("Zebra:", zebra.age, zebra.gender, zebra.is_wild)
