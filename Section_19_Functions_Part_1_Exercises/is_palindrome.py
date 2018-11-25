def is_palindrome(word):
    new = [c for c in word.lower() if c != ' ']
    return new == new[::-1]

print(is_palindrome('testing') == False)
print(is_palindrome('tacocat') == True)
print(is_palindrome('hannah') == True)
print(is_palindrome('robert') == False)
print(is_palindrome('amanaplanacanalpanama') == True)
