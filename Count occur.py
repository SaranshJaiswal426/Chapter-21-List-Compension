print (sum(
 1 for x in range(1000)
 if x % 2 == 0 and
 '9' in str(x)
))
