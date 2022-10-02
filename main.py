def fib():
    memo = [1, 2]
    while True:
        memo.append(sum(memo))
        yield memo.pop(0)

def sequence_down_from_n(n, seq_generator):
    seq = []
    for s in seq_generator():
        seq.append(s)
        if s >= n: break
    return seq[::-1]

def zeckendorf(n):
    if n == 0: return [0]
    seq = sequence_down_from_n(n, fib)
    digits, nleft = [], n
    for s in seq:
        if s <= nleft:
            digits.append(1)
            nleft -= s
        else:
            digits.append(0)
    assert nleft == 0
    assert sum(x*y for x,y in zip(digits, seq)) == n
    while digits[0] == 0:
        digits.pop(0)
    return digits

n = 100
print('Fibonacci digit multipliers: %r' % sequence_down_from_n(n, fib))
for i in range(n + 1):
    print('%3i: %8s' % (i, ''.join(str(d) for d in zeckendorf(i))))
