import string

def generate(alphabet, max_len):
    if max_len <= 0: return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generate(alphabet, max_len - 1):
            yield c + next

print(list(generate(string.ascii_lowercase.encode('utf-8'), 2)))