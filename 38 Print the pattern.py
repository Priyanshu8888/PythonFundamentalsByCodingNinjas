def pattern(n):
    mid = (n >> 1)
    if n & 1 != 0:
        mid += 1
    val = 1
    for i in range(mid):
        for j in range(val, val + n):
            print(j, end=' ')
        print()
        val += (n << 1)
    if n & 1 != 0:
        val -= (n << 1)
        val -= n
        for i in range(mid, n):
            for j in range(val, val + n):
                print(j, end=' ')
            print()
            val -= (n << 1)
    else:
        val -= n
        for i in range(mid, n):
            for j in range(val, val + n):
                print(j, end=' ')
            print()
            val -= (n << 1)


n = int(input())
pattern(n)