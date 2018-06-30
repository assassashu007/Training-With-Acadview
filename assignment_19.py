import pandas as pd


print("\nQ1. Create a dataframe with your name, age, mail-id and phone number and add your friends’s information to the same.\n")

data = {'Name':['Ashutosh'],'Age':[21],'mail id':['assassashu007@gmail.com'],'phone no':['8171xxxxxx']}
df = pd.DataFrame(data)
df.loc[1]=['Prerak',21,'prerakpanwar@gmail.com','9077xxxxxx']       #Add detail of friend 1
df.loc[2]=['Kushagra',21,'matrukhush@gmail.com','7066xxxxxx']       #Add detail of friend 2
print(df)
print("\n")



print("\n\nQ2. Import the data from "https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv" and print:\n")

df=pd.read_csv('weather.csv')
#print(df)

#a.) First 5 rows of Dataframe
print(df.head(5))

#b.) First 10 rows of the Dataframe
print(df.head(10))

#c.) Find basic statistics on the particular dataset.
print(df['MinTemp'].describe())
print(df['MaxTemp'].describe())

#d.) Find the last 5 rows of the dataframe
print(df.tail(5))

#e.) Extract the 2nd column and find basic statistics on it.
finaldata=[df.iloc[:,2].sum(),
df.iloc[:,2].mean(),
df.iloc[:,2].median(),
df.iloc[:,2].nunique(),
df.iloc[:,2].max(),
df.iloc[:,2].min()]
print(finaldata) 
