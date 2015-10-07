#An Alizishaan Khatri creation

from twython import Twython
import json

APP_KEY=""
APP_SECRET=""

ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET=""

twitter = Twython(APP_KEY, APP_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#code to retreive tweets: one page at a time

#specify no of tweets

n=100

#specify search keywords

keywords_en=['head transplant','epidemic','medical marijuana']
keywords_de=['medizinische','durchfall','infektion'] 
keywords_ru=['медицинская','диарея','инфекция']

#specify folder/file number

folder="6_"

file_en=folder+'data_en.txt'
file_de=folder+'data_de.txt'
file_ru=folder+'data_ru.txt'

for x in range(0,3):  
    with open(file_en, 'a') as outfile_en:
        if(x==0):
            outfile_en.write('[')
            
        result=twitter.search(q=keywords_en[x],lang='en',until='2015-09-18',count=n)
        json.dump(result, outfile_en)
        if(x!=2):
            outfile_en.write(",")
        else:
            outfile_en.write(']')

    with open(file_de, 'a') as outfile_de:
        if(x==0):
            outfile_de.write('[')
        result=twitter.search(q=keywords_de[x],lang='de',until='2015-09-18',count=n)
        json.dump(result, outfile_de)   
        if(x!=2):
            outfile_de.write(",")
        else:
            outfile_de.write(']')

    with open(file_ru, 'a') as outfile_ru:
        if(x==0):
            outfile_ru.write('[')
        result=twitter.search(q=keywords_ru[x],lang='ru',until='2015-09-18',count=n)
        json.dump(result, outfile_ru)   
        if(x!=2):
            outfile_ru.write(",")
        else:
            outfile_ru.write(']')
