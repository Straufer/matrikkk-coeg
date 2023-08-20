#!/usr/bin/env python3

import numpy as np

# matriks
p = np.array([[2, 1], [-1, 5]])
q = np.array([[-3, 4], [-0, -4]])
r = np.array([[4, 3], [-2, 2]])

# soal
# 1. pq
# 2. pq^t
# 3. p(r+q)
# 4. (p+q)(p-q])

# 1
soal_1 = np.dot(p, q)
print(soal_1)


