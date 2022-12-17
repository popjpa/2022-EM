def soma_multipla(*args):
    s = 0
    for i in args:
        s += i
    print(s)
    print(args)

soma_multipla(10,10,10,1,101)