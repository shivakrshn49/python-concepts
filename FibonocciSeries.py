# 0, 1, 1, 2, 3, 5, 8, 13, 21 etc.,

def fibonocci_series(a=0, b=1, limit=25):
    if b < limit:
        return_value = a + b
        if return_value < limit:
            print return_value
            fibonocci_series(a=b, b=return_value)


# fibonocci_series()