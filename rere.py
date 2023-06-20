# matplotlib inline
import numpy as np
import dataframe_image as dfi
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate
from surprise.model_selection import KFold
import warnings
# from test import get_movie_id,getinput
import cv2
import os
warnings.simplefilter('ignore')

md = pd. read_csv('./movies_metadata.csv')
# md.head()

md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(
    lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

links_small = pd.read_csv('./links_small.csv')
links_small = links_small[links_small['tmdbId'].notnull()
                          ]['tmdbId'].astype('int')

md = md.drop([19730, 29503, 35587])

md['id'] = md['id'].astype('int')

smd = md[md['id'].isin(links_small)]
# print(smd.shape)

# Movie Description Based Recommender

smd['tagline'] = smd['tagline'].fillna('')
smd['description'] = smd['overview'] + smd['tagline']
smd['description'] = smd['description'].fillna('')

# tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
# tfidf_matrix = tf.fit_transform(smd['description'])

# print(tfidf_matrix.shape)

# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# smd = smd.reset_index()
# titles = smd['title']
# indices = pd.Series(smd.index, index=smd['title'])


def get_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]


# print(get_recommendations('Guardians of the Galaxy').head(15)) #shows error for The Avengers


"---------------------------------------"
# Metadata Based Recommender
"---------------------------------------"

credits = pd.read_csv('./credits.csv')
keywords = pd.read_csv('./keywords.csv')

keywords['id'] = keywords['id'].astype('int')
credits['id'] = credits['id'].astype('int')
md['id'] = md['id'].astype('int')

# print(md.shape)

md = md.merge(credits, on='id')
md = md.merge(keywords, on='id')

smd = md[md['id'].isin(links_small)]
# print(smd.shape)

smd['cast'] = smd['cast'].apply(literal_eval)
smd['crew'] = smd['crew'].apply(literal_eval)
smd['keywords'] = smd['keywords'].apply(literal_eval)
smd['cast_size'] = smd['cast'].apply(lambda x: len(x))
smd['crew_size'] = smd['crew'].apply(lambda x: len(x))


def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan


smd['director'] = smd['crew'].apply(get_director)

smd['cast'] = smd['cast'].apply(lambda x: [i['name']
                                for i in x] if isinstance(x, list) else [])
smd['cast'] = smd['cast'].apply(lambda x: x[:3] if len(x) >= 3 else x)

smd['keywords'] = smd['keywords'].apply(
    lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

smd['cast'] = smd['cast'].apply(
    lambda x: [str.lower(i.replace(" ", "")) for i in x])
smd['director'] = smd['director'].astype('str').apply(
    lambda x: str.lower(x.replace(" ", "")))
smd['director'] = smd['director'].apply(lambda x: [x, x, x])

s = smd.apply(lambda x: pd.Series(x['keywords']), axis=1).stack(
).reset_index(level=1, drop=True)
s.name = 'keyword'
s = s.value_counts()
# print(s[:5])

s = s[s > 1]
stemmer = SnowballStemmer('english')
stemmer.stem('dogs')


def filter_keywords(x):
    words = []
    for i in x:
        if i in s:
            words.append(i)
    return words


smd['keywords'] = smd['keywords'].apply(filter_keywords)
smd['keywords'] = smd['keywords'].apply(lambda x: [stemmer.stem(i) for i in x])
smd['keywords'] = smd['keywords'].apply(
    lambda x: [str.lower(i.replace(" ", "")) for i in x])

smd['soup'] = smd['keywords'] + smd['cast'] + smd['director'] + smd['genres']
smd['soup'] = smd['soup'].apply(lambda x: ' '.join(x))

count = CountVectorizer(analyzer='word', ngram_range=(
    1, 2), min_df=0, stop_words='english')
count_matrix = count.fit_transform(smd['soup'])

cosine_sim = cosine_similarity(count_matrix, count_matrix)

smd = smd.reset_index()
titles = smd['title']
indices = pd.Series(smd.index, index=smd['title'])

# print(get_recommendations('The Martian').head(15))
directory = 'Posters'

dr = ''


def getinput(filen):
    global dr
    dr = 'Posters\\'+f'{filen}'


# getinput('l8lq77bNqJY94JCMPI731jwtDsE.jpg')
img1 = cv2.imread(dr)


def try_very_hard():
    def check(img_p):
        img2 = cv2.imread('Posters/'+img_p)
    # img2=cv2.imread('asd2.jpg')
        try:
            diff = cv2.subtract(img1, img2)

            result = not np.any(diff)
            if result is True:
                # print("Image Found!!!")
                return img_p
        except:
            return

    for file_name in os.listdir(directory):
        st = f'{file_name}'
        t = check(st)
        if type(t) != type(None):
            break
    return t


def get_movie_id():
    md = pd.read_csv('movies_metadata.csv')
    pr = md['poster_path']
    rc = md['original_title']
    c = 0
    poster_id = try_very_hard()
    poster_id1 = '/'+poster_id
    for i in pr:
        st = f'{i}'
        if st == poster_id1:
            break
        c += 1
    return rc[c]


print(get_movie_id())


#  needs debugging
def improved_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:26]
    movie_indices = [i[0] for i in sim_scores]

    # shows error for year
    movies = smd.iloc[movie_indices][['title', 'vote_count', 'vote_average']]
    vote_counts = movies[movies['vote_count'].notnull()
                         ]['vote_count'].astype('int')
    vote_averages = movies[movies['vote_average'].notnull(
    )]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(0.60)
    qualified = movies[(movies['vote_count'] >= m) & (
        movies['vote_count'].notnull()) & (movies['vote_average'].notnull())]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    # qualified['wr'] = qualified.apply(weighted_rating, axis=1) # error for weighted_rating
    qualified = qualified.sort_values('vote_average', ascending=False).head(15)
    # qualified.to_csv("As.csv", index=False)
    dfi.export(qualified, 'qualified.png')
    return qualified


print(improved_recommendations(get_movie_id()))


reader = Reader()
ratings = pd.read_csv('./ratings_small.csv')
# ratings.head()
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
# data.split(n_folds=5)
kf = KFold(n_splits=5)
kf.split(data)
svd = SVD()
cross_validate(svd, data, measures=['RMSE', 'MAE'])
trainset = data .build_full_trainset()
svd.fit(trainset)
ratings[ratings['userId'] == 1]
# svd.predict(1, 302, 3)


def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan


id_map = pd.read_csv('./links_small.csv')[['movieId', 'tmdbId']]
id_map['tmdbId'] = id_map['tmdbId'].apply(convert_int)
id_map.columns = ['movieId', 'id']
id_map = id_map.merge(smd[['title', 'id']], on='id').set_index('title')
#id_map = id_map.set_index('tmdbId')

indices_map = id_map.set_index('id')


def hybrid(userId, title):
    idx = indices[title]
    tmdbId = id_map.loc[title]['id']
    # print(idx)
    movie_id = id_map.loc[title]['movieId']

    sim_scores = list(enumerate(cosine_sim[int(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:26]
    movie_indices = [i[0] for i in sim_scores]

    movies = smd.iloc[movie_indices][[
        'title', 'vote_count', 'vote_average', 'id']]
    movies['est'] = movies['id'].apply(lambda x: svd.predict(
        userId, indices_map.loc[x]['movieId']).est)
    movies = movies.sort_values('est', ascending=False)
    return movies.head(10)


# print(hybrid(1, 'Fast Five'))
