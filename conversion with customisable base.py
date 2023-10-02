R = 0
N = int(input())
base = 16
bin = []

while N > 0:
    R = N % base
    N = N // base
    bin.append(R)

print(''.join(map(str, bin[::-1])))