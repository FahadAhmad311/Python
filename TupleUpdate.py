fruits=('Mango','Apricot','Grapes','Strawberry')
fruits1=list(fruits)
fruits1.append('Blueberry')
fruits1[2]='Banana'
fruits=tuple(fruits1)
print(type(fruits))
print(fruits)
vegetable=('Onion','Potato','Tomato','Chillies')
x=list(vegetable)
x.remove('Chillies')
vegetable=tuple(x)
print(vegetable)
del (fruits)
print(fruits)
print(vegetable)