# def per(x,a,b):
#     s=''
#     x=int(str(x),a)
#     while x>0:
#         s = s + str(x%b)
#         x = x//b
#     return s[::-1]
#
# print(int('85667',9))
#
#
# def newvodka(x,base):
#     sys = '0123456789ABCDE'
#     s=''
#     while x>0:
#         s=sys[x%base]+s
#         x=x//base
#     return s
#
# print(int('10101',5))
# print(newvodka(651,15))
#
# print(bin(68))

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
    assert nleft == 0, 'Check all of n is accounted for'
    assert sum(x*y for x,y in zip(digits, seq)) == n, 'Assert digits are correct'
    while digits[0] == 0:
        digits.pop(0)
    return digits

n = 100
print('Fibonacci digit multipliers: %r' % sequence_down_from_n(n, fib))
for i in range(n + 1):
    print('%3i: %8s' % (i, ''.join(str(d) for d in zeckendorf(i))))