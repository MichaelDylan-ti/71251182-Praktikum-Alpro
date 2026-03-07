C_ke_F = lambda C: int((9/5) * C + 32)
C_ke_R = lambda C: int(0.8 * C)

A = int(input("Masukkan C: "))
B = int(input("Masukkan C: "))
C = int(input("Masukkan C: "))
print("F= ", C_ke_F(A))
print("R= ", C_ke_R(B))
print("F= ", C_ke_F(C))