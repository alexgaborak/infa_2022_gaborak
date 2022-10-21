def min_integer(numba):
    if numba == 0:
        return 0
    elif numba < 0:
        pumba = -numba
    else:
        pumba = numba

    strokumba = str(pumba)
    zero = strokumba.count('0')
    one = strokumba.count('1')
    if numba > 0:
        hren = ''
        for i in range(10):
            hren = hren + str(i)
        result = hren[1] + hren[0]*zero + hren[1]*(one - 1)
        for i in range(2, 10):
            result = result + hren[i]*strokumba.count(str(i))
        return int(result)
    elif numba < 0:
        result = ''
        for i in range(9, -1, -1):
            result = result + strokumba.count(str(i))*str(i)
        return -int(result)

