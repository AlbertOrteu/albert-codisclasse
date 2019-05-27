#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
import time
#import Adafruit_DHT
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import matplotlib as mpl
from random import randint


def googledrive():
    # PUJADA AL DRIVE DEL PNG OBTINGUT
    g_login = GoogleAuth()
    g_login.LoadCredentialsFile("mycreds.txt")
    if g_login.credentials is None:
        # Authenticate if they're not there
        g_login.LocalWebserverAuth()
    elif g_login.access_token_expired:
        # Refresh them if expired
        g_login.Refresh()
    else:
        # Initialize the saved creds
        g_login.Authorize()
    # Save the current credentials to a file
    g_login.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(g_login)
    print('si')
    file_drive = drive.CreateFile({'title': data})  
    file_drive.SetContentFile(data)
    file_drive.Upload()
    print("L'arxiu ha pujat al drive")
    sys.exit()




#Base pel nom d'arxiu png que pujarem al drive
data = '{}-dht11.png'.format(str(datetime.datetime.now()).replace(' ','-').replace(':','-'))

# Definicio del sensor i el pin de dades
#sensor = Adafruit_DHT.DHT11
#pin = '4'
# Inicialitzacio de dades i variables
count = 0
a=[]
b=[]
xs =[]
buleana = True

# Recollida de dades del sensor DHT11. 10 mesures en 5 hores.
while buleana:
    count += 1
    #humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    humidity, temperature = (randint(50,100),randint(20,35))
    print(humidity,temperature)
    a.append(humidity)
    b.append(temperature)
    xs.append(time.strftime('%H:%M'))
    time.sleep(10)
    if count == 10:
       buleana = False
############################ DIAGRAMA DE BARRES DE TEMPERATURA I HUMITAT ###################################################################################
label_size = 5
mpl.rcParams['xtick.labelsize'] = label_size 
ind=range(10) # Coordenades x
fig, (ax1,ax2) = plt.subplots(1,2) # Numero de grafiques que dibuixem a la figura. que passa si fem fig, (ax1,ax2) = plt.subplots(1,2)
width = 0.35 # Amplada dels diagrames
rects1 = ax1.bar(ind, a, width, color='r') # Dades dels diagrames. Coordenades, Valors de les variables, Amplada i Color.
ax1.set_ylabel('Humitat %') # Llegenda de eix Y.
ax1.set_title('10 mesures humitat') # Titol del grafic
ax1.set_xticks(ind) # Marques sota de cada diagrama
ax1.set_xticklabels(xs)
ax1.yaxis.set_major_locator(plt.NullLocator())
for rect in rects1: # Dibuixem cadascun dels diagrames que son rectangles.
        height = rect.get_height() # De cada rectangle agafem la seva alcada.
        ax1.text(rect.get_x() + rect.get_width()/2., height,'%d' % int(height),ha='center', va='bottom') # Els valors quedaran damunt del diagrama
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['top'].set_visible(False)

width = 0.35 # Amplada dels diagrames
rects2 = ax2.bar(ind, b, width, color='r') # Dades dels diagrames. Coordenades, Valors de les variables, Amplada i Color.
ax2.set_ylabel('Temperatura') # Llegenda de eix Y.
ax2.set_title('10 mesures temperatura') # Titol del grafic
ax2.set_xticks(ind) # Marques sota de cada diagrama
ax2.set_xticklabels(xs)
ax2.yaxis.set_major_locator(plt.NullLocator())
for rect in rects2: # Dibuixem cadascun dels diagrames que son rectangles.
        height = rect.get_height() # De cada rectangle agafem la seva alcada.
        ax2.text(rect.get_x() + rect.get_width()/2., height,'%d' % int(height),ha='center', va='bottom') # Els valors quedaran damunt del diagrama
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['top'].set_visible(False)  
plt.savefig(data,dpi=300)
plt.close(fig)

googledrive()
