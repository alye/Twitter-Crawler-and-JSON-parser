import json,datetime,pytz

_author_='Alizishaan'


for lang in range(0,3):                                         #loop to process data in multiple languages
    if(lang==0):
        set_lang='en'
    elif(lang==1):
        set_lang='de'
    elif(lang==2):
        set_lang='ru'
        
    for day in range(0,5):                                      #loop to process data collected over multiple days
        in_file=str(day+1)+'_data_'+set_lang+'.txt'
    
        with open (in_file,'r') as inp_file:
            json_data=json.load(inp_file)
            for x in range(0,3):
                for y in range(0,100):
                    try:                                        #in case a page contains less than 100 tweets 
                        op_file='text_'+set_lang+'.json'
                        with open(op_file,'a',encoding='utf8') as out_file:
                            #Convert date to Solr format
                            fmt = '%Y-%m-%dT%H:%M:%SZ'
                            created_at=str(json_data[x]["statuses"][y]["created_at"])  
                            temp = datetime.datetime.strptime(created_at,'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)
                           
                            #List comprehension for URLs
                            d=[a for a in json_data[x]["statuses"][y]["entities"]["urls"]]
                            urls=[i['expanded_url'] for i in d]

                            #List comprehension for hashtags
                            hash_list=[a for a in json_data[x]["statuses"][y]["entities"]["hashtags"]]
                            h_list=[i['text'] for i in hash_list]

                            #defining a Tweet Dictionary

                            tweet={
                                
                                'id': json_data[x]["statuses"][y]["id_str"],
                               'text':json_data[x]["statuses"][y]["text"],
                               'lang':json_data[x]["statuses"][y]["lang"],
                               'created_at': str(temp.strftime(fmt)), 
                               'tweet_urls': urls,
                               'tweet_hashtags':h_list
                            }
                            json.dump(tweet,out_file,ensure_ascii=False,sort_keys=True, indent=4, separators=(',', ': '))
                            out_file.write(",")
                    except:
                        continue
