print("===================================")
print("       PROGRAM PERULANGAN ANGKA")
print("===================================")

angka_awal = int(input("Masukkan angka awal  : "))
angka_akhir = int(input("Masukkan angka akhir : "))

print("\nHasil Perulangan:")
print("-----------------------------------")

for angka in range(angka_awal, angka_akhir + 1):
    print("Angka:", angka)

print("-----------------------------------")
print("Program selesai.")