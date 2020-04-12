# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file


#Code starts here

#Reading the file
data=pd.read_csv(path)

#Renaming a column
data.rename(columns={'Total':'Total_Medals'},inplace=True)

#Printing the first five columns
print(data.head(5))


#Code ends here


# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

data=pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'},inplace=True)
def f(x):
    if x["Total_Summer"]>x["Total_Winter"]:
        return "Summer"
    if x["Total_Summer"]==x["Total_Winter"]:
        return "Both"
    if x["Total_Summer"]<x["Total_Winter"]:
        return "Winter"
data["Better_Event"]=data.apply(f,axis=1)
data["Better_Event"].value_counts()
better_event="Summer"





# --------------
top_countries=data.loc[:,['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries.iloc[:-1,:]
country_list=[]
clm=top_countries.drop("Country_Name",axis=1).columns
def top_ten(top_countries,clmn):
    return top_countries.nlargest(10,clmn)["Country_Name"]
for clmn in clm :
    country_list.append(list(top_ten(top_countries,clmn)))
top_10_summer,top_10_winter,top_10=country_list
st1=set(country_list[0])
st2=set(country_list[1])
st3=set(country_list[2])
common=list(st1&st2&st3)
print(common)


# --------------
#Code starts here
summer_df=data.query("Country_Name in ['United States','Soviet Union','Great Britain','France','Germany','Italy','Sweden','Hungary','China','Australia']")
winter_df=data.query("Country_Name in ['Norway','United States','Austria','Germany','Soviet Union','Canada','Finland','Sweden','Switzerland','Russia']")
top_df=data.query("Country_Name in ['United States','Soviet Union','Great Britain','Germany','France','Italy','Sweden','China','East Germany','Russia']")
plt.scatter(summer_df["Country_Name"],summer_df["Total_Summer"],label="Summer")
plt.scatter(winter_df["Country_Name"],winter_df["Total_Winter"],c='r',label="Winter")
plt.scatter(top_df["Country_Name"],top_df["Total_Medals"],c='g',label="Total")
plt.legend()


# --------------
summer_df["Golden_Ratio"]=summer_df["Gold_Summer"]/summer_df["Total_Summer"]
summer_max_ratio=summer_df["Golden_Ratio"].max()
summer_country_gold=str(summer_df.loc[summer_df["Golden_Ratio"].max()==summer_df["Golden_Ratio"],"Country_Name"].values[0])
print(summer_max_ratio)
print(summer_country_gold)

winter_df["Golden_Ratio"]=winter_df["Gold_Winter"]/winter_df["Total_Winter"]
winter_max_ratio=winter_df["Golden_Ratio"].max()
winter_country_gold=str(winter_df.loc[winter_df["Golden_Ratio"].max()==winter_df["Golden_Ratio"],"Country_Name"].values[0])
print(winter_max_ratio)
print(winter_country_gold)

top_df["Golden_Ratio"]=top_df["Gold_Total"]/top_df["Total_Medals"]
top_max_ratio=top_df["Golden_Ratio"].max()
top_country_gold=str(top_df.loc[top_df["Golden_Ratio"].max()==top_df["Golden_Ratio"],"Country_Name"].values[0])
# top_country_gold=str(top_country_gold)
print(top_max_ratio)
print(top_country_gold)


# --------------
#Code starts here
data_1=data.iloc[:-1,:]
data_1["Total_Points"]=data_1["Gold_Total"]*3+data_1["Silver_Total"]*2+data_1["Bronze_Total"]
most_points=data_1["Total_Points"].max()
best_country=data_1.loc[data_1["Total_Points"].idxmax(),"Country_Name"]
print(most_points)
print(best_country)


# --------------
#Code starts herebest=data[data["Country_Name"]==best_country]
best=data[data["Country_Name"]==best_country]
best=best.loc[:,['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medas Tally")
plt.xticks(rotation=45)
best


