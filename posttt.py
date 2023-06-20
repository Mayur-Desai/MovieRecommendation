import requests
api_key='b5f9e14fb97127ecc111aab55ba5da48'
movie_id='tt4154796'

url='https://api.themoviedb.org/3/movie/0302427/images?api_key=b5f9e14fb97127ecc111aab55ba5da48'
res = requests.get(url)
res=res.json()
print(res)