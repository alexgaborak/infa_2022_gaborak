import numpy as np
mat_n1_3_3 = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
mat_n2_3_2 = np.array([(1, 1), (1, 1), (1, 1)])
ident_mat = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)])

# uncomment below for see matrix
# print(mat_n1_3_3)
# print(mat_n2_3_2)
# print(ident_mat)

mat_mult_dot = np.dot(mat_n1_3_3, mat_n2_3_2)
print(mat_mult_dot)
mat_mult_matmul = np.matmul(mat_n1_3_3, mat_n2_3_2)
print(mat_mult_matmul)  # same result

print(np.matmul(mat_n1_3_3, ident_mat), '\n', np.matmul(ident_mat, mat_n1_3_3))
