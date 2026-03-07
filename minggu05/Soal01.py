def cek_angka(a, b, c):
    if a != b and b != c and a != c:
        if b + c == a or a + c == b or a + b == c:
            return True
    return False 

print(cek_angka(2, 3, 5))
print(cek_angka(1, 2, 2))