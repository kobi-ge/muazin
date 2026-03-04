import hashlib

def generate_unique_id(path, ctime, size):
    full_str = path + ctime + str(size)
    res = hashlib.md5(full_str.encode())
    return res.digest()


