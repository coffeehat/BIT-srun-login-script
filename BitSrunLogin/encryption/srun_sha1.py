import hashlib
def get_sha1(value):
    return hashlib.sha1(value.encode()).hexdigest()
if __name__ == '__main__':
    print(get_sha1("123456"))