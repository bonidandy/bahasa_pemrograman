nim = int(input("Nim : "))
Nama = str (input("Nama : "))


def menu ():
    print ("Pilihan")
    print("1. capucino")
    print("2. teh")
    print ("3. exit")


while True:
    menu()
    pil = int(input("masukkan pilihan : "))

    if pil == 1:
        print ("memilih capucino")
        harga = int(input("Masukkan harga :"))
        ppn = harga * 10/100
        jumlah_bayar = harga + ppn
        print("Jumlah yang harus dibayarkan ", jumlah_bayar)
    elif pil == 2:
        print ("memilih teh")
        harga = int(input("Masukkan harga :"))
        ppn = harga * 10/100
        jumlah_bayar = harga + ppn
        print("Jumlah yang harus dibayarkan ", jumlah_bayar)
    else:
        print("Terima kasih ")
        break
