#Created by Erdal Nayir
import time

def detectPosition(X,Y):
    if X <= 180 and Y <= 180:
        return "Kuzey Bati"
    elif X <= 180 and 180 < Y <= 360:
        return "Bati"
    if X <= 180 and 360 < Y <= 540:
        return "Guney Bati"

    if 180< X <= 360 and Y <= 180:
        return "Kuzey"
    elif 180< X <= 360 and 180 < Y <= 360:
        return "Merkez"
    if 180< X <= 360 and 360 < Y <= 540:
        return "Guney"

    if 360< X <= 540 and Y <= 180:
        return "Kuzey Dogu"
    elif 360< X <= 540 and 180 < Y <= 360:
        return "Dogu"
    if 360< X <= 540 and 360 < Y <= 540:
        return "Guney Dogu"
