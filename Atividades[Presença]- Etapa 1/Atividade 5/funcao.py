def func_verificacao(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return False
    else:
        if x < y + z and y < x + z and z < x + y:
            return True
        return False
