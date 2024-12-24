def alphabet_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(chr(ord('A') + j - 1), end=" ")
        for j in range(i-1, 0, -1):
            print(chr(ord('A') + j - 1), end=" ")
        print()