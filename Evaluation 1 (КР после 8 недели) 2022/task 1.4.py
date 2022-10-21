def min_integer(numba):
    if numba == 0:
        return 0
    elif numba < 0:
        pumba = -numba
    else:
        pumba = numba

    strokumba = str(pumba)
    zero = strokumba.count('0')
    if numba > 0:
        for i in range(1, 10):
            if strokumba.count(str(i)) != 0:
                first = i
                break
        hren = ''
        for i in range(10):
            hren = hren + str(i)
        result = hren[first] + hren[0]*zero + hren[first]*(strokumba.count(str(first)) - 1)
        for i in range(first + 1, 10):
            result = result + hren[i]*strokumba.count(str(i))
        return int(result)
    elif numba < 0:
        result = ''
        for i in range(9, -1, -1):
            result = result + strokumba.count(str(i))*str(i)
        return -int(result)

print(min_integer(-230579))