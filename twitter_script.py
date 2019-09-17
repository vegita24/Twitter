from parse_twitter import parameter_parser
import json
import pandas as pd
import matplotlib.pyplot as plt

def trends(val):
    global dic
    df = pd.read_csv(val,encoding = 'unicode_escape')
    tweets = pd.DataFrame(columns=['text','hashtag','hashtag1','label'])
    tweets['text']=df['text'].astype(str)
    tweets['hashtag']=df['entities.hashtags.0.text'].astype(str)
    tweets['hashtag1']=df['entities.hashtags.1.text'].astype(str)
    
    tr=[]
    for i in dic:
        tr.append(i)
    for i in tweets.index:
        tweets['label'][i]=0
        for k in tr:
            if tweets['hashtag'][i].find(k)!=-1 or tweets['hashtag1'][i].find(k)!=-1:
                tweets['label'][i] = 1
                dic[k]=dic[k]+1
                break
                
        if tweets['label'][i]<1:
            tweets['label'][i]=0
    #final={}
    #final[args.number]=l
    

if __name__ == "__main__":
	#args = parameter_parser()
    dic={ 'PaulaAmorimNaPlanetGirls':0,
    'MonstruoDeEcatepec':0,
    'BeforeNetflixAndChill':0,
    'WorldMentalHealthDay':0,
    'MentalHealthDay':0,
    'mentalhealth':0,
    'AajKiRaat':0,
    'YargıSuçsuzDedi':0,
    'aborto':0,
    'MeToo':0,
    'PSAT':0,
    'SimpleWaysToUnwind':0,
    'ItTakesTwo':0,
    'AmazonGreatIndianFestival':0,
    'BTSLoveYourselfTour':0,
    'PasoALaRepública':0,
    'DebateDosVices':0,
    'JKLive':0,
    'LEAPcon':0,
    'KanyeWest':0,
    'Hurricane':0,
    'AMAs':0,
    'İnanmayaDevam':0,
    'SanayiBakanlığı200MakineMüh':0,
    'PursaklarBelediyesi':0,
    'AlbanMartirPorLaDemocracia':0,
    'AtatürkKırmızıÇizgimizdir':0,
    'Vingança':0,
    'NuncaMeDigas':0,
    'LadyDepartamentos':0,
    'ScaryStoriesForAdults':0,
    'ItaliaUcraina':0,
    'WednesdayWisdom':0,
    'inktober2018':0,
    'TheBigBillionDays':0,
    'inktober':0,
    'BTS':0,
    'MentalHealthDay2018':0,
    'HurricaneMichael':0,
    'Michael':0,
    'WorldMentalHealthDay2018':0,
    'Sevdamınİmtihanı':0,
    'DiaMundialSaludMental':0,
    'ConsequencesMusicVideo':0,
    'LaEsperanzaEsLaEducación':0,
    'OTDirecto10OCT':0,
    'MentalHealthAwarenessDay':0,
    'Mercedes Ninci':0,
    'Eric Holder':0,
    'Arda Turan':0,
    'Rafa Nadal':0,
    'SoldadoDefensorDeLaPatria':0,
    'De Vido':0,
    'metoo':0,
    'psat2018':0,
    'psat':0,
    'Mexico Beach':0,
    'BTSinLondon':0,
    'Keiko Fujimori':0,
    'MPN':0,
    'AravindhaSametha':0,
    'BTSXLondon':0,
    'bolsonaroCagao':0,
    'WorldMentaHealthDay2018':0}
    for i in range(0,59):
        val="./data/tweets/"+str(i)+".csv"
        trends(val)
    l=[]
    for i in dic:
            l.append([i,dic[i]])
    print(l)