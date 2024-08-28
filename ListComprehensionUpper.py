vegetables=['cabbage','spanish','pumkin','garlic']
veg=[x.upper() for x in vegetables]
print(veg)
print(vegetables)
veg=['Carrot' for  x in vegetables]
print(veg)
veg2=[ x if x !='spanish' else 'Radish' for x in vegetables]
print(veg2)