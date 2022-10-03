import numpy as np
import pandas as pd

df2 = pd.read_csv('final.csv')
c = df2['vote_average'].mean()
m = df2['vote_count'].quantile(0.9)
q_movies = df2.copy().loc[df2['vote_count']>=m]

def weighted_rating(x,m=m,c=c):
  v = x['vote_count']
  R = x['vote_average']
  wr = (R*(v/(v+m)))+((m/(v+m))*c)
  return wr

q_movies['score'] = q_movies.apply(weighted_rating,axis=1)

q_movies = q_movies.sort_values('score',ascending = False)
output = q_movies[['title','poster_link','vote_average','release_date','runtime','overview']].head(20).values.tolist()
