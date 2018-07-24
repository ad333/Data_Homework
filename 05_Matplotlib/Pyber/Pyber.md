
# Pyber Ride Sharing

## Analysis
    
    (1) For rural cities, number of drivers constituted only 1% of the total drivers while the 
        total rides were 5.3%.  On the other hand, for urban cities, number of drivers constituted 
        86.2% while the total rides were 68.4%.  Hence, demand for drivers were highest for the 
        rural type and lowest for the urban type. 
    
    (2) Average fare was lowest for the urban city type and highest for the rural city type.  
        This directly correlates with the earlier statistics on drivers demand.
    
    (3) Fare prices varied most in the rural cities while they were fairly consistent in the 
        urban cities.  This is probably due to high supply of drivers in the urban cities compared to 
        the rural cities.


```python
# import Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
```


```python
# Set file path
city_path = os.path.join("city_data.csv")
ride_path = os.path.join("ride_data.csv")
```


```python
# Import file and read into Pandas DataFrame
city_df = pd.read_csv(city_path)
ride_df = pd.read_csv(ride_path)
# city_df.head()
# ride_df.head()
```


```python
# Remove any duplicate cities
city_df = city_df.drop_duplicates("city")
```


```python
# merge two data
combine_df = ride_df.merge(city_df, on = "city")
combine_df.head()
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
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sarabury</td>
      <td>2016-07-23 07:42:44</td>
      <td>21.76</td>
      <td>7546681945283</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sarabury</td>
      <td>2016-04-02 04:32:25</td>
      <td>38.03</td>
      <td>4932495851866</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sarabury</td>
      <td>2016-06-23 05:03:41</td>
      <td>26.82</td>
      <td>6711035373406</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sarabury</td>
      <td>2016-09-30 12:48:34</td>
      <td>30.30</td>
      <td>6388737278232</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>



# Bubble Plot of Ride Sharing Data


```python
# Calculate the following variables

avg_fare_per_city = ride_df.groupby("city")["fare"].mean()
# avg_fare_per_city.head()

total_rides_per_city = ride_df.groupby("city")["ride_id"].count()
#total_rides_per_city.head()

total_drivers_per_city = city_df.groupby("city")["driver_count"].sum()
#total_drivers_per_city.head()

city_type = city_df.set_index("city")["type"]
# city_type.head()
```


```python
# Add above data into new dataframe
new_df = pd.DataFrame({"average_fare" : avg_fare_per_city,
                       "total_rides" : total_rides_per_city,
                       "total_drivers" : total_drivers_per_city,
                       "city_type" : city_type},
                     columns = ["average_fare", "total_rides", "total_drivers", "city_type"])
# new_df.head()
```


```python
# specific city types
rural_df = new_df[new_df["city_type"] == "Rural"]
suburban_df = new_df[new_df["city_type"] == "Suburban"]
urban_df = new_df[new_df["city_type"] == "Urban"]
```


```python
# Info of total rides, average fare and total drivers per city by city type
# These will be the axis in the bubble plot
rural_rides_df = rural_df["total_rides"]
suburban_rides_df = suburban_df["total_rides"]
urban_rides_df = urban_df["total_rides"]

rural_fare_df = rural_df["average_fare"]
suburban_fare_df = suburban_df["average_fare"]
urban_fare_df = urban_df["average_fare"]

rural_drivers_df = rural_df["total_drivers"]
suburban_drivers_df = suburban_df["total_drivers"]
urban_drivers_df = urban_df["total_drivers"]
```


```python
# Create scatter plot
rural = plt.scatter(rural_rides_df, rural_fare_df, s = rural_drivers_df*5, color = "gold", edgecolor = "black", alpha = 0.8)
suburban = plt.scatter(suburban_rides_df, suburban_fare_df, s = suburban_drivers_df*5, color = "lightskyblue", edgecolor = "black", alpha = 0.8)
urban = plt.scatter(urban_rides_df, urban_fare_df, s = urban_drivers_df*5, color = "lightcoral", edgecolor = "black", alpha = 0.8)

# Assign title, suptitle, axis labels and legends
plt.title("Note: Circle size correlates with Drivers count per city")
plt.suptitle("Pyber Ride Sharing Data")
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare Per City ($)")
plt.legend((rural, suburban, urban), ("Rural", "Suburban", "Urban"))

# Print the plot to the screen
plt.show()
```


![png](output_13_0.png)


# Total Fares by City Type


```python
# Calculate total fare by city type
total_fare = combine_df.groupby("type")["fare"].sum()

# total_fare
```


```python
# Set the following features
colors = ["yellow", "lightskyblue", "lightcoral"]
explode = [0, 0, 0.15]
labels = total_fare.index

# Assign title, create pie plot and print to screen
plt.title("% of Total Fares by City Type")
plt.pie(total_fare, startangle = 120, colors = colors, explode = explode, labels = labels, autopct = "%1.1f%%", shadow = True)
plt.show()
```


![png](output_16_0.png)


# Total Rides by City Type


```python
# Calculate total rides by city type
total_rides = combine_df.groupby("type")["ride_id"].count()

# total_rides
```


```python
# Set the following features
colors = ["yellow", "lightskyblue", "lightcoral"]
explode = [0, 0, 0.15]
labels = total_rides.index

# Assign title, create pie plot and print to screen
plt.title("% of Total Rides by City Type")
plt.pie(total_rides, startangle = 120, colors = colors, explode = explode, labels = labels, autopct = "%1.1f%%", shadow = True)
plt.show()
```


![png](output_19_0.png)


# Total Drivers by City Type


```python
# Calculate total drivers by city type
total_drivers = combine_df.groupby("type")["driver_count"].sum()

# total_drivers
```


```python
# Set the following features
colors = ["yellow", "lightskyblue", "lightcoral"]
explode = [0, 0, 0.15]
labels = total_drivers.index

# Assign title, create pie plot and print to screen
plt.title("% of Total Drivers by City Type")
plt.pie(total_drivers, startangle = 120, colors = colors, explode = explode, labels = labels, autopct = "%1.1f%%", shadow = True)
plt.show()
```


![png](output_22_0.png)

