# contoh cara mengoding yang sederhana
def tambah():
    a = int (input("angka 1 :"))
    b = int (input("angka 2 :"))
    c = a+b
    print(c)

def kurang():
    a = int (input("angka 1 :"))
    b = int (input("angka 2 :"))
    c = a-b
    print(c)

def kali():
    a = int (input("angka 1 :"))
    b = int (input("angka 2 :"))
    c = a*b
    print(c)

def pilihan():
    print("1. tambah")
    print("2. kurang")
    print("3. kali")
    print("4. exit")

while True: 
    pilihan()
    pil = int(input("pilihan : "))
    if pil == 1:
        tambah()
    elif pil==2:
        kurang()
    elif pil==3:
        kali()
    else : 
        break