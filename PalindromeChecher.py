def is_palindrome(s):
    s = ''.join(e.lower() for e in s if e.isalnum())
    
    return s == s[::-1]

result = is_palindrome('eye')
print(result)
