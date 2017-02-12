def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return  int(''.join([str(i) for i in digits[::-1]]))

def algo(n, b):
    x = y = 0
    raw = [s for s in n]

    #
    raw.sort()
    for i, val in enumerate(raw):
        _i = int(val)
        #print(_i)
        _p = pow(b, abs(i - (len(raw) - 1)))
        #print(_p)
        _y = _i * _p
        #print(_y)
        y += _y

    #print(y)
    raw.reverse()
    for i, val in enumerate(raw):
        x += int(val) * pow(b, abs(i - (len(raw) - 1)))
    #print(x)
    z = x - y

    zs = str(numberToBase(z, b)) if z > 0 else str(z)
    if (len(zs) < len(raw)):
        j = len(raw) - len(zs)
        return ''.join(["0" for _ in range(j)]) + zs
    else:
        return zs

def answer(n, b):
    ref = []
    _in = algo(n, b)
    ref.append(_in)
    while True:
        _out = algo(_in, b)
        if (_in == _out):
            return 1
        elif (_out in ref):
            i = ref.index(_out)
            j = ref.index(_in)

            return abs(j - i) + 1
        else:
            _in = _out
            ref.append(_in)
