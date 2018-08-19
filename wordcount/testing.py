'''fulltext = request.GET['Fulltext']
countwords = fulltext.split()
totalwords = len(countwords)'''
worddictionary = {'kjnkn':4, 'efgrs':6, 'fgesgv':7}
a = list()
b = list()
c = list()
k = len(a)
'''for word in countwords:
        if word in worddictionary:
                worddictionary[word] += 1
        else:
                worddictionary[word] = 1
'''
for key, value in worddictionary.items():
        a.append(key)
        b.append(value)
for i in range(k):
        c[i] = a[i] + '-' + b[i]
        print(c[i])

