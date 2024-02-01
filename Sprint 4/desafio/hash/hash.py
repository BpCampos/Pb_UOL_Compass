import hashlib

while True:

    h = hashlib.sha1()

    string = input("Digite qualquer coisa: ")

    encoded_string = string.encode()

    h.update(encoded_string)

    print(h.hexdigest())
