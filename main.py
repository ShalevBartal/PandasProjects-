# This dataset includes information on over 9,000 animal bites which occurred near Louisville,
# Kentucky from 1985 to 2017 and includes information on whether the animal was quarantined after the bite occurred and whether that animal was rabid.
import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('C:/Users/shalev/Desktop/Health_AnimalBites.csv')
print( df.shape)  # Geting the scale of the data set


# THE ATTRIBUTES OF THE DATA SET:
# bite_date: The date the bite occurred
# SpeciesIDDesc: The species of animal that did the biting
# BreedIDDesc: Breed (if known)
# GenderIDDesc: Gender (of the animal)
# color: color of the animal
# vaccination_yrs: how many years had passed since the last vaccination
# vaccination_date: the date of the last vaccination
# victim_zip: the zipcode of the victim
# AdvIssuedYNDesc: whether advice was issued
# WhereBittenIDDesc: Where on the body the victim was bitten
# quarantine_date: whether the animal was quarantined
# DispositionIDDesc: whether the animal was released from quarantine
# headsentdate: the date the animal’s head was sent to the lab
# release_date: the date the animal was released
# ResultsIDDesc: results from lab tests (for rabies)

# My research questions:
# 1.What are the unique types of animals?
# 2.who is the most common biter?
# 3.Who is the animal that bites the least?
# 4.how many bite cases per year?
# 5.What is the year with most bite cases and how many cases was in it and the same check about the year with the least bite cases.
# 6.Is there an increase in the number of bites per year?
# 7.What is the most common body part that geting bited(head or body)?
# 8.Percentage of people who contracted rabies following the bite
# 9.percentage of animals who died or killed during the quarantine

# Preparation the dataset to conduct the research questions:
# 1.fixing the date coulmuns (We want to delete the "00:00" fron evry cell)
# 2.delete the empty rows(when 'SpeciesIDDesc' is null)
# 3.Removing duplicates

# 2.delete the empty rows(when 'SpeciesIDDesc' is null)

df.dropna(subset = ["SpeciesIDDesc"], inplace=True)
df.dropna(subset = ["bite_date"], inplace=True)


# 1.fixing the date coulmuns (We want to delete the "00:00" fron evry cell)
df["vaccination_date"].fillna("00/00/0000", inplace=True)
df["quarantine_date"].fillna("00/00/0000", inplace=True)
df["head_sent_date"].fillna("00/00/0000", inplace=True)
df["release_date"].fillna("00/00/0000", inplace=True)


for x in df.index:
    if '00:00' in df.loc[x, "vaccination_date"]:
        df.loc[x, "vaccination_date"] = df.loc[x, "vaccination_date"].replace('00:00', '')

for x in df.index:
    if '00:00' in df.loc[x, "quarantine_date"]:
        df.loc[x, "quarantine_date"] = df.loc[x, "quarantine_date"].replace('00:00', '')

for x in df.index:
    if '00:00' in df.loc[x, "head_sent_date"]:
        df.loc[x, "head_sent_date"] = df.loc[x, "head_sent_date"].replace('00:00', '')

for x in df.index:
    if '00:00' in df.loc[x, "release_date"]:
        df.loc[x, "release_date"] = df.loc[x, "release_date"].replace('00:00', '')

for x in df.index:
    if '00:00' in df.loc[x, "bite_date"]:
        df.loc[x, "bite_date"] = df.loc[x, "bite_date"].replace('00:00', '')


# 3 Removing duplicates
df.drop_duplicates(inplace=True)


# we can start our research
print(df.info)

# 1.What are the unique types of animals?

unique_animals = df.SpeciesIDDesc.unique()
h='\n'
print('1.The unique animals are ')
print(unique_animals,h)

# 2.who is the most common biter?

a={}
for x in unique_animals:
    a[x] = len(df.loc[df.SpeciesIDDesc == x])

print(a)

max_key=max(a,key=a.get)
print('2.The most common biter is the '+ max_key,h)

# 3.Who is the animal that bites the least?

min_key=min(a,key=a.get)
print('3.The animal that bites the least is the '+min_key,h)

#4.how many bite cases per year ?
#Before the print i relise that the year 2011 accedntly wrriten as 2101 so i will fix the wrong values.
for x in df.index:
    if '2101' in df.loc[x, "bite_date"]:
        df.loc[x, "bite_date"] = df.loc[x, "bite_date"].replace('2101', '2011')

a=[]
b=[]
for x in df.index:
    a=df.loc[x, "bite_date"].split('/')
    b.append(a[2])

BiteSeries=pd.Series(b)
print('4.Rank of bites per year')
print(BiteSeries.value_counts(),h)

# 5.What is the year with most bite cases and how many cases was in it and the same check about the year with the least bite cases.
max_key=max(b,key=b.count)
min_key=min(b,key=b.count)
c=BiteSeries.value_counts()
d='5.The year with the most bite cases is'
e='The number of cases was'
f='The year with the least bite cases is'
g='The number of cases was'

print(d,max_key,e,c[0],f,min_key,g,c[-1],h)


#After the print i relise that also the years 2013,2001 accedntly wrriten wrongly so i will fix the wrong values.
for x in df.index:
    if '5013' in df.loc[x, "bite_date"]:
        df.loc[x, "bite_date"] = df.loc[x, "bite_date"].replace('5013', '2013')

for x in df.index:
    if '2201' in df.loc[x, "bite_date"]:
        df.loc[x, "bite_date"] = df.loc[x, "bite_date"].replace('2201', '2001')

# 6.Is there an increase in the number of bites (avg) per year?













