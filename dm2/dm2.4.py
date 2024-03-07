def palindrome(str):
    reversed = str[::-1]
    lcp = ""
    for i in range(len(str)):
        if str[:i+1] == reversed[len(reversed)-i-1:]:
            lcp = str[:i+1]
    return reversed[:len(reversed)-len(lcp)] + str

print(palindrome("aabbaaa"))