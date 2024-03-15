# importing the numpy and pandas python modules
import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


# storing the movies.cs file's data in a variable named 'movies'
movies = pd.read_csv('./tmdb_5000_movies.csv')

# storing the credits.cs file's data in a variable named 'credits'
credits = pd.read_csv('./tmdb_5000_credits.csv')

# merging both the file's data and storing it in another variable named 'mergedResult'
mergedResult = movies.merge(credits, on='title')


# only storing those columns which are required in our project
movies = mergedResult[['movie_id','title', 'overview', 'genres', 'keywords', 'cast', 'crew']]






# movies.isnull().sum()  -->  it helps in checking whether any data have some missing values or not

# as in the dataset only 3 rows are present with some missing values that's why we will remove them.

movies.dropna(inplace=True)

# movies.duplicated(sum)  -->  it is used to check whether any duplicated values are present or not

# print(movies.iloc[0].genres)
# here 'iloc' means inteer location based indexing



# function that will convert and format the data
def convert(obj):
    L = []
    for i in eval(obj):
        L.append(i['name'])
    return L

def convertTo3(obj):
    counter = 0
    L = []
    for i in eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter+=1
        else:
            break
    return L

def convertDirector(obj):
    L = []
    for i in eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L


# this function will remove all the spaces between
def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1




# applying the function in some of the columns
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convertTo3)
movies['cast'] = movies['cast'].apply(lambda x:x[0:3])
movies['crew'] = movies['crew'].apply(convertDirector)



# movies['cast'] = movies['cast'].apply(collapse)
# movies['crew'] = movies['crew'].apply(collapse)
# movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)
movies['overview'] = movies['overview'].apply(lambda x:x.split())



# creating a new column names tags which will contain all the keywords, genres, cast, etc
movies['tags'] = movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew'] + movies['overview']



# creating a new data set with only 3 columns, and remove all other column which are not required
new_DataSet = movies.drop(columns=['overview','genres','keywords','cast','crew'])


# converting the array to string and making all the string characters to lower case
new_DataSet['tags'] = new_DataSet['tags'].apply(lambda x:" ".join(x))
new_DataSet['tags'] = new_DataSet['tags'].apply(lambda x:x.lower())


cv = CountVectorizer(max_features=5000, stop_words="english")

vectors = cv.fit_transform(new_DataSet['tags']).toarray()



def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)



new_DataSet['tags'] = new_DataSet['tags'].apply(stem)


similarity = (cosine_similarity(vectors))


def recommend(movie):
    movieResult = []
    movie_index = new_DataSet[new_DataSet['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[:6]
    for i in movie_list:
        movieResult.append(movies.iloc[i[0]])
    return movieResult


def getMovieDetails(movie):
    index = movies[movies['title'] == movie].index[0]
    value = movies.iloc[index]
    return value
