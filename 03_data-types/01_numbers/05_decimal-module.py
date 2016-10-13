from decimal import Decimal as D
# Output: Decimal('3.3')
print(D('1.1') + D('2.2')  ==  D('3.3') )

# Output: Decimal('3.000')
print(D('1.2') * D('2.50'))
print(D.sqrt(D('2')))