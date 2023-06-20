import pandas as pd
md = pd. read_csv('./data/movies_dataset.csv')
pr=md['genre_ids']
d={
    '28':'Action',
    '12': 'Adventure',
    '16':'Animation',
    '14': 'Fantasy',
    '10751': 'Family',
    '35': 'Comedy',
    '18': 'Drama',
    '10749':'Romance',
    '80': 'Crime',
    '53': 'Thriller',
    '878':'Science Fiction',
    '27':'Horror',
    '9648':'Mystery',
    '36':'History',
    '10769':'Foreign',
    '10402':'Music',
    '99':'Documentary',
    '10752':'War',
    '37':'Western'

}
c=0

for i in pr:
    #"[80,90,09]"
    i=i[1:-1]
    st=i.split(', ')#['80','90','09']
    f=[]   
    for j in st:
        r={}
        if j in d:
            r['id']=int(j)
            r['name']=d[j]
        f.append(r)
    pr[c]=f
    c=c+1


# pr[0]=[{'id':80,'name':'Crime'},{'id':35,'name': 'Comedy'},{'id':18,'name': 'Drama'}]
pr.to_csv("All.csv", index=False)
# print(pr)