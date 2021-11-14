# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import seaborn as sns
# import nltk
# import string
import difflib
!pip install geopy
from pyproj import Proj, transform
from geopy import GoogleV3
from sklearn import tree
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
# from sklearn.feature_extraction.text import TfidfVectorizer
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import SnowballStemmer
# nltk.download('punkt')
# nltk.download('stopwords')

egrul = pd.read_excel("Data/eg.xlsx")
licence1 = pd.read_excel("Data/licence1.xls")
licence2 = pd.read_excel("Data/licence2.xls")
NVOS = pd.read_excel("Data/NVOS.xlsx")
register_of_licenses = pd.read_excel("Data/register_of_licenses.xlsx")
reg_pollutant = pd.read_excel("Data/reg_pollutant.xlsx")

print(NVOS.columns.values)

NVOS.groupby('Категория \nобъекта НВОС')['Кол-во \nисточников выбросов'].nunique().reset_index().sort_values('Кол-во \nисточников выбросов', ascending=True)

egrul['Вид деятельности'].unique()

print(egrul.columns.values)

def detector(x_c, y_c, r):
    pass

bad_performances = ['обработка металлов', 'обращение с отходами', '']

def similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()

similarity(df[2], data[0])



egrul.shape

len(egrul['Адрес'].unique())

place = '454080, г. Челябинск, п. Мелькомбинат 2 участок 1, д. 37'
location = GoogleV3(api_key="AIzaSyApxlxXIdRM9sWefCgQNHTdCewnxkccb_Q", domain="maps.google.ru").geocode(place)
print(location.address)
print(location.latitude, location.longitude)

data_address = list(egrul['Адрес'])

def convert(address):
    location = GoogleV3(api_key="AIzaSyApxlxXIdRM9sWefCgQNHTdCewnxkccb_Q", domain="maps.google.ru").geocode(address)
    return [location.latitude, location.longitude]

coord = convert(data_address[1])

print(coord)
print(type(coord))

coordinates = list(map(convert, data_address))

!pip install pyproj

def to_x_and_y(coordinates):
    inProj = Proj(init='epsg:3857')
    outProj = Proj(init='epsg:4326')
    x1,y1 = -11705274.6374, 4826473.6922
    x2,y2 = transform(inProj,outProj,x1,y1)
    return x2,y2



inProj = Proj(init='epsg:3857')
outProj = Proj(init='epsg:4326')
x1,y1 = -11705274.6374, 4826473.6922
x2,y2 = transform(inProj,outProj,x1,y1)
print (x2,y2)

def in_circle(center_x, center_y, radius, x, y):
    square_dist = (center_x - x) ** 2 + (center_y - y) ** 2
    return square_dist <= radius ** 2





