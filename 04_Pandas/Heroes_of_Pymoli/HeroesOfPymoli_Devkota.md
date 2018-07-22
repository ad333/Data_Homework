
```python
# Summary of three observable trends based on data
print('''\n
      Summary of three observable trends
      ---------------------------------- 
        1. Heroes of Pymoli game is mainly dominated by male players, and they consist of 
            more than 80 percent of the total players.  Hence, they also lead in Purchase Count
            and Total Purchase Value.
            
        2. Age group 20-24 make up highest Purchase Count and Total purchase value, although 
            the average purchase price for this age group is the lowest.
            
        3. Most of the top spenders did not necessarily spent highest average price per item.  
            However, they purchased more number of items, and this led to the highest 
            Total Purchase Value.
        \n''')
```

    
    
          Summary of three observable trends
          ---------------------------------- 
            1. Heroes of Pymoli game is mainly dominated by male players, and they consist of 
                more than 80 percent of the total players.  Hence, they also lead in Purchase Count
                and Total Purchase Value.
                
            2. Age group 20-24 make up highest Purchase Count and Total purchase value, although 
                the average purchase price for this age group is the lowest.
                
            3. Most of the top spenders did not necessarily spent highest average price per item.  
                However, they purchased more number of items, and this led to the highest 
                Total Purchase Value.
            
    



```python
# Import Dependencies
import pandas as pd
import numpy as np
import os
```


```python
#Import file and read into Pandas DataFrame
data_file = "purchase_data.json"
df = pd.read_json(data_file)

# Print the first five rows of data to the screen
# df.head()
```


```python
# Find total number of unique players
total_players = len(df["SN"].unique())

# Convert the result into a DataFrame
total_players_df = pd.DataFrame({"Total Players" : [total_players]},
                             columns = ["Total Players"])

# Print 
print("\nPlayer Count")
print("------------")
total_players_df
```

    
    Player Count
    ------------





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
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Calculations for Purchasing Analysis (Total)
Number_of_unique_items = len(df["Item ID"].unique())
Average_purchase_price = round(df["Price"].mean(), 2)
Total_number_of_purchases = len(df["Price"])
Total_Revenue = round(df["Price"].sum(), 2)
```


```python
# Add results into a DataFrame and specify columns
purc_analysis_tot_df = pd.DataFrame([[Number_of_unique_items, Average_purchase_price, 
                                Total_number_of_purchases, Total_Revenue]],
                    columns = ["Number of Unique Items", "Average Purchase Price", 
                               "Number of Purchases", "Total Revenue"])    

# Format and print the DataFrame table
print("\nPurchasing Analysis (Total)")
print("---------------------------")
purc_analysis_tot_df.style.format({"Average Purchase Price" : "${:.2f}", "Total Revenue" : "${:.2f}"})
```

    
    Purchasing Analysis (Total)
    ---------------------------





<style  type="text/css" >
</style>  
<table id="T_16dcfbe6_1035_11e8_9563_6c96cfdcdde3" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Number of Unique Items</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Number of Purchases</th> 
        <th class="col_heading level0 col3" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_16dcfbe6_1035_11e8_9563_6c96cfdcdde3level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_16dcfbe6_1035_11e8_9563_6c96cfdcdde3row0_col0" class="data row0 col0" >183</td> 
        <td id="T_16dcfbe6_1035_11e8_9563_6c96cfdcdde3row0_col1" class="data row0 col1" >$2.93</td> 
        <td id="T_16dcfbe6_1035_11e8_9563_6c96cfdcdde3row0_col2" class="data row0 col2" >780</td> 
        <td id="T_16dcfbe6_1035_11e8_9563_6c96cfdcdde3row0_col3" class="data row0 col3" >$2286.33</td> 
    </tr></tbody> 
</table> 




```python
# Calculate count and percent of each Gender
male_count = df[df["Gender"] == "Male"]["SN"].nunique()
female_count = df[df["Gender"] == "Female"]["SN"].nunique()
other_count = df[df["Gender"] == "Other / Non-Disclosed"]["SN"].nunique()

male_percent = (male_count / total_players) * 100
female_percent = (female_count / total_players) * 100
other_percent = (other_count / total_players) * 100
```


```python
# Add results into a DataFrame, specify index and columns
gender_dem_df = pd.DataFrame([[male_percent, male_count],
                               [female_percent, female_count],
                               [other_percent, other_count]],
                            index = ["Male", "Female", "Other / Non-disclosed"],
                            columns = ["Percentage of Players", "Total Count"])  

# Format and print the DataFrame table
print("\nGender Demographics")
print("-------------------")
gender_dem_df.style.format({"Percentage of Players" : "{:.2f}%"})
```

    
    Gender Demographics
    -------------------





<style  type="text/css" >
</style>  
<table id="T_16e09940_1035_11e8_b54c_6c96cfdcdde3" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Percentage of Players</th> 
        <th class="col_heading level0 col1" >Total Count</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_16e09940_1035_11e8_b54c_6c96cfdcdde3level0_row0" class="row_heading level0 row0" >Male</th> 
        <td id="T_16e09940_1035_11e8_b54c_6c96cfdcdde3row0_col0" class="data row0 col0" >81.15%</td> 
        <td id="T_16e09940_1035_11e8_b54c_6c96cfdcdde3row0_col1" class="data row0 col1" >465</td> 
    </tr>    <tr> 
        <th id="T_16e09940_1035_11e8_b54c_6c96cfdcdde3level0_row1" class="row_heading level0 row1" >Female</th> 
        <td id="T_16e09940_1035_11e8_b54c_6c96cfdcdde3row1_col0" class="data row1 col0" >17.45%</td> 
        <td id="T_16e09940_1035_11e8_b54c_6c96cfdcdde3row1_col1" class="data row1 col1" >100</td> 
    </tr>    <tr> 
        <th id="T_16e09940_1035_11e8_b54c_6c96cfdcdde3level0_row2" class="row_heading level0 row2" >Other / Non-disclosed</th> 
        <td id="T_16e09940_1035_11e8_b54c_6c96cfdcdde3row2_col0" class="data row2 col0" >1.40%</td> 
        <td id="T_16e09940_1035_11e8_b54c_6c96cfdcdde3row2_col1" class="data row2 col1" >8</td> 
    </tr></tbody> 
</table> 




```python
# Calculate Purchase Count, Average Purchase Price, Total Purchase Value and Normalized totals for each Gender
purchase_male = df[df["Gender"] == "Male"]["Price"].count()
purchase_female = df[df["Gender"] == "Female"]["Price"].count()
purchase_other = df[df["Gender"] == "Other / Non-Disclosed"]["Price"].count()

ave_price_male = df[df["Gender"] == "Male"]["Price"].mean()
ave_price_female = df[df["Gender"] == "Female"]["Price"].mean()
ave_price_other = df[df["Gender"] == "Other / Non-Disclosed"]["Price"].mean()

tot_value_male = df[df["Gender"] == "Male"]["Price"].sum()
tot_value_female = df[df["Gender"] == "Female"]["Price"].sum()
tot_value_other = df[df["Gender"] == "Other / Non-Disclosed"]["Price"].sum()

norm_tot_male = tot_value_male / male_count
norm_tot_female = tot_value_female / female_count
norm_tot_other = tot_value_other / other_count
```


```python
# Add results into a DataFrame, specify index and columns
purchasing_analysis_df = pd.DataFrame([[purchase_male, ave_price_male, tot_value_male, norm_tot_male],
                               [purchase_female, ave_price_female, tot_value_female, norm_tot_female],
                               [purchase_other, ave_price_other, tot_value_other, norm_tot_other]],
                            index = ["Male", "Female", "Other / Non-disclosed"],
                            columns = ["Purchase Count", "Average Purchase Price", 
                                       "Total Purchase Value", "Normalized Totals"])  

# Format and print the DataFrame table
print("\nPurchasing Analysis (Gender)")
print("----------------------------")
purchasing_analysis_df.style.format({"Average Purchase Price" : "${:.2f}", 
                                     "Total Purchase Value" : "${:.2f}",
                                     "Normalized Totals" : "${:.2f}"})
```

    
    Purchasing Analysis (Gender)
    ----------------------------





<style  type="text/css" >
</style>  
<table id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
        <th class="col_heading level0 col3" >Normalized Totals</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3level0_row0" class="row_heading level0 row0" >Male</th> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row0_col0" class="data row0 col0" >633</td> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row0_col1" class="data row0 col1" >$2.95</td> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row0_col2" class="data row0 col2" >$1867.68</td> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row0_col3" class="data row0 col3" >$4.02</td> 
    </tr>    <tr> 
        <th id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3level0_row1" class="row_heading level0 row1" >Female</th> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row1_col0" class="data row1 col0" >136</td> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row1_col1" class="data row1 col1" >$2.82</td> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row1_col2" class="data row1 col2" >$382.91</td> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row1_col3" class="data row1 col3" >$3.83</td> 
    </tr>    <tr> 
        <th id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3level0_row2" class="row_heading level0 row2" >Other / Non-disclosed</th> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row2_col0" class="data row2 col0" >11</td> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row2_col1" class="data row2 col1" >$3.25</td> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row2_col2" class="data row2 col2" >$35.74</td> 
        <td id="T_16e6fa68_1035_11e8_81ec_6c96cfdcdde3row2_col3" class="data row2 col3" >$4.47</td> 
    </tr></tbody> 
</table> 




```python
# Determine maximum and minimum Age values to create bins
# print("max:", df["Age"].max())
# print("min:", df["Age"].min())
```


```python
# Create bins and assign group labels
bins = [0, 9, 14, 19, 24, 29, 34, 39, 44]
group_labels = ["Less than 10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40 or above"]

# Slice the data and place into bins
pd.cut(df["Age"], bins, labels = group_labels).head()

# Place the data series into a new column named "Age Group" inside of the DataFrame
df["Age Group"] = pd.cut(df["Age"], bins, labels = group_labels)
# df.head()
```


```python
# Create a groupby object based on "Age Group"
by_group = df.groupby("Age Group")

# Calculations
purchase_count = by_group["Age"].count()
total_purchase_value = by_group["Price"].sum()
average_purchase_price = by_group["Price"].mean()
normalized_totals = round((total_purchase_value / purchase_count), 2)

# Add results to a DataFrame and rename column headers
purchase_count_df = pd.DataFrame(purchase_count)
renamed_purchase_count_df = purchase_count_df.rename(columns = {"Age" : "Purchase Count"})
total_purchase_value_df = pd.DataFrame(total_purchase_value)
renamed_total_purchase_value_df = total_purchase_value_df.rename(columns = {"Price" : "Total Purchase Value"})
average_purchase_price_df = pd.DataFrame(average_purchase_price)
renamed_average_purchase_price_df = average_purchase_price_df.rename(columns = {"Price" : "Average Purchase Price"})
normalized_totals_df = pd.DataFrame(normalized_totals)
renamed_normalized_total_df = normalized_totals_df.rename(columns = {0 : "Normalized Totals"})
```


```python
# Merge DataFrame tables
merge_table1 = pd.DataFrame.join(renamed_purchase_count_df, renamed_average_purchase_price_df)
merge_table2 = pd.DataFrame.join(merge_table1, renamed_total_purchase_value_df)
age_demographics_df = pd.DataFrame.join(merge_table2, renamed_normalized_total_df)

# Format and print the DataFrame table
print("\nAge Demographics")
print("----------------")
age_demographics_df.style.format({"Average Purchase Price" : "${:.2f}", 
                                            "Total Purchase Value" : "${:.2f}",
                                            "Normalized Totals" : "${:.2f}"})
```

    
    Age Demographics
    ----------------





<style  type="text/css" >
</style>  
<table id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
        <th class="col_heading level0 col3" >Normalized Totals</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Age Group</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3level0_row0" class="row_heading level0 row0" >Less than 10</th> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row0_col0" class="data row0 col0" >28</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row0_col1" class="data row0 col1" >$2.98</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row0_col2" class="data row0 col2" >$83.46</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row0_col3" class="data row0 col3" >$2.98</td> 
    </tr>    <tr> 
        <th id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3level0_row1" class="row_heading level0 row1" >10-14</th> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row1_col0" class="data row1 col0" >35</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row1_col1" class="data row1 col1" >$2.77</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row1_col2" class="data row1 col2" >$96.95</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row1_col3" class="data row1 col3" >$2.77</td> 
    </tr>    <tr> 
        <th id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3level0_row2" class="row_heading level0 row2" >15-19</th> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row2_col0" class="data row2 col0" >133</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row2_col1" class="data row2 col1" >$2.91</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row2_col2" class="data row2 col2" >$386.42</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row2_col3" class="data row2 col3" >$2.91</td> 
    </tr>    <tr> 
        <th id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3level0_row3" class="row_heading level0 row3" >20-24</th> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row3_col0" class="data row3 col0" >336</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row3_col1" class="data row3 col1" >$2.91</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row3_col2" class="data row3 col2" >$978.77</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row3_col3" class="data row3 col3" >$2.91</td> 
    </tr>    <tr> 
        <th id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3level0_row4" class="row_heading level0 row4" >25-29</th> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row4_col0" class="data row4 col0" >125</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row4_col1" class="data row4 col1" >$2.96</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row4_col2" class="data row4 col2" >$370.33</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row4_col3" class="data row4 col3" >$2.96</td> 
    </tr>    <tr> 
        <th id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3level0_row5" class="row_heading level0 row5" >30-34</th> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row5_col0" class="data row5 col0" >64</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row5_col1" class="data row5 col1" >$3.08</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row5_col2" class="data row5 col2" >$197.25</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row5_col3" class="data row5 col3" >$3.08</td> 
    </tr>    <tr> 
        <th id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3level0_row6" class="row_heading level0 row6" >35-39</th> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row6_col0" class="data row6 col0" >42</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row6_col1" class="data row6 col1" >$2.84</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row6_col2" class="data row6 col2" >$119.40</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row6_col3" class="data row6 col3" >$2.84</td> 
    </tr>    <tr> 
        <th id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3level0_row7" class="row_heading level0 row7" >40 or above</th> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row7_col0" class="data row7 col0" >16</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row7_col1" class="data row7 col1" >$3.19</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row7_col2" class="data row7 col2" >$51.03</td> 
        <td id="T_16efcdd4_1035_11e8_9060_6c96cfdcdde3row7_col3" class="data row7 col3" >$3.19</td> 
    </tr></tbody> 
</table> 




```python
# Groupby players to determine Total Purchase Value, Average Purchase Price and Purchase Count
purchase_total = df.groupby("SN")["Price"].sum().to_frame()
purchase_count = df.groupby("SN")["Price"].count().to_frame() 
purchase_average = df.groupby("SN")["Price"].mean().to_frame()

# Rename columns
purchase_count.columns = ["Purchase Count"]
purchase_total.columns = ["Total Purchase Value"]
purchase_average.columns = ["Average Purchase Price"]
```


```python
# Merge the DataFrames
merge1 = pd.DataFrame.join(purchase_count, purchase_average)
merge2 = pd.DataFrame.join(merge1, purchase_total)

# Put column names in order
merge2.columns = ["Purchase Count", "Average Purchase Price", "Total Purchase Value"]

# Format and print the DataFrame table
print("\nTop Spenders")
print("------------")
top_spenders = merge2.sort_values('Total Purchase Value', ascending = False).head()
top_spenders.style.format({"Average Purchase Price" : "${:.2f}", "Total Purchase Value" : "${:.2f}"})
```

    
    Top Spenders
    ------------





<style  type="text/css" >
</style>  
<table id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >SN</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3level0_row0" class="row_heading level0 row0" >Undirrala66</th> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row0_col0" class="data row0 col0" >5</td> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row0_col1" class="data row0 col1" >$3.41</td> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row0_col2" class="data row0 col2" >$17.06</td> 
    </tr>    <tr> 
        <th id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3level0_row1" class="row_heading level0 row1" >Saedue76</th> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row1_col0" class="data row1 col0" >4</td> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row1_col1" class="data row1 col1" >$3.39</td> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row1_col2" class="data row1 col2" >$13.56</td> 
    </tr>    <tr> 
        <th id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3level0_row2" class="row_heading level0 row2" >Mindimnya67</th> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row2_col0" class="data row2 col0" >4</td> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row2_col1" class="data row2 col1" >$3.18</td> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row2_col2" class="data row2 col2" >$12.74</td> 
    </tr>    <tr> 
        <th id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3level0_row3" class="row_heading level0 row3" >Haellysu29</th> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row3_col0" class="data row3 col0" >3</td> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row3_col1" class="data row3 col1" >$4.24</td> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row3_col2" class="data row3 col2" >$12.73</td> 
    </tr>    <tr> 
        <th id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3level0_row4" class="row_heading level0 row4" >Eoda93</th> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row4_col0" class="data row4 col0" >3</td> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row4_col1" class="data row4 col1" >$3.86</td> 
        <td id="T_16f4e580_1035_11e8_8306_6c96cfdcdde3row4_col2" class="data row4 col2" >$11.58</td> 
    </tr></tbody> 
</table> 




```python
# Groupe by following items
sum_id = df.groupby("Item ID").sum().reset_index()
sum_name = df.groupby("Item Name").sum().reset_index()
count_item = df.groupby("Item Name").count().reset_index()

# Merge DataFrames
m1 = pd.merge(sum_name, sum_id, on = "Price")
m2 = pd.merge(count_item, m1, on = "Item Name")
# m2.head()
```


```python
# Calculate item price and rename all column names to more descriptive names
m2["Gender"] = round((m2["Price_y"]/m2["Item ID"]), 2)
m2_renamed = m2.rename(columns = {"Age" : "Purchase Count",
                                 "Gender" : "Item Price",
                                 "Item ID" : "null",
                                 "Price_y" : "Total Purchase Value",
                                 "Item ID_y" : "Item ID"})

# Reorder column names and set index
m2_organized = m2_renamed[["Item ID", "Item Name", "Purchase Count", "Item Price", "Total Purchase Value"]]
m2_organized_indexed = m2_organized.set_index(["Item Name", "Item ID"])

# Format, sort according to Purchase count and print 5 most popular items
print("\nMost Popular Items")
print("------------------")
most_popular_items = m2_organized_indexed.sort_values("Purchase Count", ascending = False).head()
most_popular_items.style.format({"Item Price" : "${:.2f}", "Total Purchase Value" : "${:.2f}"})

```

    
    Most Popular Items
    ------------------





<style  type="text/css" >
</style>  
<table id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3" > 
<thead>    <tr> 
        <th class="blank" ></th> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Item Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item Name</th> 
        <th class="index_name level1" >Item ID</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3level0_row0" class="row_heading level0 row0" >Arcane Gem</th> 
        <th id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3level1_row0" class="row_heading level1 row0" >84</th> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row0_col0" class="data row0 col0" >11</td> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row0_col1" class="data row0 col1" >$2.23</td> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row0_col2" class="data row0 col2" >$24.53</td> 
    </tr>    <tr> 
        <th id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3level0_row1" class="row_heading level0 row1" >Betrayal, Whisper of Grieving Widows</th> 
        <th id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3level1_row1" class="row_heading level1 row1" >39</th> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row1_col0" class="data row1 col0" >11</td> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row1_col1" class="data row1 col1" >$2.35</td> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row1_col2" class="data row1 col2" >$25.85</td> 
    </tr>    <tr> 
        <th id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3level0_row2" class="row_heading level0 row2" >Trickster</th> 
        <th id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3level1_row2" class="row_heading level1 row2" >31</th> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row2_col0" class="data row2 col0" >9</td> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row2_col1" class="data row2 col1" >$2.07</td> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row2_col2" class="data row2 col2" >$18.63</td> 
    </tr>    <tr> 
        <th id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3level0_row3" class="row_heading level0 row3" >Woeful Adamantite Claymore</th> 
        <th id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3level1_row3" class="row_heading level1 row3" >175</th> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row3_col0" class="data row3 col0" >9</td> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row3_col1" class="data row3 col1" >$1.24</td> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row3_col2" class="data row3 col2" >$11.16</td> 
    </tr>    <tr> 
        <th id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3level0_row4" class="row_heading level0 row4" >Serenity</th> 
        <th id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3level1_row4" class="row_heading level1 row4" >13</th> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row4_col0" class="data row4 col0" >9</td> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row4_col1" class="data row4 col1" >$1.49</td> 
        <td id="T_16fbe1b4_1035_11e8_b651_6c96cfdcdde3row4_col2" class="data row4 col2" >$13.41</td> 
    </tr></tbody> 
</table> 




```python
# Sort according to Total Purchase Value, format results and print 5 most profitable items
print("\nMost Profitable Items")
print("---------------------")
most_profitable_items = m2_organized_indexed.sort_values("Total Purchase Value", ascending = False).head()
most_profitable_items.style.format({"Item Price" : "${:.2f}", "Total Purchase Value" : "${:.2f}"})
```

    
    Most Profitable Items
    ---------------------





<style  type="text/css" >
</style>  
<table id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3" > 
<thead>    <tr> 
        <th class="blank" ></th> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Item Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item Name</th> 
        <th class="index_name level1" >Item ID</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3level0_row0" class="row_heading level0 row0" >Retribution Axe</th> 
        <th id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3level1_row0" class="row_heading level1 row0" >34</th> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row0_col0" class="data row0 col0" >9</td> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row0_col1" class="data row0 col1" >$4.14</td> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row0_col2" class="data row0 col2" >$37.26</td> 
    </tr>    <tr> 
        <th id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3level0_row1" class="row_heading level0 row1" >Spectral Diamond Doomblade</th> 
        <th id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3level1_row1" class="row_heading level1 row1" >115</th> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row1_col0" class="data row1 col0" >7</td> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row1_col1" class="data row1 col1" >$4.25</td> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row1_col2" class="data row1 col2" >$29.75</td> 
    </tr>    <tr> 
        <th id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3level0_row2" class="row_heading level0 row2" >Orenmir</th> 
        <th id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3level1_row2" class="row_heading level1 row2" >32</th> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row2_col0" class="data row2 col0" >6</td> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row2_col1" class="data row2 col1" >$4.95</td> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row2_col2" class="data row2 col2" >$29.70</td> 
    </tr>    <tr> 
        <th id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3level0_row3" class="row_heading level0 row3" >Singed Scalpel</th> 
        <th id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3level1_row3" class="row_heading level1 row3" >103</th> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row3_col0" class="data row3 col0" >6</td> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row3_col1" class="data row3 col1" >$4.87</td> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row3_col2" class="data row3 col2" >$29.22</td> 
    </tr>    <tr> 
        <th id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3level0_row4" class="row_heading level0 row4" >Splitter, Foe Of Subtlety</th> 
        <th id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3level1_row4" class="row_heading level1 row4" >107</th> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row4_col0" class="data row4 col0" >8</td> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row4_col1" class="data row4 col1" >$3.61</td> 
        <td id="T_16fddcc6_1035_11e8_bac1_6c96cfdcdde3row4_col2" class="data row4 col2" >$28.88</td> 
    </tr></tbody> 
</table> 


