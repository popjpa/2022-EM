def diversos_argumentos(*args):
    for i in args:
        print(f'{i} é o argumento {args.index(i)}')

diversos_argumentos(10, 20, 30, 'oi', 550, 1000, 'olá')