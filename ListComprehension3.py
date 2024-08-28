tags = [u'man', u'you', u'are', u'awesome']
entries = [[u'man', u'thats'],[ u'right',u'awesome']]

result = []
[result.extend(entry) for tag in tags for entry in entries if tag in entry]

print(result)


words="Aon1iaml00kingf0r0pportuni8y"
wordcheck=[x for x in words if x.isdigit()]
print(wordcheck)