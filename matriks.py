#!/usr/bin/env python3

import numpy as np

a = np.array(([-2, 4], [-3,5]))
b = np.array(([1,1], [-2,-3]))
c = np.array(([-6, 2], [-5, 2]))

print("matriks A")
print(a)

print("matriks B")
print(b)

print("matriks C")
print(c)

# soal nya itu a + b - c
hasil = a + b - c

print("hasil\n", hasil)

# soal nya itu 3b + 2c
soal2_formula = (3 * b) + (2 * c)
print("hasil\n", soal2_formula)

# soal c |A| + |B| + |C|
determinan_a = np.linalg.det(a)
determinan_b = np.linalg.det(b)
determinan_c = np.linalg.det(c)
hasil_soal3 = determinan_a + determinan_b + determinan_c

print(hasil_soal3)

# soal perkalian matriks a kali c
hasilDot = np.dot(a, c)
hasilAt = a @ c
hasilMatmul = np.matmul(a, c)

print("hasil\n", hasilDot)
print("hasil\n", hasilAt)
print("hasil\n", hasilMatmul)
