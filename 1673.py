while 1:
    try:
        n, k = map(int, input().split())
        result = 0 
        result += n
        while n//k:
            result += n//k
            n = n//k + n%k
        print(result)
    except:
        break