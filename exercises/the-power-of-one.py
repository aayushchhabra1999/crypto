import time
import random
import string
from hashlib import sha256

start = time.time()

n = 10000
for i in range(n):
    iter_start = time.time()
    preimage_seed = random.choice(string.ascii_lowercase)
    hash = sha256(preimage_seed.encode()).hexdigest()
    for c in string.ascii_lowercase:
        if sha256(c.encode()).hexdigest() == hash:
            break
    iter_end = time.time()
    print('time taken', iter_end - iter_start)

end = time.time()

print ("Average:", (end - start)/n)