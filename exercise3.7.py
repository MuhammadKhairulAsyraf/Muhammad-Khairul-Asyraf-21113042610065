guests = [
    "Kylian Mbappe",
    "Cristiano Ronaldo",
    "Erling Haaland",
    "Neymar Jr.",
    "Albert Einstein",
    "Zlatan Ibrahimovic"
]

print("Maaf, saya hanya bisa mengundang dua orang untuk makan malam.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, saya tidak bisa mengundang Anda untuk makan malam.")

print("\nDua orang yang masih diundang:")

for guest in guests:
    print(f"Halo {guest}, Anda tetap diundang untuk makan malam.")

del guests[0]
del guests[0]

print("\nDaftar tamu setelah dihapus:")
print(guests)