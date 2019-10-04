def byte_to_int(num):
    return int.from_bytes(num, byteorder='big')


def pixel(r, g, b):
    return (byte_to_int(r), byte_to_int(g), byte_to_int(b))


def printf(string):
    print(string, end='')