def cek_bilangan():
    print("===== PROGRAM CEK BILANGAN =====")
    angka = int(input("Masukkan sebuah bilangan: "))

    if angka % 2 == 0:
        print("Bilangan", angka, "adalah GENAP")
    else:
        print("Bilangan", angka, "adalah GANJIL")


def cek_prima():
    print("===== PROGRAM CEK BILANGAN PRIMA =====")
    angka = int(input("Masukkan bilangan: "))

    if angka > 1:
        for i in range(2, angka):
            if angka % i == 0:
                print("Bukan bilangan prima")
                break
        else:
            print("Bilangan prima")
    else:
        print("Bukan bilangan prima")


def main():
    while True:
        print("\n===== MENU =====")
        print("1. Cek Ganjil/Genap")
        print("2. Cek Bilangan Prima")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        try:
            if pilihan == "1":
                cek_bilangan()
            elif pilihan == "2":
                cek_prima()
            elif pilihan == "3":
                print("Program selesai. Terima kasih!")
                break
            else:
                print("Pilihan tidak valid, coba lagi.")
        except ValueError:
            print("Input harus berupa angka bulat!")


main()