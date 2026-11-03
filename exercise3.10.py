# Membuat list kendaraan
vehicles = ["Honda", "Toyota", "Yamaha", "Mitsubishi"]

# Menampilkan list
print("Daftar kendaraan:")
print(vehicles)

# Mengakses elemen list
print("\nKendaraan pertama:")
print(vehicles[0])

# Mengubah elemen list
vehicles[0] = "Suzuki"
print("\nSetelah mengubah elemen:")
print(vehicles)

# Menambahkan elemen menggunakan append()
vehicles.append("Kawasaki")
print("\nSetelah append():")
print(vehicles)

# Menambahkan elemen menggunakan insert()
vehicles.insert(1, "Daihatsu")
print("\nSetelah insert():")
print(vehicles)

# Menghapus elemen menggunakan del
del vehicles[1]
print("\nSetelah del:")
print(vehicles)

# Menghapus elemen menggunakan pop()
popped_vehicle = vehicles.pop()
print("\nKendaraan yang dihapus dengan pop():")
print(popped_vehicle)

# Menghapus elemen menggunakan remove()
vehicles.remove("Toyota")
print("\nSetelah remove():")
print(vehicles)

# Mengurutkan sementara menggunakan sorted()
print("\nUrutan alfabetis:")
print(sorted(vehicles))

# Membalik urutan menggunakan reverse()
vehicles.reverse()
print("\nSetelah reverse():")
print(vehicles)

# Mengurutkan secara alfabetis menggunakan sort()
vehicles.sort()
print("\nSetelah sort():")
print(vehicles)

# Mengurutkan secara alfabetis terbalik
vehicles.sort(reverse=True)
print("\nUrutan alfabetis terbalik:")
print(vehicles)

# Menghitung jumlah elemen menggunakan len()
print("\nJumlah kendaraan:")
print(len(vehicles))