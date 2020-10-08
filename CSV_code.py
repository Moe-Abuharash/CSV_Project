import csv
from datetime import datetime
open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
'''
print(header_row)

for index, column_header in enumerate(header_row):
    print(index,column_header)

'''

import csv
from datetime import datetime
new_file = open("death_valley_2018_simple.csv", "r")

csv_blip = csv.reader(new_file, delimiter=",")

lower_row = next(csv_blip)

# new_vari = header_row.index('TMAX')



high_sitka = []
date_sitka =[]
low_sitka = []
high_dv = []
date_dv = []
low_dv = []
    #for index, col_header in enumerate(header_row):


    #if n == csv_file:
        #highs = []
        #dates =[]
        #lows = []

for row in csv_file:
    try:
        new_vari = header_row.index('TMAX')
        new_vari1 = header_row.index('TMIN')
        new_vari2 = header_row.index('DATE')
        #high_sitka.append(row[new_vari])
        #current_date = datetime.strptime(row[new_vari2],'%Y-%m-%d')
        #date_sitka.append(current_date)
        #low_sitka.append(row[new_vari1])
                #highs.append(int(row[max]))
                    #current_date= datetime.strptime(row[date],'%Y-%m-%d')
                    #dates.append(x)
                   # lows.append(int(row[min]))
    except ValueError:
        print("Missing data for date")
    else:
        high_sitka.append(row[new_vari])
        current_date = datetime.strptime(row[new_vari2],'%Y-%m-%d')
        date_sitka.append(current_date)
        low_sitka.append(row[new_vari1])
        

   # if x == csv_file:
        #high = []
        #date =[]
        #low = []

for row in csv_blip:
    #high = []
    #date =[]
    #low = []
    try:
        vari = lower_row.index('TMAX')
        vari1 = lower_row.index('TMIN')
        vari2 = lower_row.index('DATE')
        #high_dv.append(row[vari])
        #current_date= datetime.strptime(row[vari2],'%Y-%m-%d')
        #date_dv.append(current_date)    
        #low_dv.append(row[vari1])
        #print(vari)
    except ValueError:
        print("Missing data for date")
    else:
        high_dv.append(row[vari])
        current_date= datetime.strptime(row[vari2],'%Y-%m-%d')
        date_dv.append(current_date)    
        low_dv.append(row[vari1])

#print(high_dv)
#print(low_dv)
#print(date_dv)                            
                
                
                #high.append(int(row[max]))
                #current_date= datetime.strptime(row[date],'%Y-%m-%d')
                #date.append(x)
                #low.append(int(row[min]))
            #except:
                #print("Missing data for date")




'''for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
'''

import matplotlib.pyplot as plt
fig,ax = plt.subplots(2)

#fig = plt.figure()

ax[1].plot(date_dv, low_dv, c="blue", alpha=0.5)
ax[0].plot(date_sitka, low_sitka, c="blue", alpha=0.5)
ax[0].plot(date_sitka, high_sitka, c="red", alpha=0.5)
ax[1].plot(date_dv, high_dv, c="red", alpha=0.5)


ax[0].set_title("Temperature comparison between SITKA AIRPORT, AK US AND DEATH VALLEY, CA US\nDEATH VALLEY, CA US", fontsize =8)
ax[1].set_title("SITKA AIRPOT, AK US", fontsize=8)




ax[1].fill_between(date_dv, high_dv, low_dv, facecolor = 'blue', alpha=0.1)
ax[0].fill_between(date_sitka, high_sitka, low_sitka, facecolor = 'blue', alpha=0.1)

fig.autofmt_xdate()

#plt.ylabel("Temperature (F)", fontsize=8)

#plt.tick_params(axis="both",labelsize=8)

#subplots()
plt.show()
