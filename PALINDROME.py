"""def palin(N):
    S = ogd(N) - 2
    L = ogd(N) - 1
    if S<=0 : return True
    N1 = N // 10**S
    N2 = N % 10
    if N1 == N2 :
        return palin((N-N1*10**L) // 10)
    else : return False"""

def ogd(N):
    return len(str(N))
