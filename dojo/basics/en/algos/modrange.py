# Example 1:
amin = -10
amax = 10
b = 3

# modn will compute -10 mod 3 = 1, and 10 mod 3 = 1.
print(modn(amin, b))  # Output: 1
print(modn(amax, b))  # Output: 1

# slow_modrange will compute the minimum and maximum of modn(n, 3) for n in range(-10, 11)
# The resulting set of values are [0, 1, 2, 0, 1, 2, ...], hence the min is 0 and the max is 2.
print(slow_modrange(amin, amax, b))  # Output: (0, 2)

# fast_modrange computes the same result, but more efficiently.
# Since the range crosses zero, the result is the full range of modulus, which is [0, b-1] = [0, 2].
print(fast_modrange(amin, amax, b))  # Output: (0, 2)


# Example 2:
amin = 10
amax = 20
b = 5

# modn will compute 10 mod 5 = 0, and 20 mod 5 = 0.
print(modn(amin, b))  # Output: 0
print(modn(amax, b))  # Output: 0

# slow_modrange will compute the minimum and maximum of modn(n, 5) for n in range(10, 21)
# The resulting set of values are [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0], hence the min is 0 and the max is 4.
print(slow_modrange(amin, amax, b))  # Output: (0, 4)

# fast_modrange computes the same result, but more efficiently.
# Since the range (amax - amin = 10) is wider than the modulus (5), the result is the full range of modulus, which is [0, b-1] = [0, 4].
print(fast_modrange(amin, amax, b))  # Output: (0, 4)


# Example 3:
amin = 7
amax = 9
b = 5

# modn will compute 7 mod 5 = 2, and 9 mod 5 = 4.
print(modn(amin, b))  # Output: 2
print(modn(amax, b))  # Output: 4

# slow_modrange will compute the minimum and maximum of modn(n, 5) for n in range(7, 10)
# The resulting set of values are [2, 3, 4], hence the min is 2 and the max is 4.
print(slow_modrange(amin, amax, b))  # Output: (2, 4)

# fast_modrange computes the same result, but more efficiently.
# Since the range (amax - amin = 2) is narrower than the modulus (5), it computes the mod of the range ends and returns them.
print(fast_modrange(amin, amax, b))  # Output: (2, 4)
