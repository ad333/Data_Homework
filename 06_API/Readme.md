
# WeatherPy

## Analysis
    
    (1) Cities closest to the equator have highest temperatures, and temperatures 
        start to decrease as we move farther away from the equator.  However, the 
        decrease in maximum temperature is more severe towards positive latitude 
        and less toward negative latitude.
    
    (2) There is no obvious correlation between latitude and cloudiness, wind speed 
        or humidity from my data.
    
    (3) Although cities were randomly selected, there seems some bias that there are 
        more number of cities from the positive latitudes compared to the negative 
        latitudes.


```python
# Import Dependencies
import requests as req
import os
import json
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from citipy import citipy
import time
```


```python
# Declare variables to store list values
lat = []
lon = []
cityname = []
countrycode = []

# Loop through to create 2000 random latidudes and longitudes and append them to list
for x in range(2000):
    lat1 = np.random.uniform(-90, 90)
    lat.append(lat1)
    lon1 = np.random.uniform(-180, 180)
    lon.append(lon1)
    
    # Determine nearest city and country and append them to list
    city = citipy.nearest_city(lat[x], lon[x])
    cityname1 = city.city_name
    cityname.append(cityname1)
    countrycode1 = city.country_code
    countrycode.append(countrycode1)

# Put results into a pandas DataFrame
df = pd.DataFrame({"City":cityname,
                   "Country": countrycode,
                   "Latitude": lat,
                   "Longitude": lon},
                 columns = ["City", "Country", "Latitude", "Longitude"])
# df.head()
```


```python
# Remove any duplicate cities
unique_df = df.drop_duplicates("City", keep = "first")
#len(unique_df)
```


```python
# Specify url and api key
url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "8d1231a477d4bbcd36fe966326717bce"
```


```python
# counter variable
count = 0

#Add columns to store values
unique_df["Date"] = ""
unique_df["Max Temp"] = ""
unique_df["Humidity"] = ""
unique_df["Cloudiness"] = ""
unique_df["Wind_Speed"] = ""
```

    /Users/ad/anaconda3/envs/PythonData/lib/python3.6/site-packages/ipykernel_launcher.py:5: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """
    /Users/ad/anaconda3/envs/PythonData/lib/python3.6/site-packages/ipykernel_launcher.py:6: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    /Users/ad/anaconda3/envs/PythonData/lib/python3.6/site-packages/ipykernel_launcher.py:7: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      import sys
    /Users/ad/anaconda3/envs/PythonData/lib/python3.6/site-packages/ipykernel_launcher.py:8: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    /Users/ad/anaconda3/envs/PythonData/lib/python3.6/site-packages/ipykernel_launcher.py:9: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      if __name__ == '__main__':



```python
# Loop through all query url and print to screen
for index, row in unique_df.iterrows():
    count = count+1
    query_url = url + "appid=" + api_key + "&units=imperial" + "&q=" + row["City"]
    print("Processing City", count, " | ", row["City"])
    print(query_url)
    
    # Get weather data in JSON format
    try:
        weather_data = req.get(query_url)
        weather_data_json = weather_data.json()
        # print(json.dumps(weather_data_json, indent=4, sort_keys=True))
        
        # Add cloudiness, humidity, max temp and wind speed to dataframe
        unique_df.set_value(index, "Date", str(weather_data_json["dt"]))
        unique_df.set_value(index, "Cloudiness", int(weather_data_json["clouds"]["all"]))
        unique_df.set_value(index, "Humidity", int(weather_data_json["main"]["humidity"]))
        unique_df.set_value(index, "Max Temp", int(weather_data_json["main"]["temp_max"]))
        unique_df.set_value(index, "Wind_Speed", int(weather_data_json["wind"]["speed"]))
    
    # Show error message if no data
    except:
        if(unique_df["City"].empty):
            print("There is no data for city", row["City"])

print("----------------------------")
print("Data Retrieval Complete")  
print("----------------------------")
```

    Processing City 1  |  bengkulu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bengkulu
    Processing City 2  |  dana point
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dana point
    Processing City 3  |  mys shmidta
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mys shmidta
    Processing City 4  |  vao
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vao
    Processing City 5  |  busselton
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=busselton
    Processing City 6  |  hirara
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hirara
    Processing City 7  |  qaqortoq
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=qaqortoq
    Processing City 8  |  lebu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lebu
    Processing City 9  |  ruhengeri
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ruhengeri
    Processing City 10  |  vardo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vardo
    Processing City 11  |  longyearbyen
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=longyearbyen
    Processing City 12  |  yumen
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yumen
    Processing City 13  |  vaini
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vaini
    Processing City 14  |  rikitea
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=rikitea
    Processing City 15  |  port alfred
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=port alfred
    Processing City 16  |  illoqqortoormiut
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=illoqqortoormiut
    Processing City 17  |  mogadishu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mogadishu
    Processing City 18  |  nizhneyansk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nizhneyansk
    Processing City 19  |  ushuaia
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ushuaia
    Processing City 20  |  morant bay
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=morant bay
    Processing City 21  |  carnarvon
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=carnarvon
    Processing City 22  |  hermanus
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hermanus
    Processing City 23  |  putina
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=putina
    Processing City 24  |  barentsburg
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=barentsburg
    Processing City 25  |  twentynine palms
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=twentynine palms
    Processing City 26  |  matlock
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=matlock
    Processing City 27  |  thrissur
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=thrissur
    Processing City 28  |  santa rosalia
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=santa rosalia
    Processing City 29  |  panixtlahuaca
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=panixtlahuaca
    Processing City 30  |  rawson
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=rawson
    Processing City 31  |  bredasdorp
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bredasdorp
    Processing City 32  |  keti bandar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=keti bandar
    Processing City 33  |  blagoyevo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=blagoyevo
    Processing City 34  |  ciudad bolivar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ciudad bolivar
    Processing City 35  |  nanortalik
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nanortalik
    Processing City 36  |  roma
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=roma
    Processing City 37  |  marcona
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=marcona
    Processing City 38  |  mar del plata
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mar del plata
    Processing City 39  |  roebourne
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=roebourne
    Processing City 40  |  grand centre
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=grand centre
    Processing City 41  |  punta arenas
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=punta arenas
    Processing City 42  |  sorvag
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sorvag
    Processing City 43  |  upernavik
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=upernavik
    Processing City 44  |  severo-kurilsk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=severo-kurilsk
    Processing City 45  |  shihezi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=shihezi
    Processing City 46  |  atuona
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=atuona
    Processing City 47  |  qaanaaq
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=qaanaaq
    Processing City 48  |  cape town
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=cape town
    Processing City 49  |  hithadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hithadhoo
    Processing City 50  |  ribeira grande
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ribeira grande
    Processing City 51  |  belushya guba
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=belushya guba
    Processing City 52  |  matagami
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=matagami
    Processing City 53  |  albany
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=albany
    Processing City 54  |  mahina
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mahina
    Processing City 55  |  conde
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=conde
    Processing City 56  |  kelso
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kelso
    Processing City 57  |  hobart
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hobart
    Processing City 58  |  mazyr
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mazyr
    Processing City 59  |  bluff
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bluff
    Processing City 60  |  mataura
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mataura
    Processing City 61  |  chernyy yar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=chernyy yar
    Processing City 62  |  vagur
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vagur
    Processing City 63  |  bandarbeyla
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bandarbeyla
    Processing City 64  |  tsihombe
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tsihombe
    Processing City 65  |  zhigansk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=zhigansk
    Processing City 66  |  tasiilaq
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tasiilaq
    Processing City 67  |  castro
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=castro
    Processing City 68  |  saint george
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=saint george
    Processing City 69  |  dikson
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dikson
    Processing City 70  |  kashi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kashi
    Processing City 71  |  lompoc
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lompoc
    Processing City 72  |  jamestown
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=jamestown
    Processing City 73  |  sao joao da barra
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sao joao da barra
    Processing City 74  |  chubbuck
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=chubbuck
    Processing City 75  |  college
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=college
    Processing City 76  |  saint-augustin
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=saint-augustin
    Processing City 77  |  natal
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=natal
    Processing City 78  |  burayevo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=burayevo
    Processing City 79  |  faanui
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=faanui
    Processing City 80  |  avarua
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=avarua
    Processing City 81  |  mahibadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mahibadhoo
    Processing City 82  |  akyab
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=akyab
    Processing City 83  |  marsaxlokk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=marsaxlokk
    Processing City 84  |  arman
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=arman
    Processing City 85  |  weligama
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=weligama
    Processing City 86  |  puerto ayora
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=puerto ayora
    Processing City 87  |  vila velha
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vila velha
    Processing City 88  |  taolanaro
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=taolanaro
    Processing City 89  |  obidos
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=obidos
    Processing City 90  |  paracatu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=paracatu
    Processing City 91  |  yerbogachen
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yerbogachen
    Processing City 92  |  leningradskiy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=leningradskiy
    Processing City 93  |  calafell
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=calafell
    Processing City 94  |  fortuna
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=fortuna
    Processing City 95  |  nelson bay
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nelson bay
    Processing City 96  |  haines junction
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=haines junction
    Processing City 97  |  sokoni
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sokoni
    Processing City 98  |  pacureti
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=pacureti
    Processing City 99  |  victoria
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=victoria
    Processing City 100  |  zhitikara
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=zhitikara
    Processing City 101  |  klaksvik
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=klaksvik
    Processing City 102  |  khatanga
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=khatanga
    Processing City 103  |  khromtau
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=khromtau
    Processing City 104  |  bethel
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bethel
    Processing City 105  |  flin flon
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=flin flon
    Processing City 106  |  beringovskiy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=beringovskiy
    Processing City 107  |  raudeberg
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=raudeberg
    Processing City 108  |  alice springs
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=alice springs
    Processing City 109  |  mahebourg
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mahebourg
    Processing City 110  |  sao filipe
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sao filipe
    Processing City 111  |  aklavik
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=aklavik
    Processing City 112  |  menomonie
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=menomonie
    Processing City 113  |  kununurra
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kununurra
    Processing City 114  |  asau
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=asau
    Processing City 115  |  narsaq
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=narsaq
    Processing City 116  |  barmer
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=barmer
    Processing City 117  |  boende
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=boende
    Processing City 118  |  bathsheba
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bathsheba
    Processing City 119  |  tabialan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tabialan
    Processing City 120  |  dhidhdhoo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dhidhdhoo
    Processing City 121  |  ponta do sol
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ponta do sol
    Processing City 122  |  half moon bay
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=half moon bay
    Processing City 123  |  mandalgovi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mandalgovi
    Processing City 124  |  himora
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=himora
    Processing City 125  |  grindavik
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=grindavik
    Processing City 126  |  hilo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hilo
    Processing City 127  |  saint anthony
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=saint anthony
    Processing City 128  |  cidreira
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=cidreira
    Processing City 129  |  birjand
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=birjand
    Processing City 130  |  sayyan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sayyan
    Processing City 131  |  ubaitaba
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ubaitaba
    Processing City 132  |  kapaa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kapaa
    Processing City 133  |  gizo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=gizo
    Processing City 134  |  general pico
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=general pico
    Processing City 135  |  diamantino
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=diamantino
    Processing City 136  |  mangrol
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mangrol
    Processing City 137  |  anahuac
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=anahuac
    Processing City 138  |  kudahuvadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kudahuvadhoo
    Processing City 139  |  oriximina
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=oriximina
    Processing City 140  |  jiexiu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=jiexiu
    Processing City 141  |  port elizabeth
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=port elizabeth
    Processing City 142  |  new norfolk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=new norfolk
    Processing City 143  |  kavieng
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kavieng
    Processing City 144  |  huilong
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=huilong
    Processing City 145  |  one hundred mile house
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=one hundred mile house
    Processing City 146  |  christchurch
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=christchurch
    Processing City 147  |  saint-philippe
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=saint-philippe
    Processing City 148  |  taloqan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=taloqan
    Processing City 149  |  isangel
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=isangel
    Processing City 150  |  louisbourg
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=louisbourg
    Processing City 151  |  matamoros
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=matamoros
    Processing City 152  |  mahajanga
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mahajanga
    Processing City 153  |  tamandare
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tamandare
    Processing City 154  |  wageningen
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=wageningen
    Processing City 155  |  tura
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tura
    Processing City 156  |  nikolskoye
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nikolskoye
    Processing City 157  |  beyneu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=beyneu
    Processing City 158  |  san jose
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=san jose
    Processing City 159  |  yellowknife
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yellowknife
    Processing City 160  |  verkhneuralsk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=verkhneuralsk
    Processing City 161  |  okha
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=okha
    Processing City 162  |  kunming
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kunming
    Processing City 163  |  praia da vitoria
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=praia da vitoria
    Processing City 164  |  beidao
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=beidao
    Processing City 165  |  brigantine
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=brigantine
    Processing City 166  |  olinda
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=olinda
    Processing City 167  |  chipinge
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=chipinge
    Processing City 168  |  richards bay
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=richards bay
    Processing City 169  |  tautira
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tautira
    Processing City 170  |  ngukurr
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ngukurr
    Processing City 171  |  olafsvik
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=olafsvik
    Processing City 172  |  mengcheng
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mengcheng
    Processing City 173  |  viedma
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=viedma
    Processing City 174  |  songea
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=songea
    Processing City 175  |  chokurdakh
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=chokurdakh
    Processing City 176  |  lorengau
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lorengau
    Processing City 177  |  namibe
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=namibe
    Processing City 178  |  birao
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=birao
    Processing City 179  |  vale da amoreira
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vale da amoreira
    Processing City 180  |  puerto madryn
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=puerto madryn
    Processing City 181  |  jiazi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=jiazi
    Processing City 182  |  amderma
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=amderma
    Processing City 183  |  nouadhibou
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nouadhibou
    Processing City 184  |  bay roberts
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bay roberts
    Processing City 185  |  neryungri
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=neryungri
    Processing City 186  |  butaritari
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=butaritari
    Processing City 187  |  faya
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=faya
    Processing City 188  |  kita
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kita
    Processing City 189  |  marquette
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=marquette
    Processing City 190  |  la ronge
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=la ronge
    Processing City 191  |  bolobo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bolobo
    Processing City 192  |  komsomolskiy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=komsomolskiy
    Processing City 193  |  chimbote
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=chimbote
    Processing City 194  |  jinchengjiang
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=jinchengjiang
    Processing City 195  |  vestmannaeyjar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vestmannaeyjar
    Processing City 196  |  lodja
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lodja
    Processing City 197  |  rosario do sul
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=rosario do sul
    Processing City 198  |  inirida
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=inirida
    Processing City 199  |  kutum
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kutum
    Processing City 200  |  lobatse
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lobatse
    Processing City 201  |  barra do corda
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=barra do corda
    Processing City 202  |  san patricio
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=san patricio
    Processing City 203  |  sao gabriel da cachoeira
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sao gabriel da cachoeira
    Processing City 204  |  pevek
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=pevek
    Processing City 205  |  maimon
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=maimon
    Processing City 206  |  ilulissat
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ilulissat
    Processing City 207  |  chuy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=chuy
    Processing City 208  |  clyde river
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=clyde river
    Processing City 209  |  krasnoselkup
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=krasnoselkup
    Processing City 210  |  hamilton
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hamilton
    Processing City 211  |  avera
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=avera
    Processing City 212  |  saskylakh
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=saskylakh
    Processing City 213  |  samusu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=samusu
    Processing City 214  |  kem
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kem
    Processing City 215  |  kupang
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kupang
    Processing City 216  |  noumea
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=noumea
    Processing City 217  |  mullaitivu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mullaitivu
    Processing City 218  |  luderitz
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=luderitz
    Processing City 219  |  vallenar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vallenar
    Processing City 220  |  sambava
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sambava
    Processing City 221  |  ijaki
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ijaki
    Processing City 222  |  barrow
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=barrow
    Processing City 223  |  saint marys
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=saint marys
    Processing City 224  |  poum
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=poum
    Processing City 225  |  arraial do cabo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=arraial do cabo
    Processing City 226  |  santa marta
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=santa marta
    Processing City 227  |  nchelenge
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nchelenge
    Processing City 228  |  trinidad
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=trinidad
    Processing City 229  |  celestun
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=celestun
    Processing City 230  |  garwa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=garwa
    Processing City 231  |  thompson
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=thompson
    Processing City 232  |  puerto colombia
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=puerto colombia
    Processing City 233  |  adrar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=adrar
    Processing City 234  |  tumannyy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tumannyy
    Processing City 235  |  vologda
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vologda
    Processing City 236  |  westlock
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=westlock
    Processing City 237  |  hammerfest
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hammerfest
    Processing City 238  |  grand river south east
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=grand river south east
    Processing City 239  |  kahului
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kahului
    Processing City 240  |  tiksi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tiksi
    Processing City 241  |  ontario
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ontario
    Processing City 242  |  gelemso
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=gelemso
    Processing City 243  |  jacareacanga
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=jacareacanga
    Processing City 244  |  provideniya
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=provideniya
    Processing City 245  |  dwarka
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dwarka
    Processing City 246  |  qovlar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=qovlar
    Processing City 247  |  nantucket
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nantucket
    Processing City 248  |  skoghall
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=skoghall
    Processing City 249  |  sapao
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sapao
    Processing City 250  |  touros
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=touros
    Processing City 251  |  dalvik
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dalvik
    Processing City 252  |  bambous virieux
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bambous virieux
    Processing City 253  |  cherskiy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=cherskiy
    Processing City 254  |  thaba-tseka
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=thaba-tseka
    Processing City 255  |  shelburne
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=shelburne
    Processing City 256  |  baruun-urt
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=baruun-urt
    Processing City 257  |  flinders
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=flinders
    Processing City 258  |  shimoda
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=shimoda
    Processing City 259  |  cayenne
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=cayenne
    Processing City 260  |  kodiak
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kodiak
    Processing City 261  |  suntar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=suntar
    Processing City 262  |  torbay
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=torbay
    Processing City 263  |  bull savanna
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bull savanna
    Processing City 264  |  inderborskiy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=inderborskiy
    Processing City 265  |  cabatuan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=cabatuan
    Processing City 266  |  sao paulo de olivenca
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sao paulo de olivenca
    Processing City 267  |  sorland
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sorland
    Processing City 268  |  bilibino
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bilibino
    Processing City 269  |  hervey bay
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hervey bay
    Processing City 270  |  quatre cocos
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=quatre cocos
    Processing City 271  |  bud
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bud
    Processing City 272  |  grafton
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=grafton
    Processing City 273  |  jieznas
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=jieznas
    Processing City 274  |  turukhansk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=turukhansk
    Processing City 275  |  xinzhi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=xinzhi
    Processing City 276  |  guerrero negro
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=guerrero negro
    Processing City 277  |  arlit
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=arlit
    Processing City 278  |  luxor
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=luxor
    Processing City 279  |  salalah
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=salalah
    Processing City 280  |  georgetown
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=georgetown
    Processing City 281  |  iqaluit
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=iqaluit
    Processing City 282  |  ajdabiya
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ajdabiya
    Processing City 283  |  abbeville
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=abbeville
    Processing City 284  |  nadym
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nadym
    Processing City 285  |  broome
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=broome
    Processing City 286  |  hvide sande
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hvide sande
    Processing City 287  |  florence
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=florence
    Processing City 288  |  portland
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=portland
    Processing City 289  |  bela vista
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bela vista
    Processing City 290  |  kuching
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kuching
    Processing City 291  |  safford
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=safford
    Processing City 292  |  banda aceh
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=banda aceh
    Processing City 293  |  manokwari
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=manokwari
    Processing City 294  |  esperance
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=esperance
    Processing City 295  |  tuy hoa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tuy hoa
    Processing City 296  |  santiago del estero
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=santiago del estero
    Processing City 297  |  mayumba
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mayumba
    Processing City 298  |  gemena
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=gemena
    Processing City 299  |  codrington
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=codrington
    Processing City 300  |  rundu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=rundu
    Processing City 301  |  ust-nera
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ust-nera
    Processing City 302  |  nakhon thai
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nakhon thai
    Processing City 303  |  hasaki
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hasaki
    Processing City 304  |  tilichiki
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tilichiki
    Processing City 305  |  wulanhaote
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=wulanhaote
    Processing City 306  |  toliary
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=toliary
    Processing City 307  |  kismayo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kismayo
    Processing City 308  |  cadillac
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=cadillac
    Processing City 309  |  tokonou
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tokonou
    Processing City 310  |  quelimane
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=quelimane
    Processing City 311  |  kruisfontein
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kruisfontein
    Processing City 312  |  kristianstad
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kristianstad
    Processing City 313  |  waipawa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=waipawa
    Processing City 314  |  turtkul
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=turtkul
    Processing City 315  |  fare
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=fare
    Processing City 316  |  sahrak
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sahrak
    Processing City 317  |  bardiyah
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bardiyah
    Processing City 318  |  baykit
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=baykit
    Processing City 319  |  san jose de guanipa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=san jose de guanipa
    Processing City 320  |  palabuhanratu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=palabuhanratu
    Processing City 321  |  karratha
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=karratha
    Processing City 322  |  tooele
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tooele
    Processing City 323  |  tazovskiy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tazovskiy
    Processing City 324  |  gore
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=gore
    Processing City 325  |  bahia honda
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bahia honda
    Processing City 326  |  port lincoln
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=port lincoln
    Processing City 327  |  caravelas
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=caravelas
    Processing City 328  |  lagoa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lagoa
    Processing City 329  |  batagay-alyta
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=batagay-alyta
    Processing City 330  |  sangar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sangar
    Processing City 331  |  coquimbo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=coquimbo
    Processing City 332  |  dickinson
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dickinson
    Processing City 333  |  havre-saint-pierre
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=havre-saint-pierre
    Processing City 334  |  mao
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mao
    Processing City 335  |  carlagan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=carlagan
    Processing City 336  |  erzin
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=erzin
    Processing City 337  |  angoche
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=angoche
    Processing City 338  |  victoria point
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=victoria point
    Processing City 339  |  seoul
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=seoul
    Processing City 340  |  yunjinghong
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yunjinghong
    Processing City 341  |  vanimo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vanimo
    Processing City 342  |  umzimvubu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=umzimvubu
    Processing City 343  |  yarumal
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yarumal
    Processing City 344  |  carballo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=carballo
    Processing City 345  |  henties bay
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=henties bay
    Processing City 346  |  yanan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yanan
    Processing City 347  |  penzance
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=penzance
    Processing City 348  |  praia
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=praia
    Processing City 349  |  obihiro
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=obihiro
    Processing City 350  |  tuktoyaktuk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tuktoyaktuk
    Processing City 351  |  blackburn
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=blackburn
    Processing City 352  |  dingle
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dingle
    Processing City 353  |  bayji
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bayji
    Processing City 354  |  hatillo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hatillo
    Processing City 355  |  bagotville
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bagotville
    Processing City 356  |  attawapiskat
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=attawapiskat
    Processing City 357  |  palmer
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=palmer
    Processing City 358  |  livingston
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=livingston
    Processing City 359  |  yuzhou
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yuzhou
    Processing City 360  |  sioux lookout
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sioux lookout
    Processing City 361  |  bayan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bayan
    Processing City 362  |  wanning
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=wanning
    Processing City 363  |  ancud
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ancud
    Processing City 364  |  sept-iles
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sept-iles
    Processing City 365  |  kayes
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kayes
    Processing City 366  |  hofn
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hofn
    Processing City 367  |  buala
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=buala
    Processing City 368  |  coracora
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=coracora
    Processing City 369  |  manaure
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=manaure
    Processing City 370  |  ha giang
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ha giang
    Processing City 371  |  foggia
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=foggia
    Processing City 372  |  santa maria
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=santa maria
    Processing City 373  |  walvis bay
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=walvis bay
    Processing City 374  |  east london
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=east london
    Processing City 375  |  harlingen
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=harlingen
    Processing City 376  |  piacabucu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=piacabucu
    Processing City 377  |  xining
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=xining
    Processing City 378  |  bosilegrad
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bosilegrad
    Processing City 379  |  esso
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=esso
    Processing City 380  |  anadyr
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=anadyr
    Processing City 381  |  satitoa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=satitoa
    Processing City 382  |  mount isa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mount isa
    Processing City 383  |  chara
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=chara
    Processing City 384  |  norman wells
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=norman wells
    Processing City 385  |  shingu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=shingu
    Processing City 386  |  bridlington
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bridlington
    Processing City 387  |  ponta delgada
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ponta delgada
    Processing City 388  |  muroto
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=muroto
    Processing City 389  |  karlskrona
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=karlskrona
    Processing City 390  |  port hedland
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=port hedland
    Processing City 391  |  teahupoo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=teahupoo
    Processing City 392  |  mackenzie
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mackenzie
    Processing City 393  |  ankazobe
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ankazobe
    Processing City 394  |  belyy yar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=belyy yar
    Processing City 395  |  noshiro
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=noshiro
    Processing City 396  |  sur
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sur
    Processing City 397  |  vila
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vila
    Processing City 398  |  vila do maio
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vila do maio
    Processing City 399  |  nizhniy kuranakh
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nizhniy kuranakh
    Processing City 400  |  zabol
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=zabol
    Processing City 401  |  george
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=george
    Processing City 402  |  sentyabrskiy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sentyabrskiy
    Processing City 403  |  rakai
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=rakai
    Processing City 404  |  saldanha
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=saldanha
    Processing City 405  |  sabang
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sabang
    Processing City 406  |  dryden
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dryden
    Processing City 407  |  khasan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=khasan
    Processing City 408  |  road town
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=road town
    Processing City 409  |  panacan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=panacan
    Processing City 410  |  dzhebariki-khaya
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dzhebariki-khaya
    Processing City 411  |  sakakah
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sakakah
    Processing City 412  |  san clemente
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=san clemente
    Processing City 413  |  rapu-rapu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=rapu-rapu
    Processing City 414  |  coihaique
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=coihaique
    Processing City 415  |  chapais
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=chapais
    Processing City 416  |  kalamazoo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kalamazoo
    Processing City 417  |  kondinskoye
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kondinskoye
    Processing City 418  |  vaitupu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vaitupu
    Processing City 419  |  myjava
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=myjava
    Processing City 420  |  victor harbor
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=victor harbor
    Processing City 421  |  puerto madero
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=puerto madero
    Processing City 422  |  talnakh
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=talnakh
    Processing City 423  |  opuwo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=opuwo
    Processing City 424  |  te anau
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=te anau
    Processing City 425  |  berlevag
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=berlevag
    Processing City 426  |  ola
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ola
    Processing City 427  |  nicoya
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nicoya
    Processing City 428  |  ascension
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ascension
    Processing City 429  |  geraldton
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=geraldton
    Processing City 430  |  pangnirtung
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=pangnirtung
    Processing City 431  |  okhotsk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=okhotsk
    Processing City 432  |  margate
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=margate
    Processing City 433  |  tanout
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tanout
    Processing City 434  |  vila franca do campo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vila franca do campo
    Processing City 435  |  katsuura
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=katsuura
    Processing City 436  |  nishihara
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nishihara
    Processing City 437  |  lalibela
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lalibela
    Processing City 438  |  maloshuyka
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=maloshuyka
    Processing City 439  |  meulaboh
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=meulaboh
    Processing City 440  |  nabire
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nabire
    Processing City 441  |  ati
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ati
    Processing City 442  |  hambantota
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hambantota
    Processing City 443  |  babanusah
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=babanusah
    Processing City 444  |  rio de janeiro
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=rio de janeiro
    Processing City 445  |  kattivakkam
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kattivakkam
    Processing City 446  |  altagracia de orituco
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=altagracia de orituco
    Processing City 447  |  pasni
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=pasni
    Processing City 448  |  kavaratti
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kavaratti
    Processing City 449  |  lake havasu city
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lake havasu city
    Processing City 450  |  coos bay
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=coos bay
    Processing City 451  |  erenhot
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=erenhot
    Processing City 452  |  kaseda
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kaseda
    Processing City 453  |  los llanos de aridane
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=los llanos de aridane
    Processing City 454  |  kankon
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kankon
    Processing City 455  |  cabo san lucas
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=cabo san lucas
    Processing City 456  |  dudinka
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dudinka
    Processing City 457  |  versalles
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=versalles
    Processing City 458  |  khudumelapye
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=khudumelapye
    Processing City 459  |  santa clara
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=santa clara
    Processing City 460  |  atambua
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=atambua
    Processing City 461  |  nur
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nur
    Processing City 462  |  benguela
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=benguela
    Processing City 463  |  puerto del rosario
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=puerto del rosario
    Processing City 464  |  ust-kulom
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ust-kulom
    Processing City 465  |  omsukchan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=omsukchan
    Processing City 466  |  boguchany
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=boguchany
    Processing City 467  |  grand-santi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=grand-santi
    Processing City 468  |  shirgaon
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=shirgaon
    Processing City 469  |  souillac
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=souillac
    Processing City 470  |  ossora
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ossora
    Processing City 471  |  bataraza
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bataraza
    Processing City 472  |  pahrump
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=pahrump
    Processing City 473  |  cartagena
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=cartagena
    Processing City 474  |  mount gambier
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mount gambier
    Processing City 475  |  tabuny
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tabuny
    Processing City 476  |  taoudenni
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=taoudenni
    Processing City 477  |  naze
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=naze
    Processing City 478  |  yulara
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yulara
    Processing City 479  |  sandviken
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sandviken
    Processing City 480  |  ixtapa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ixtapa
    Processing City 481  |  ostrovnoy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ostrovnoy
    Processing City 482  |  daund
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=daund
    Processing City 483  |  skibbereen
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=skibbereen
    Processing City 484  |  byumba
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=byumba
    Processing City 485  |  acapulco
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=acapulco
    Processing City 486  |  kieta
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kieta
    Processing City 487  |  wundanyi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=wundanyi
    Processing City 488  |  bentiu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bentiu
    Processing City 489  |  khilok
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=khilok
    Processing City 490  |  emerald
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=emerald
    Processing City 491  |  fairbanks
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=fairbanks
    Processing City 492  |  nhulunbuy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nhulunbuy
    Processing City 493  |  tonantins
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tonantins
    Processing City 494  |  saint-paul
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=saint-paul
    Processing City 495  |  copiapo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=copiapo
    Processing City 496  |  nortelandia
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nortelandia
    Processing City 497  |  porto walter
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=porto walter
    Processing City 498  |  kysyl-syr
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kysyl-syr
    Processing City 499  |  waingapu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=waingapu
    Processing City 500  |  guicheng
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=guicheng
    Processing City 501  |  nome
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nome
    Processing City 502  |  rong kwang
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=rong kwang
    Processing City 503  |  novoagansk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=novoagansk
    Processing City 504  |  stepnogorsk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=stepnogorsk
    Processing City 505  |  linhares
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=linhares
    Processing City 506  |  sento se
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sento se
    Processing City 507  |  alofi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=alofi
    Processing City 508  |  phan rang
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=phan rang
    Processing City 509  |  rungata
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=rungata
    Processing City 510  |  gat
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=gat
    Processing City 511  |  ntungamo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ntungamo
    Processing City 512  |  smithers
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=smithers
    Processing City 513  |  douentza
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=douentza
    Processing City 514  |  trani
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=trani
    Processing City 515  |  yeniseysk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yeniseysk
    Processing City 516  |  dunedin
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dunedin
    Processing City 517  |  nyanguge
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nyanguge
    Processing City 518  |  wahiawa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=wahiawa
    Processing City 519  |  duz
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=duz
    Processing City 520  |  mafeteng
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mafeteng
    Processing City 521  |  northam
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=northam
    Processing City 522  |  mayskiy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mayskiy
    Processing City 523  |  fort nelson
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=fort nelson
    Processing City 524  |  morgan city
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=morgan city
    Processing City 525  |  samarai
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=samarai
    Processing City 526  |  kawalu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kawalu
    Processing City 527  |  mikropolis
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mikropolis
    Processing City 528  |  toora-khem
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=toora-khem
    Processing City 529  |  marau
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=marau
    Processing City 530  |  padang
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=padang
    Processing City 531  |  cockburn town
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=cockburn town
    Processing City 532  |  urusha
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=urusha
    Processing City 533  |  tabiauea
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tabiauea
    Processing City 534  |  panzhihua
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=panzhihua
    Processing City 535  |  roald
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=roald
    Processing City 536  |  bubaque
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bubaque
    Processing City 537  |  kabanjahe
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kabanjahe
    Processing City 538  |  altar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=altar
    Processing City 539  |  zinder
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=zinder
    Processing City 540  |  lecce
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lecce
    Processing City 541  |  davila
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=davila
    Processing City 542  |  klyuchi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=klyuchi
    Processing City 543  |  pokhara
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=pokhara
    Processing City 544  |  maghama
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=maghama
    Processing City 545  |  belem
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=belem
    Processing City 546  |  comodoro rivadavia
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=comodoro rivadavia
    Processing City 547  |  hami
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hami
    Processing City 548  |  sisimiut
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sisimiut
    Processing City 549  |  san rafael
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=san rafael
    Processing City 550  |  son la
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=son la
    Processing City 551  |  airai
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=airai
    Processing City 552  |  meyungs
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=meyungs
    Processing City 553  |  tromso
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tromso
    Processing City 554  |  shubarshi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=shubarshi
    Processing City 555  |  barcarena
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=barcarena
    Processing City 556  |  santa rosa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=santa rosa
    Processing City 557  |  pachino
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=pachino
    Processing City 558  |  hauterive
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hauterive
    Processing City 559  |  plock
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=plock
    Processing City 560  |  houma
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=houma
    Processing City 561  |  otanche
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=otanche
    Processing City 562  |  laguna
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=laguna
    Processing City 563  |  arzgir
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=arzgir
    Processing City 564  |  bilma
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bilma
    Processing City 565  |  casper
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=casper
    Processing City 566  |  thinadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=thinadhoo
    Processing City 567  |  sulangan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sulangan
    Processing City 568  |  monte patria
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=monte patria
    Processing City 569  |  inhambane
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=inhambane
    Processing City 570  |  ambon
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ambon
    Processing City 571  |  toungoo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=toungoo
    Processing City 572  |  mitsamiouli
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mitsamiouli
    Processing City 573  |  dien bien
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=dien bien
    Processing City 574  |  khatassy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=khatassy
    Processing City 575  |  mongo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mongo
    Processing City 576  |  masvingo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=masvingo
    Processing City 577  |  maceio
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=maceio
    Processing City 578  |  hearst
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hearst
    Processing City 579  |  hamcearca
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hamcearca
    Processing City 580  |  alihe
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=alihe
    Processing City 581  |  lavrentiya
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lavrentiya
    Processing City 582  |  mahadday weyne
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mahadday weyne
    Processing City 583  |  yendi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yendi
    Processing City 584  |  goderich
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=goderich
    Processing City 585  |  kilcoole
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kilcoole
    Processing City 586  |  atchison
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=atchison
    Processing City 587  |  mindelo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mindelo
    Processing City 588  |  eyl
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=eyl
    Processing City 589  |  doha
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=doha
    Processing City 590  |  umm lajj
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=umm lajj
    Processing City 591  |  laishevo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=laishevo
    Processing City 592  |  nemuro
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nemuro
    Processing City 593  |  hobyo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hobyo
    Processing City 594  |  the valley
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=the valley
    Processing City 595  |  namatanai
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=namatanai
    Processing City 596  |  mayor pablo lagerenza
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mayor pablo lagerenza
    Processing City 597  |  botshabelo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=botshabelo
    Processing City 598  |  kaupanger
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kaupanger
    Processing City 599  |  sobolevo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sobolevo
    Processing City 600  |  kenai
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kenai
    Processing City 601  |  shitanjing
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=shitanjing
    Processing City 602  |  corner brook
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=corner brook
    Processing City 603  |  gangawati
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=gangawati
    Processing City 604  |  krasnyy chikoy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=krasnyy chikoy
    Processing City 605  |  turayf
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=turayf
    Processing City 606  |  gillette
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=gillette
    Processing City 607  |  wilmington
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=wilmington
    Processing City 608  |  lima
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lima
    Processing City 609  |  pisco
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=pisco
    Processing City 610  |  ordubad
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ordubad
    Processing City 611  |  vestmanna
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vestmanna
    Processing City 612  |  slavsk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=slavsk
    Processing City 613  |  mutoko
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mutoko
    Processing City 614  |  kitimat
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kitimat
    Processing City 615  |  husavik
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=husavik
    Processing City 616  |  san jeronimo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=san jeronimo
    Processing City 617  |  hit
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hit
    Processing City 618  |  constitucion
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=constitucion
    Processing City 619  |  eldikan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=eldikan
    Processing City 620  |  valparaiso
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=valparaiso
    Processing City 621  |  yuzhno-yeniseyskiy
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yuzhno-yeniseyskiy
    Processing City 622  |  beinamar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=beinamar
    Processing City 623  |  moree
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=moree
    Processing City 624  |  verkhoyansk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=verkhoyansk
    Processing City 625  |  santo domingo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=santo domingo
    Processing City 626  |  hualmay
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hualmay
    Processing City 627  |  batsfjord
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=batsfjord
    Processing City 628  |  kirkland lake
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kirkland lake
    Processing City 629  |  sinkat
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sinkat
    Processing City 630  |  utiroa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=utiroa
    Processing City 631  |  stropkov
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=stropkov
    Processing City 632  |  kazachinskoye
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kazachinskoye
    Processing City 633  |  los barrios
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=los barrios
    Processing City 634  |  xiangfan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=xiangfan
    Processing City 635  |  homer
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=homer
    Processing City 636  |  nyagan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nyagan
    Processing City 637  |  auki
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=auki
    Processing City 638  |  sebinkarahisar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sebinkarahisar
    Processing City 639  |  wagar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=wagar
    Processing City 640  |  luangwa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=luangwa
    Processing City 641  |  fez
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=fez
    Processing City 642  |  along
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=along
    Processing City 643  |  parczew
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=parczew
    Processing City 644  |  ziro
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ziro
    Processing City 645  |  san cristobal
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=san cristobal
    Processing City 646  |  xai-xai
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=xai-xai
    Processing City 647  |  bhuj
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bhuj
    Processing City 648  |  charters towers
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=charters towers
    Processing City 649  |  guaruja
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=guaruja
    Processing City 650  |  gushikawa
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=gushikawa
    Processing City 651  |  mayo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mayo
    Processing City 652  |  mogochin
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mogochin
    Processing City 653  |  slawno
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=slawno
    Processing City 654  |  manggar
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=manggar
    Processing City 655  |  kidal
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kidal
    Processing City 656  |  alta floresta
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=alta floresta
    Processing City 657  |  hohhot
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hohhot
    Processing City 658  |  lata
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lata
    Processing City 659  |  maningrida
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=maningrida
    Processing City 660  |  benevento
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=benevento
    Processing City 661  |  codajas
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=codajas
    Processing City 662  |  ranong
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ranong
    Processing City 663  |  laiyang
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=laiyang
    Processing City 664  |  lolua
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lolua
    Processing City 665  |  launceston
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=launceston
    Processing City 666  |  kushima
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kushima
    Processing City 667  |  oistins
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=oistins
    Processing City 668  |  sao luis do quitunde
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sao luis do quitunde
    Processing City 669  |  billings
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=billings
    Processing City 670  |  yar-sale
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=yar-sale
    Processing City 671  |  sayan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sayan
    Processing City 672  |  salisbury
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=salisbury
    Processing City 673  |  fukue
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=fukue
    Processing City 674  |  karaton
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=karaton
    Processing City 675  |  mehamn
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mehamn
    Processing City 676  |  waddan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=waddan
    Processing City 677  |  snezhnogorsk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=snezhnogorsk
    Processing City 678  |  caucaia
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=caucaia
    Processing City 679  |  sao jose da coroa grande
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sao jose da coroa grande
    Processing City 680  |  hov
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=hov
    Processing City 681  |  okahandja
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=okahandja
    Processing City 682  |  fuerte olimpo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=fuerte olimpo
    Processing City 683  |  malartic
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=malartic
    Processing City 684  |  pochutla
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=pochutla
    Processing City 685  |  ouranopolis
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=ouranopolis
    Processing City 686  |  morehead
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=morehead
    Processing City 687  |  high level
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=high level
    Processing City 688  |  bargal
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bargal
    Processing City 689  |  paamiut
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=paamiut
    Processing City 690  |  thessalon
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=thessalon
    Processing City 691  |  rocha
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=rocha
    Processing City 692  |  tigil
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tigil
    Processing City 693  |  nuuk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nuuk
    Processing City 694  |  jacqueville
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=jacqueville
    Processing City 695  |  karpogory
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=karpogory
    Processing City 696  |  rio gallegos
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=rio gallegos
    Processing City 697  |  saint-francois
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=saint-francois
    Processing City 698  |  tondano
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tondano
    Processing City 699  |  shinpokh
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=shinpokh
    Processing City 700  |  mudgee
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mudgee
    Processing City 701  |  kloulklubed
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kloulklubed
    Processing City 702  |  kamenskoye
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kamenskoye
    Processing City 703  |  qazigund
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=qazigund
    Processing City 704  |  vanavara
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vanavara
    Processing City 705  |  felidhoo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=felidhoo
    Processing City 706  |  qiongshan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=qiongshan
    Processing City 707  |  arinos
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=arinos
    Processing City 708  |  marzuq
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=marzuq
    Processing City 709  |  candido de abreu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=candido de abreu
    Processing City 710  |  honningsvag
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=honningsvag
    Processing City 711  |  bali chak
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bali chak
    Processing City 712  |  cururupu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=cururupu
    Processing City 713  |  theologos
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=theologos
    Processing City 714  |  tubuala
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tubuala
    Processing City 715  |  puerto maldonado
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=puerto maldonado
    Processing City 716  |  bhikhi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=bhikhi
    Processing City 717  |  zyryanka
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=zyryanka
    Processing City 718  |  donskoye
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=donskoye
    Processing City 719  |  falealupo
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=falealupo
    Processing City 720  |  galesong
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=galesong
    Processing City 721  |  kegayli
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kegayli
    Processing City 722  |  tabou
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tabou
    Processing City 723  |  taihe
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=taihe
    Processing City 724  |  salcininkai
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=salcininkai
    Processing City 725  |  grand gaube
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=grand gaube
    Processing City 726  |  labutta
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=labutta
    Processing City 727  |  haibowan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=haibowan
    Processing City 728  |  mizpe ramon
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mizpe ramon
    Processing City 729  |  kailua
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kailua
    Processing City 730  |  port-cartier
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=port-cartier
    Processing City 731  |  belem de sao francisco
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=belem de sao francisco
    Processing City 732  |  inuvik
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=inuvik
    Processing City 733  |  takoradi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=takoradi
    Processing City 734  |  valleyview
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=valleyview
    Processing City 735  |  lamu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lamu
    Processing City 736  |  maua
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=maua
    Processing City 737  |  aswan
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=aswan
    Processing City 738  |  mackay
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mackay
    Processing City 739  |  lundin links
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=lundin links
    Processing City 740  |  tisovec
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=tisovec
    Processing City 741  |  sibu
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sibu
    Processing City 742  |  necochea
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=necochea
    Processing City 743  |  vicosa do ceara
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=vicosa do ceara
    Processing City 744  |  puksoozero
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=puksoozero
    Processing City 745  |  mujiayingzi
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=mujiayingzi
    Processing City 746  |  haverfordwest
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=haverfordwest
    Processing City 747  |  valente
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=valente
    Processing City 748  |  zhanatas
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=zhanatas
    Processing City 749  |  buraydah
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=buraydah
    Processing City 750  |  aloleng
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=aloleng
    Processing City 751  |  alotau
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=alotau
    Processing City 752  |  sarakhs
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=sarakhs
    Processing City 753  |  kiruna
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=kiruna
    Processing City 754  |  nouakchott
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=nouakchott
    Processing City 755  |  huarmey
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=huarmey
    Processing City 756  |  moron
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=moron
    Processing City 757  |  san andres
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=san andres
    Processing City 758  |  evensk
    http://api.openweathermap.org/data/2.5/weather?appid=8d1231a477d4bbcd36fe966326717bce&units=imperial&q=evensk
    ----------------------------
    Data Retrieval Complete
    ----------------------------



```python
# Remove any rows containing empty values
unique_df = unique_df.replace("", np.nan)
unique_df.dropna(how = "any", inplace = True)
#len(unique_df)
```


```python
# Check to see if all field counts are same
unique_df.count()
```




    City          673
    Country       673
    Latitude      673
    Longitude     673
    Date          673
    Max Temp      673
    Humidity      673
    Cloudiness    673
    Wind_Speed    673
    dtype: int64




```python
unique_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Country</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Date</th>
      <th>Max Temp</th>
      <th>Humidity</th>
      <th>Cloudiness</th>
      <th>Wind_Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>dana point</td>
      <td>us</td>
      <td>32.746596</td>
      <td>-118.121761</td>
      <td>1519855080</td>
      <td>62.0</td>
      <td>62.0</td>
      <td>1.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>vao</td>
      <td>nc</td>
      <td>-27.088292</td>
      <td>165.232422</td>
      <td>1519857751</td>
      <td>1.0</td>
      <td>92.0</td>
      <td>20.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>busselton</td>
      <td>au</td>
      <td>-58.212701</td>
      <td>86.782430</td>
      <td>1519857760</td>
      <td>62.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>hirara</td>
      <td>jp</td>
      <td>21.144415</td>
      <td>128.541418</td>
      <td>1519857748</td>
      <td>69.0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>qaqortoq</td>
      <td>gl</td>
      <td>63.923653</td>
      <td>-43.057192</td>
      <td>1519854600</td>
      <td>46.0</td>
      <td>39.0</td>
      <td>8.0</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
output_file = os.path.join("Output", "OutputFile.csv")
unique_df.to_csv(output_file, index = False, header = True)
```


```python
date = time.strftime("%m/%d/%Y")
# print(date)
```

# Latitude vs Temperature Plot


```python
# Latitude vs max temperature scatter plot
plt.scatter(unique_df["Latitude"], unique_df["Max Temp"], color = "blue", edgecolor = "black")
plt.suptitle("City Latitude vs Maximum Temperature")
plt.title(date)
plt.xlabel("Latitude")
plt.ylabel("Max Temperature (F)")

# Define output file path and export graph to output folder
temp_path = os.path.join("output", "latitude_vs_temperature.png")
plt.savefig(temp_path)

# Print plot to the screen
plt.show()
```


![png](output_14_0.png)


# Latitude vs Humidity Plot


```python
# Latitude vs humidity scatter plot
plt.scatter(unique_df["Latitude"], unique_df["Humidity"], color = "blue", edgecolor = "black")
plt.suptitle("City Latitude vs Humidity")
plt.title(date)
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")

# Define output file path and export graph to output folder
humidity_path = os.path.join("output", "latitude_vs_humidity.png")
plt.savefig(humidity_path)

# Print plot to the screen
plt.show()
```


![png](output_16_0.png)


# Latitude vs Cloudiness Plot


```python
# Latitude vs cloudiness scatter plot
plt.scatter(unique_df["Latitude"], unique_df["Cloudiness"], color = "blue", edgecolor = "black")
plt.suptitle("City Latitude vs Cloudiness")
plt.title(date)
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)")

# Define output file path and export graph to output folder
cloudiness_path = os.path.join("output", "latitude_vs_cloudiness.png")
plt.savefig(cloudiness_path)

# Print plot to the screen
plt.show()
```


![png](output_18_0.png)


# Latitude vs Wind Speed Plot


```python
# Latitude vs wind speed scatter plot
plt.scatter(unique_df["Latitude"], unique_df["Cloudiness"], color = "blue", edgecolor = "black")
plt.suptitle("City Latitude vs Wind Speed")
plt.title(date)
plt.xlabel("Latitude")
plt.ylabel("Wind_Speed (mph)")

# Define output file path and export graph to output folder
windspeed_path = os.path.join("output", "latitude_vs_windspeed.png")
plt.savefig(windspeed_path)

# Print plot to the screen
plt.show()
```


![png](output_20_0.png)

