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