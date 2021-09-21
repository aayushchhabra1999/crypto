## Generate the digest (md5sum) for the file passed in as the first command line argument.

from hashlib import md5
import sys

def message_digest(filepath):
    with open(filepath, 'rb') as file:
        return md5(file.read()).hexdigest()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(message_digest(sys.argv[1]))
    else:
        print(message_digest("src/files/example.txt"))