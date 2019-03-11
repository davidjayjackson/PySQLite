#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
connection = sqlite3.connect("sun_data.sqlite3")

df = pd.read_csv("/Users/howe/DeskTop/combined.csv")
Ra = pd.read_csv("https://www.aavso.org/sites/default/files/solar/NOAAfiles/NOAAdaily.csv")

df.head()
Ra.head()

df.to_sql('data',connection)
Ra.to_sql('Ra',connection,)

db = pd.read_sql("select * from data where Year =1955;",connection)
db1 = pd.read_sql("select Year,avg(aavso)as aavso,avg(AMERICAN) as american from data  group by Year;",connection)

db1.head()

year = db.Ymd
spots = db.AMERICAN
aavso = db.AAVSO
yr = db1.Year
spt = db1.american
aa = db1.aavso


plt.plot(year,spots)
plt.plot(year,aavso)
plt.xlabel("Year-Month-Day")
plt.ylabel('Sunspots')
plt.show()


plt.bar(yr,spt)
plt.plot(yr,aa)
plt.xlabel("Year-Month-Day")
plt.ylabel('Sunspots')
plt.show()



