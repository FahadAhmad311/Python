'''numbers=[1,2,3,4,5]
print(sum(numbers))'''
def sum(numbers):
    total=0
    for x in numbers:
        total+=x
    return total
print(sum((2,3,5,6)))