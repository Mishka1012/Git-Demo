
def decimal_part(n):
    if type(n) == int:
        return 0
    return float('0.' + str(n).split('.')[-1])

one = decimal_part(1.2)# ➞ 0.2
two = decimal_part(-3.73)# ➞ 0.73
three = decimal_part(10)# ➞ 0

print(one)
print(two)
print(three)