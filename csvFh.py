with open('sample.csv') as fh:
    next(fh)
    for n, line in enumerate(fh):
        print (n)
        print (line)
