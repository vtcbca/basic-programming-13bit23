def is_palindrome(s):
    return all(s[i] == s[~i] for i, _ in enumerate(s[:len(s) // 2]))