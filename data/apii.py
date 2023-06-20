import requests
import pandas as pd
import sys
import threading, logging

# uncomment next line and add your tmdb api key
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlOTNlYmM5ZmI1ZTViZmJjYmFkNDExNGEyZGEyMzE0MCIsInN1YiI6IjYzN2UyNWM5ZTgxMzFkMDBlNmE4ZDBlYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.4v3-UYZQR77_SY2jS_9FVhZBfKS6qWEN3ieC7u_PLr0"
language_count = {
    'en':10000,
    'hi':5000,
    'bn':1000,
}


def get_movies(lang, freq):
  url = 'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&with_original_language={lang}'.format(api_key=api_key,lang=lang)
  # print(url)
  movies = []
  page = 1
  progress = 0
  while movies.__len__()<freq:
    try:
        res = requests.get(url+"&page="+str(page))
    except:
        raise ('not connected to internet or movidb issue')

    if res.status_code != 200:
        print ('error')
        return []

    res = res.json()
    
    if 'errors' in res.keys():
      print('api error !!!')
      return movies

    movies = movies + res['results']

    if progress != round(len(movies)/freq*100):
      progress = round(len(movies)/freq*100)
      if progress%5==0:
        print( progress, end="%, ")
        
    page = page + 1
    # break
    # print(res)
  return movies

all_movies = []

for key in language_count:
  # print(key,language_count[key])
  print("Downloading ", key, end=" : ")
  movies = get_movies(key,language_count[key])
  all_movies = all_movies + movies
  print('Total movies found : ', movies.__len__())
  # break

  df = pd.DataFrame(all_movies, columns=['genre_ids', 'id', 'original_language',
       'overview', 'popularity', 'release_date', 'title', 'vote_average', 'vote_count'])
df.to_csv('movies_dataset.csv', index=False)
df.to_pickle('movies_dataset.pk',)
#print(df)

ids = df['id'].tolist()

def get_credits(ids):
  total_len = len(ids)
  progress = 0
  done_items = 0
  credits = []

  def get_credit(id):
    url = 'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}'.format(api_key=api_key,movie_id=id)
    try:
        res = requests.get(url)
    except:
        raise ('not connected to internet or movidb issue')

    if res.status_code != 200:
        print ('error')
        return []

    res = res.json()
    
    if 'errors' in res.keys():
      print('api error !!!')
      return credits
    # print(res)
    credits.append(res)

  threads = list()
  for id in ids:
    x = threading.Thread(target=get_credit,args=(id,))
    threads.append(x)
    x.start()
  for index, thread in enumerate(threads):
      # logging.info("Main    : before joining thread %d.", index)
      thread.join()    

  return credits

movie_credits = get_credits(ids)

new_movie_credits = {'cast':[],'crew':[]}
for movie_credit in movie_credits:
  
  new_movie_credits['cast'].append( {'id' : movie_credit['id'], 'cast' :[]} )
  for credit in movie_credit['cast']:
    new_movie_credits['cast'][ -1 ][ 'cast' ].append({
        'cast_id': credit['id'],
        'name': credit['name'],
        'character': credit['character'],
    })
    # break
  
  new_movie_credits['crew'].append( {'id' : movie_credit['id'], 'crew' :[]} )
  for crew in movie_credit['crew']:
    new_movie_credits['crew'][ -1 ][ 'crew' ].append({
        'crew_id': crew['id'],
        'name': crew['name'],
        'department': crew['department'],
    })
  # break

cast_df = pd.DataFrame(new_movie_credits['cast'])
crew_df = pd.DataFrame(new_movie_credits['crew'])

cast_df.to_csv('cast_dataset.csv', index=False)
crew_df.to_csv('crew_dataset.csv', index=False)

def get_keywords(ids):
  total_len = len(ids)
  progress = 0
  keywords = []

  def get_keyword(id):
    url = 'https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key={api_key}'.format(api_key=api_key,movie_id=id)
    try:
        res = requests.get(url)
    except:
        raise ('not connected to internet or movidb issue')

    if res.status_code != 200:
        print ('error')
        return []

    res = res.json()
    
    if 'errors' in res.keys():
      print('api error !!!')
      return keywords
    # print(res)
    keywords.append(res)

    # for id in ids:
    #   get_cred

  threads = list()
  for id in ids:
    x = threading.Thread(target=get_keyword,args=(id,))
    threads.append(x)
    x.start()
  for index, thread in enumerate(threads):
    logging.info("Main    : before joining thread %d.", index)
    thread.join()

  return keywords

movie_keywords = get_keywords(ids)
keywords_df = pd.DataFrame(movie_keywords)
keywords_df.to_csv('keywords_dataframe.csv')
#print(keywords_df)
