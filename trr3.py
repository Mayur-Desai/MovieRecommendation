import urllib.request
import pandas as pd
md = pd. read_csv('./movies_metadata.csv')
pr = md['poster_path']
# print(pr)
# st="7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg"
# st=''
# /rhIRbceoE9lR4veEXuwCC2wARtG.jpg


# def do_i(st):
#     url = 'https://image.tmdb.org/t/p/w500/'+st
#     try:
#         urllib.request.urlretrieve(url, "./Posters"+st)
#     except:
#         return

s=" "


for i in pr:
    if type(i)==type(s):
        url = 'https://image.tmdb.org/t/p/w500/'+i
        try:
            urllib.request.urlretrieve(url, "./Posters"+i)
        except:
            continue

