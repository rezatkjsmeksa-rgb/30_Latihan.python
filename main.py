from ganjilgenap30 import cek_bilangan, cek_prima
from bangundatar30 import hitung_persegi, hitung_persegi_panjang
from bangunruang30 import hitung_kubus, hitung_balok


def menu():
    while True:
        print("\n===== MENU UTAMA =====")
        print("1. Cek Bilangan Ganjil/Genap")
        print("2. Cek Bilangan Prima")
        print("3. Hitung Persegi")
        print("4. Hitung Persegi Panjang")
        print("5. Hitung Kubus")
        print("6. Hitung Balok")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            cek_bilangan()
        elif pilihan == "2":
            cek_prima()
        elif pilihan == "3":
            hitung_persegi()
        elif pilihan == "4":
            hitung_persegi_panjang()
        elif pilihan == "5":
            hitung_kubus()
        elif pilihan == "6":
            hitung_balok()
        elif pilihan == "7":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


menu()