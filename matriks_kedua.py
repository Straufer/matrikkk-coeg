#!/usr/bin/env python3

import numpy as np

# bunch of matrix
p = np.array([[2, 1], [-1, 5]])
q = np.array([[-3, 4], [-0, -4]])
r = np.array([[4, 3], [-2, 2]])

# question?
# 1. pq
# 2. pq^t
# 3. p(r+q)
# 4. (p+q)(p-q)
 
# guess
# 1. -6, 4, 3, -24
# 2. -2, -4, 23, -20
# 3. 0, 7, -11, -17
# 4. -10, 48, -6, 12

# 1
soal_1 = np.dot(p, q)
print(f"question 1: \n{soal_1}")

# 2
soal_2 = np.dot(p, np.transpose(q))
print(f"question 2: \n{soal_2}")

# 3
sum_rq = np.add(r, q)
soal_3 = np.dot(p, sum_rq)
print(f"question 3: \n{soal_3}")

# 4 
sum_plus = np.add(p, q)
sum_mines = np.subtract(p, q)
soal_4 = np.dot(sum_plus, sum_mines)
print(f"question 4: \n{soal_4}")
