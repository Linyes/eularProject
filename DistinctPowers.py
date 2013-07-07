result = [a**b for a in range(2,101) for b in range(2,101)]
result = list(set(result))
print len(result)
