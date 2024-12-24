def star_pattern(n):
    for i in range(1, n+1):
        print(*filter(None, ["*" for _ in range(i)]))