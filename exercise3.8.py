# Daftar tempat yang ingin dikunjungi
places = ["Jepang", "Swiss", "Madinah", "Paris", "Korea Selatan"]

# Menampilkan daftar asli
print("Daftar tempat asli:")
print(places)

# Menampilkan urutan alfabetis tanpa mengubah list asli
print("\nUrutan alfabetis:")
print(sorted(places))

# Menampilkan kembali daftar asli
print("\nDaftar asli:")
print(places)

# Menampilkan urutan alfabetis terbalik
print("\nUrutan alfabetis terbalik:")
print(sorted(places, reverse=True))

# Memastikan daftar asli tidak berubah
print("\nDaftar asli:")
print(places)

# Membalik urutan list
places.reverse()
print("\nSetelah reverse pertama:")
print(places)

# Mengembalikan urutan list
places.reverse()
print("\nSetelah reverse kedua:")
print(places)

# Mengurutkan list secara alfabetis
places.sort()
print("\nSetelah sort alfabetis:")
print(places)

# Mengurutkan list secara alfabetis terbalik
places.sort(reverse=True)
print("\nSetelah sort terbalik:")
print(places)