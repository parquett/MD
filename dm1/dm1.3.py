def getLongestSubstring(x):
    if len(set(x)) == len(x):
        return len(x)
    substring = ''
    strLen = 1
    for a in x:
        if a not in substring:
            substring = substring + a
            strLen = max(strLen, len(substring))
        else:
            substring = substring.split(a)[1] + a
    print(substring)
    return strLen


print(getLongestSubstring("xywxywyy"))