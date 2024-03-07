def powerset(original):
    result = [[]]
    for i in original:
        subsets = [[i] + subset for subset in result]
        result.extend(subsets)
    return result

print(powerset([1,2,3]))