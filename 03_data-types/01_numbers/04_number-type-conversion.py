# areEqual = (1.1 + 2.2) == 3.3
# areEqual = (1.10 + 2.20) == 3.3
# print(areEqual)

# why? 1/3= 0.333333333333333
# Binary 1/3 = 0.00011001100110011001100110011 They'll never be equal

# Precision
import decimal

# Output: 0.1
print(0.1)

# Output: Decimal('0.1000000000000000055511151231257827021181583404541015625')
print(decimal.Decimal(0.1))