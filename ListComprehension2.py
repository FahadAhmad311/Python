sentence=[['The', 'cat', 'chases','the','mouse','.'],['The', 'dog', 'barks.']]
allWords=[word for sentence in sentence for word in sentence]
print(allWords)

allUniqueWords=list({word for sentence in sentence for word in sentence})
print(allUniqueWords)
allUniqueWords1=list(set(allWords))
print(allUniqueWords1)
