while True:
    print("\n===== MENU MATEMATIKA =====")
    print("1. Cek Bilangan Ganjil/Genap")
    print("2. Cek Bilangan Prima")
    print("3. Kalkulator")
    print("4. Keluar")
    print("===========================")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        x = int(input("Masukkan angka : "))

        if x % 2 == 0:
            print("Bilangan genap")
        else:
            print("Bilangan ganjil")

    elif pilihan == "2":
        x = int(input("Masukkan angka : "))

        if x < 2:
            print("Bukan bilangan prima")
        else:
            prima = True

            for i in range(2, x):
                if x % i == 0:
                    prima = False
                    break

            if prima:
                print("Bilangan prima")
            else:
                print("Bukan bilangan prima")

    elif pilihan == "3":
        print("\n===== KALKULATOR =====")
        angka1 = float(input("Masukkan angka pertama : "))
        operator = input("Masukkan operator (+, -, *, /) : ")
        angka2 = float(input("Masukkan angka kedua : "))

        if operator == "+":
            print("Hasil =", angka1 + angka2)
        elif operator == "-":
            print("Hasil =", angka1 - angka2)
        elif operator == "*":
            print("Hasil =", angka1 * angka2)
        elif operator == "/":
            if angka2 != 0:
                print("Hasil =", angka1 / angka2)
            else:
                print("Tidak bisa dibagi 0")
        else:
            print("Operator tidak tersedia")

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")

    print("---------------------------")