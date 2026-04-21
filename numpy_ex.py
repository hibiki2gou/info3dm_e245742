import numpy as np

A = np.array([[1]] * 5)

B = np.array([[1]] * 5, dtype = float)  # 配列全体の型をfloatに変更
B[2] = 3.14

C = A.copy()
C_t= C.T    # Cを転置

D = np.dot(C, C_t)

E = np.random.rand(10)

F = np.random.normal(loc = 10, scale = 2, size = (2, 5))

G = np.random.normal(loc = 10, scale = 2, size = (5, 2))

H = np.dot(F, G)

print(A)            # (1)
print(B)            # (2)
print(C_t)          # (3)
print(D)            # (4)
print(E)            # (5)
print(F)            # (6)
print(F[:, 2])      # (7)
print(F[:, 3:4])    # (8)    
print(H)            # (9)