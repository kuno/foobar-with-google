def answer(xs):
    pos = [n for n in xs if n > 1]
    nag = [n for n in xs if n < -1]

    #
    nag.sort()
    if (len(nag) % 2) == 1:
        nag.pop()

    output = 1
    print(nag)
    for n in (pos + nag):
       output *= abs(n)

    return str(output)
