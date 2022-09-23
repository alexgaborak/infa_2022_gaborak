def dot_product(n, vector1, vector2):
    scalar_product = 0
    for i in range(n):
        scalar_product += vector1[i] * vector2[i]

    return scalar_product
