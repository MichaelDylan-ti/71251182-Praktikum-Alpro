def cek_digit_belakang(a, b, c):
    a = a % 10
    b = b % 10
    c = c % 10

    if a == b or c == a or b == c :
        return True
    else:
        return False

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))
print (cek_digit_belakang(a=angka1, b=angka2, c=angka3))