print([x if x % 2 == 0 else None for x in range(10)]
)
#<value-if-condition-is-true> if <condition> else <value-if-condition-is-false>
print([2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)])