while True:
    print("\n===== CEK GANJIL / GENAP =====")

    angka = int(input("Masukkan angka: "))

    if angka % 2 == 0:
        print("Angka", angka, "adalah GENAP")
    else:
        print("Angka", angka, "adalah GANJIL")

    ulang = input("Cek angka lagi? (y/n): ")

    if ulang.lower() == "n":
        print("Program selesai.")
        break