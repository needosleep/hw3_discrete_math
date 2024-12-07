import hashlib

s = "DM Fall 2024 HW3"

hash = int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16)
hash = bin(hash)[2:]

def split_bin(string, block):
    res = []
    for i in range(0, len(string) - block + 1, block):
        res.append(string[i: i + block])
    return res

d = 0

for i in split_bin(hash, 32):
    d ^= int(i)

w = d ^ int("7613a0ca", 16)
print(w)