import hashlib

h = hashlib.md5()
h.update(b'abcdef')
h.hexdigest()

print(h)
