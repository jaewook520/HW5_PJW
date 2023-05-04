import csv

def main():
    f = open('q4.csv','r')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    station_sum = [0 for i in range(4)]
    station_name_max = ['' for i in range(4)]
    station_name_min = ['' for i in range(4)]
    station_max = [0 for i in range(4)]
    station_min = [1000000000 for i in range(4)]
    station = [0 for i in range(4)]

    for row in data:
        if(row[1] == "1호선"):
            station_sum[0] = int(row[4]) + int(row[5])
            if(station_sum[0] > station_max[0]):
                station_max[0] = station_sum[0]
                station_name_max[0] = row[3]
            elif(station_sum[0] < station_min[0]):
                station_min[0] = station_sum[0]
                station_name_min[0] = row[3]
        elif(row[1] == "2호선"):
            station_sum[1] = int(row[4]) + int(row[5])
            if(station_sum[1] > station_max[1]):
                station_max[1] = station_sum[1]
                station_name_max[1] = row[3]
            elif(station_sum[1] < station_min[1]):
                station_min[1] = station_sum[1]
                station_name_min[1] = row[3]
        elif(row[1] == "3호선"):
            station_sum[2] = int(row[4]) + int(row[5])
            if(station_sum[2] > station_max[2]):
                station_max[2] = station_sum[2]
                station_name_max[2] = row[3]
            elif(station_sum[2] < station_min[2]):
                station_min[2] = station_sum[2]
                station_name_min[2] = row[3]
        elif(row[1] == "4호선"):
            station_sum[3] = int(row[4]) + int(row[5])
            if(station_sum[3] > station_max[3]):
                station_max[3] = station_sum[3]
                station_name_max[3] = row[3]
            elif(station_sum[3] < station_min[3]):
                station_min[3] = station_sum[3]
                station_name_min[3] = row[3]
        else:
            continue
        
    f.close()

    print("*** Subway Report for Seoul on March 2023 ***")
    print("Line 1:")
    print("Busiest Station: {0:s} ({1:d})".format(station_name_max[0], station_max[0]))
    print("Least used Station: {0:s} ({1:d})".format(station_name_min[0], station_min[0]))
    print("Line 2:")
    print("Busiest Station: {0:s} ({1:d})".format(station_name_max[1], station_max[1]))
    print("Least used Station: {0:s} ({1:d})".format(station_name_min[1], station_min[1]))
    print("Line 3:")
    print("Busiest Station: {0:s} ({1:d})".format(station_name_max[2], station_max[2]))
    print("Least used Station: {0:s} ({1:d})".format(station_name_min[2], station_min[2]))
    print("Line 4:")
    print("Busiest Station: {0:s} ({1:d})".format(station_name_max[3], station_max[3]))
    print("Least used Station: {0:s} ({1:d})".format(station_name_min[3], station_min[3]))

if __name__=="__main__":
    main()
