from django.shortcuts import render
import re


def Aditya(request):
        return render(request, 'home.html')

def count(request):
        fulltext = request.GET['Fulltext']
        countwords = re.findall(r"[\w']+", fulltext)
        totalwords = len(countwords)
        worddictionary = {}
        c = list()
        for word in countwords:
            if word in worddictionary:
                worddictionary[word] += 1
            else :
                worddictionary[word] = 1

        for w in sorted(worddictionary, key=worddictionary.get, reverse=True):
            c.append(str(w) + '-' + str(worddictionary[w]))


        return render(request, 'count.html', {'worddictionary': c, 'totalwords': totalwords})

def about(request):
        return render(request, 'about.html')


