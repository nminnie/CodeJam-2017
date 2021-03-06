import numpy as np   # for plotting
import matplotlib.pyplot as plt   # for plotting
import csv  # for parsing the data set
import math

# class represent a bike ride
class Ride:
    time = -1  # 0=4:00 to 11:59, 1=12:00 to 18:59, 2=19:00 to 3:59
    day = -1  # 0=weekday, 1=weekend
    season = -1  # 0=winter, 1=summer
    startLat = 0.0
    startLong = 0.0
    endLat = 0.0
    endLong = 0.0

def main():
    # specify the min & max longitudes and latitudes for the plot
    xMin = 40.67
    xMax = 40.78
    yMin = -74.04
    yMax = -73.93
    # parse the data set for January (winter)
    rides = []
    with open('2014-01 - Citi Bike trip data.csv') as f:   # get data from data set
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            x = Ride()
            x.season = 0
            starttime = row['starttime']
            sDate, sTime = starttime.split(" ")
            sHour, sMin = sTime.split(":")
            sHour = int(sHour)
            # classify rides by time of the day
            if (4 <= sHour and sHour < 12):       # 0 = morning
                x.time = 0
            elif (12 <= sHour and sHour < 19):    # 1 = afternoon
                x.time = 1
            else:                                 # 2 = night
                 x.time = 2
            sMonth, sDay, sYear = sDate.split("/")
            sDay = int(sDay)
            # classify rides by day of the week 
            if (sDay % 7 == 4 or sDay % 7 == 5):   # 1 = weekend
                x.day = 1
            else:                                  # 0 = weekday
                x.day = 0
            
            # get the longitude and latitude of the starting and ending points of the rides
            startLat = row['start station latitude']
            startLat = float(startLat)
            x.startLat = startLat
            startLong = row['start station longitude']
            startLong = float(startLong)
            x.startLong = startLong
            endLat = row['end station latitude']
            endLat = float(endLat)
            x.endLat = endLat
            endLong = row['end station longitude']
            endLong = float(endLong)
            x.endLong = endLong
            # if the ride is within our map's range, add it to 'ride' list
            if (xMin <= x.startLat <= xMax and yMin <= x.startLong <= yMax): 
                rides.append(x)

    # do the same to July data set (summer)
    with open('2014-07 - Citi Bike trip data.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            x = Ride()
            x.season = 1
            starttime = row['starttime']
            sDate, sTime = starttime.split(" ")
            sHour, sMin = sTime.split(":")
            sHour = int(sHour)
            # 0 = morning, 1 = afternoon, 2 = night
            if (4 <= sHour and sHour < 12):
                x.time = 0
            elif (12 <= sHour and sHour < 19):
                x.time = 1
            else:
                x.time = 2
            sMonth, sDay, sYear = sDate.split("/")
            sDay = int(sDay)
            # 0 = weekday, 1 = weekend
            if (sDay % 7 == 5 or sDay % 7 == 6):
                x.day = 1
            else:
                x.day = 0
            startLat = row['start station latitude']
            startLat = float(startLat)
            x.startLat = startLat
            startLong = row['start station longitude']
            startLong = float(startLong)
            x.startLong = startLong
            endLat = row['end station latitude']
            endLat = float(endLat)
            x.endLat = endLat
            endLong = row['end station longitude']
            endLong = float(endLong)
            x.endLong = endLong
            if (xMin <= x.startLat <= xMax and yMin <= x.startLong <= yMax):
                rides.append(x)
    
    # declare lists for different times,  days, seasons
    # these will be filled later
    # all rides = #all year, all week, all day -- this is the 'rides' list
    allmorning = []  # all year, all week, morning
    allafternoon = []  # all year, all week, afternoon
    allnight = []  # all year, all week, night
    weekdayallday = []  # all year, weekday, allday
    weekdaymorning = []  # all year, weekday, morning
    weekdayafternoon = []  # all year, weekday, afternoon
    weekdaynight = []  # all year, weekday, night
    weekendallday = []
    weekendmorning = []
    weekendafternoon = []
    weekendnight = []
    winter_AllWeek_allday = []
    winter_AllWeek_morning = []
    winter_AllWeek_afternoon = []
    winter_AllWeek_night = []
    winter_Weekday_allday = []
    winter_Weekday_morning = []
    winter_Weekday_afternoon = []
    winter_Weekday_night = []
    winter_Weekend_allday = []
    winter_Weekend_morning = []
    winter_Weekend_afternoon = []
    winter_Weekend_night = []
    summer_AllWeek_allday = []
    summer_AllWeek_morning = []
    summer_AllWeek_afternoon = []
    summer_AllWeek_night = []
    summer_Weekday_allday = []
    summer_Weekday_morning = []
    summer_Weekday_afternoon = []
    summer_Weekday_night = []
    summer_Weekend_allday = []
    summer_Weekend_morning = []
    summer_Weekend_afternoon = []
    summer_Weekend_night = []
    
    # file the lists with the bike rides corresponding to their time, day, and season
    for i in range(0, len(rides)):
        x = rides[i]
        if (x.time == 0):
            allmorning.append(x)
        elif (x.time == 1):
            allafternoon.append(x)
        elif (x.time == 2):
            allnight.append(x)
        if (x.day == 0):  # weekday
            weekdayallday.append(x)
            if (x.time == 0):
                weekdaymorning.append(x)
            elif (x.time == 1):
                weekdayafternoon.append(x)
            elif (x.time == 2):
                weekdaynight.append(x)
        if (x.day == 1):  # weekend
            weekendallday.append(x)
            if (x.time == 0):
                weekendmorning.append(x)
            elif (x.time == 1):
                weekendafternoon.append(x)
            elif (x.time == 2):
                weekendnight.append(x)
        if (x.season == 0):  # winter
            # all day
            winter_AllWeek_allday.append(x)
            if (x.time == 0):
                winter_AllWeek_morning.append(x)
            elif (x.time == 1):
                winter_AllWeek_afternoon.append(x)
            elif (x.time == 2):
                winter_AllWeek_night.append(x)
            # weekday
            if (x.day == 0):
                winter_Weekday_allday.append(x)
                if (x.time == 0):
                    winter_Weekday_morning.append(x)
                elif (x.time == 1):
                    winter_Weekday_afternoon.append(x)
                elif (x.time == 2):
                    winter_Weekday_night.append(x)
            # weekend
            if (x.day == 1):
                winter_Weekend_allday.append(x)
                if (x.time == 0):
                    winter_Weekend_morning.append(x)
                elif (x.time == 1):
                    winter_Weekend_afternoon.append(x)
                elif (x.time == 2):
                    winter_Weekend_night.append(x)
        if (x.season == 1):  # summer
            # all day
            summer_AllWeek_allday.append(x)
            if (x.time == 0):
                summer_AllWeek_morning.append(x)
            elif (x.time == 1):
                summer_AllWeek_afternoon.append(x)
            elif (x.time == 2):
                summer_AllWeek_night.append(x)
            # weekday
            if (x.day == 0):
                summer_Weekday_allday.append(x)
                if (x.time == 0):
                    summer_Weekday_morning.append(x)
                elif (x.time == 1):
                    summer_Weekday_afternoon.append(x)
                elif (x.time == 2):
                    summer_Weekday_night.append(x)
            # weekend
            if (x.day == 1):
                summer_Weekend_allday.append(x)
                if (x.time == 0):
                    summer_Weekend_morning.append(x)
                elif (x.time == 1):
                    summer_Weekend_afternoon.append(x)
                elif (x.time == 2):
                    summer_Weekend_night.append(x)
    
    #declare variables for plotting graph
    sum = 0
    stations = 80
    regionDensity = []
    numInRegion = []
    bikeStops = []

    xSize = 10
    ySize = 10

    # dictionary to help create .png files with appropriate names
    dict = {'rides': "ALLDAY_ALLWK_ALLYR",
            'allmorning': "day_ALLWK_ALLYR",
            'allafternoon': "eve_ALLWK_ALLYR",
            'allnight': "night_ALLWK_ALLYR",

            'weekdayallday': "ALLDAY_WKDAY_ALLYR",
            'weekdaymorning': "day_WKDAY_ALLYR",
            'weekdayafternoon': "eve_WKDAY_ALLYR",
            'weekdaynight': "night_WKDAY_ALLYR",

            'weekendallday': "ALLDAY_WKEND_ALLYR",
            'weekendmorning': "day_WKEND_ALLYR",
            'weekendafternoon': "eve_WKEND_ALLYR",
            'weekendnight': "night_WKEND_ALLYR",

            'winter_AllWeek_allday': "ALLDAY_ALLWK_WINTER",
            'winter_AllWeek_morning': "day_ALLWK_WINTER",
            'winter_AllWeek_afternoon': "eve_ALLWK_WINTER",
            'winter_AllWeek_night': "night_ALLWK_WINTER",

            'winter_Weekday_allday': "ALLDAY_WKDAY_WINTER",
            'winter_Weekday_morning': "day_WKDAY_WINTER",
            'winter_Weekday_afternoon': "eve_WKDAY_WINTER",
            'winter_Weekday_night': "night_WKDAY_WINTER",

            'winter_Weekend_allday': "ALLDAY_WKEND_WINTER",
            'winter_Weekend_morning': "day_WKEND_WINTER",
            'winter_Weekend_afternoon': "eve_WKEND_WINTER",
            'winter_Weekend_night': "night_WKEND_WINTER",

            'summer_AllWeek_allday': "ALLDAY_ALLWK_SUMMER",
            'summer_AllWeek_morning': "day_ALLWK_SUMMER",
            'summer_AllWeek_afternoon': "eve_ALLWK_SUMMER",
            'summer_AllWeek_night': "night_ALLWK_SUMMER",

            'summer_Weekday_allday': "ALLDAY_WKDAY_SUMMER",
            'summer_Weekday_morning': "day_WKDAY_SUMMER",
            'summer_Weekday_afternoon': "eve_WKDAY_SUMMER",
            'summer_Weekday_night': "night_WKDAY_SUMMER",

            'summer_Weekend_allday': "ALLDAY_WKEND_SUMMER",
            'summer_Weekend_morning': "day_WKEND_SUMMER",
            'summer_Weekend_afternoon': "eve_WKEND_SUMMER",
            'summer_Weekend_night': "night_WKEND_SUMMER",
            }

    listMake = allmorning
    
    # create .png files 
    filename = dict['allmorning'] + ".png"
    
    # begin plotting
    x = []
    y = []

    for i in range(0, len(listMake)):  # Adds new elements
        x.append(listMake[i].startLat)
        y.append(listMake[i].startLong)

    # good range: [40.4, 41.0], [-74.4, -73.6]
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=(xSize, ySize), range=[[40.63, 40.81], [-74.05, -73.9]])
    extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]
    for i in range(0, xSize):
        for j in range(0, ySize):
            regionDensity.append(heatmap[i, j])
            sum += heatmap[i, j]
    
    # Turn regionDensity into a proportion
    for i in range(0, xSize):
        for j in range(0, ySize):
            regionDensity[i * xSize + j] = regionDensity[i * xSize + j] / sum
            numInRegion.append(stations * regionDensity[i * xSize + j])
            numInRegion[i * xSize + j] = round(numInRegion[i * xSize + j])
    xSizeRes = 100
    ySizeRes = 100
    ratioX = round(xSizeRes / xSize)
    ratioY = round(ySizeRes / ySize)
    nodeLoc = []
    temp = []
    heatmapRes, xedges, yedges = np.histogram2d(x, y, bins=(xSizeRes, ySizeRes),
                                                range=[[40.63, 40.81], [-74.05, -73.9]])
    plt.clf()
    # interpolation = 'nearest',
    plt.imshow(heatmapRes, extent=extent, interpolation='nearest', origin='lower')
    # plt.show()
    factor = 0
    for z in range(0, xSize * ySize):
        nodeLoc.append([])
    for row in range(0, xSizeRes):
        for col in range(0, ySizeRes):
            block = math.floor(row / ratioX) + math.floor(col / ratioY) + factor
            nodeLoc[block].append(round(heatmapRes[row][col]))
            if ((row * xSizeRes + col + 1) % (ratioY * ratioX * xSize) == 0):
                factor += (xSize - 1)
                # print (nodeLoc)
    tempLocValues = []
    bikeStopsX = []
    bikeStopsY = []
    for i in range(0, int(xSize * ySize)):
        nodeLoc[i].sort()
        for j in range(0, int(numInRegion[i])):
            tempLocValues.append(nodeLoc[i].pop())
            # Go through heatmap to find the positions where this occurs
            for k in range(0, xSizeRes):
                for l in range(0, ySizeRes):
                    if (heatmapRes[k][l] == tempLocValues[j]):
                        bikeStopsX.append(k / 550 + 40.625)
                        bikeStopsY.append(l / 550 - 74.06)
                        # print(bikeStopsY.append(l))
                        # bikeStops[len(bikeStops)] = [heatmapRes.index(tempLocValues[j])]
        tempLocValues = []
    latIn = 0
    longIn = 0
    distanceArr = []
    bikeStopDtn = []
    for i in range(0, len(bikeStopsX)):
        bikeStopDtn.append(0)
    refArray = []  # reference array that contains [lat, long]
    refArrayNode = []  # corresponds with refArray. Shows node
    for i in range(0, len(bikeStopsX)):
        refArray = []
    indexVal = 0

    for j in range(0, len(x)):
        print (j)
        for i in range (0, len(bikeStopsX)):
            distanceArr.append(distance(x[j], y[j], bikeStopsX[i], bikeStopsY[i]))
        minDistance = min(distanceArr)
        minPos = distanceArr.index(minDistance)
        bikeStopDtn[minPos]+= 1
        distanceArr = []

    ifile = open('NYC-vehicle-collisions.csv', "r")
    reader = csv.reader(ifile, delimiter=",")
    rownum = 0
    a = []
    for row in reader:
        a.append(row)
        rownum += 1
    ifile.close()
    x = []
    y = []
    xMin = 40.67
    xMax = 40.78
    yMin = -74.04
    yMax = -73.93
    for z in range(1, len(a)):
        if a[z][5] != "" and a[z][6] != "" and xMin <= float(a[z][5]) <= xMax and yMin <= float(a[z][6]) <= yMax:
            x.append(float(a[z][5]))
            y.append(float(a[z][6]))
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=(1000, 1000), range=[[xMin, xMax], [yMin, yMax]])
    extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]

    for i in range (0, len(bikeStopDtn)):
        bikeStopDtn[i] = math.sqrt(bikeStopDtn[i])
    plt.clf()
    plt.imshow(heatmap, extent=extent, cmap="gray", origin='lower', vmax=1)
    plt.scatter(bikeStopsY, bikeStopsX, s = bikeStopDtn, c = bikeStopDtn, cmap = "Pastel1", marker = 'o', edgecolors='black', linewidths=1)
    plt.savefig(filename, format='png', dpi = 1200, transparent = True)
    plt.show()


def distance(x, y, refX, refY):
    value = math.sqrt((x - refX) ** 2 + (y - refY) ** 2)
    return value

main()

