# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:17:22 2020

@author: dell
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import gspread
from oauth2client.service_account import ServiceAccountCredentials
a='https://www.googleapis.com/auth/spreadsheets.readonly'
b='https://www.googleapis.com/auth/spreadsheets'
c='https://www.googleapis.com/auth/drive.readonly'
d='https://www.googleapis.com/auth/drive.file'
e='https://www.googleapis.com/auth/drive'
scope=[a,b,c,d,e]
credit=ServiceAccountCredentials.from_json_keyfile_name('E:\ds_jyp\cred.json',scope)
client=gspread.authorize(credit)
# sheet=client.open('document').sheet1
#print(sheet.col_values(1))
plt.style.use('fivethirtyeight')
fig1=plt.figure()
ax1=fig1.add_subplot(1,1,1)
def animate(p):
    plot_data=client.open('document').sheet1
    line_data=plot_data.col_values(1)
    for i in range(0,len(line_data)):
        line_data[i]=int(line_data[i])
    l1=list(range(len(line_data)))
    x1=[]
    y1=[]
    for i in range(0,len(line_data)):
        y,x=line_data[i],l1[i]
        x1.append(x)
        y1.append(y)
        ax1.clear()
        ax1.plot(x1,y1)
anime_data=animation.FuncAnimation(fig1,animate,interval=10)
print(anime_data)