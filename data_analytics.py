import pandas as pd
import difflib
from pyproj import Proj, transform
from geopy import GoogleV3





class detection:
    def __init__(self, latitude, longitude, r):
        self.latitude = latitude
        self.longitude = longitude
        self.r = r

    """приведение широты и долготы к нормальным координатам"""
    def to_x_and_y(latitude, longitude):
        inProj = Proj(init='epsg:3857')
        outProj = Proj(init='epsg:4326')
        x1, y1 = latitude, longitude
        x2, y2 = transform(inProj, outProj, x1 ,y1)
        return [x2, y2]

    """проверка на нахождение предприятия в выделенном круге, координаты придприятий вязты из колонки с одресами предприятий из таблицы egrul"""
    def detector(x_c, y_c, r, data_address):
        in_circle = []
        for address in data_address:
            square_dist = (x_c - data_address[address][0]) ** 2 + (y_c - data_address[address][1]) ** 2
            if square_dist <= r ** 2:
                in_circle.append(data_address[address])
            else:
                pass
    
    """сравнение двух строк на идентичность, возвращает процент идентичности"""
    def similarity(s1, s2):
        normalized1 = s1.lower()
        normalized2 = s2.lower()
        matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
        return matcher.ratio()
    
    """конвертация строки адреса в долготу и широту, на выходе массив координат"""
    def convert(address):
        location = GoogleV3(api_key="AIzaSyApxlxXIdRM9sWefCgQNHTdCewnxkccb_Q", domain="maps.google.ru").geocode(address)
        return [location.latitude, location.longitude]



test_data = [55.1696515, 61.34494420000001]

test = detection.convert("454080, г. Челябинск, п. Мелькомбинат 2 участок 1, д. 37")

print(test)








# egrul = pd.read_excel("Data/eg.xlsx")
# licence1 = pd.read_excel("Data/licence1.xls")
# licence2 = pd.read_excel("Data/licence2.xls")
# NVOS = pd.read_excel("Data/NVOS.xlsx")
# register_of_licenses = pd.read_excel("Data/register_of_licenses.xlsx")
# reg_pollutant = pd.read_excel("Data/reg_pollutant.xlsx")










# # place = '454080, г. Челябинск, п. Мелькомбинат 2 участок 1, д. 37'
# # location = GoogleV3(api_key="AIzaSyApxlxXIdRM9sWefCgQNHTdCewnxkccb_Q", domain="maps.google.ru").geocode(place)
# # print(location.address)
# # print(location.latitude, location.longitude)

# data_address = list(egrul['Адрес'])

# # долгота и широта адреса
# def convert(address):
#     location = GoogleV3(api_key="AIzaSyApxlxXIdRM9sWefCgQNHTdCewnxkccb_Q", domain="maps.google.ru").geocode(address)
#     return [location.latitude, location.longitude]

# coord = convert(data_address[1])

# # print(coord)
# # print(type(coord))

# # долгота и широта адресов преприятий
# coordinates = list(map(convert, data_address))

# # долгота и широта адресов преприятий в килллометрах
# def to_x_and_y(coordinates):
#     inProj = Proj(init='epsg:3857')
#     outProj = Proj(init='epsg:4326')
#     x1, y1 = coordinates[0], coordinates[1]
#     x2, y2 = transform(inProj, outProj, x1 ,y1)
#     return [x2, y2]


# coor_x_y = to_x_and_y(coord)


# # coor_x_y = list(map(to_x_and_y, coordinates))


# in_circle = []

# def detector(coor_x_y, r, data_address):
#     square_dist = (coor_x_y[0] - data_address[5][0]) ** 2 + (coor_x_y[1] - data_address[5][1]) ** 2
#     if square_dist <= r:
#         in_circle.append(data_address[5])



# bad_performances = ['обработка металлов', 'обращение с отходами']
# bad_performances_in_circle = []

# def similarity(s1, s2):
#     normalized1 = s1.lower()
#     normalized2 = s2.lower()
#     matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
#     return matcher.ratio()

# sim = similarity(bad_performances[1], data_address[5])
# if sim > 0.35:
#     bad_performances_in_circle.append(data_address[5])
# else:
#     pass

# reg_factories = list(NVOS['Наименование объекта'])

# for elm in bad_performances_in_circle:
#     if elm in reg_factories:
#         print("Everuthing is all rigth")
#     else:
#         print("This factory must be checked")

