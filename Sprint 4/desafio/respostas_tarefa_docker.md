## 1

### Dockerfile:

```Dockerfile
FROM python

WORKDIR /app

COPY . .

CMD ["python", "carguru.py"]
```

### Comando

- `docker run --name python_app desafio-docker`

## 2

Sim, pelo comando: `docker start -i <nome_do_container>`

## 3

### Script

```Python
import hashlib

while True:

    h = hashlib.sha1()

    string = input("Digite qualquer coisa: ")

    encoded_string = string.encode()

    h.update(encoded_string)

    print(h.hexdigest())
```

### Dockerfile

```Dockerfile
FROM python

WORKDIR /app

COPY . .

CMD ["python", "hash.py"]

comando de inicialização:
```

### Comando

`docker run -it --name python_hash mascarar-dados`
