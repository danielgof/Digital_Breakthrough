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


egrul['Вид деятельности'].unique()


place = '454080, г. Челябинск, п. Мелькомбинат 2 участок 1, д. 37'
location = GoogleV3(api_key="AIzaSyApxlxXIdRM9sWefCgQNHTdCewnxkccb_Q", domain="maps.google.ru").geocode(place)
print(location.address)
print(location.latitude, location.longitude)

data_address = list(egrul['Адрес'])

# долгота и широта адреса
def convert(address):
    location = GoogleV3(api_key="AIzaSyApxlxXIdRM9sWefCgQNHTdCewnxkccb_Q", domain="maps.google.ru").geocode(address)
    return [location.latitude, location.longitude]

coord = convert(data_address[1])

# print(coord)
# print(type(coord))

# долгота и широта адресов преприятий
coordinates = list(map(convert, data_address))

# долгота и широта адресов преприятий в килллометрах
def to_x_and_y(coordinates):
    inProj = Proj(init='epsg:3857')
    outProj = Proj(init='epsg:4326')
    x1, y1 = coordinates[0], coordinates[1]
    x2, y2 = transform(inProj, outProj, x1 ,y1)
    return [x2, y2]


coor_x_y = to_x_and_y(coord)


# coor_x_y = list(map(to_x_and_y, coordinates))


in_circle = []

def detector(coor_x_y, r, data_address):
    square_dist = (coor_x_y[0] - data_address[5][0]) ** 2 + (coor_x_y[1] - data_address[5][1]) ** 2
    if square_dist <= r:
        in_circle.append(data_address[5])



bad_performances = ['обработка металлов', 'обращение с отходами']
bad_performances_in_circle = []

def similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()

sim = similarity(bad_performances[1], data_address[5])
if sim > 0.35:
    bad_performances_in_circle.append(data_address[5])
else:
    pass

reg_factories = list(NVOS['Наименование объекта'])

for elm in bad_performances_in_circle:
    if elm in reg_factories:
        print("Everuthing is all rigth")
    else:
        print("This factory must be checked")


