def parametros(*args, **kwargs):
    for i in args:
        print(i)

    for j in kwargs:
        print(kwargs[j])


parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)