import csv

def main():
    f = open('q1.csv','r')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    average_temp = 0.0
    average_min_temp = 0.0
    average_max_temp = 0.0
    cnt=0
    for row in data:
        if(row[2] != '' and row[3] != '' and row[4] != ''): 
            average_temp += float(row[2])
            average_min_temp += float(row[3])
            average_max_temp += float(row[4])
            cnt += 1
    f.close()
    average_temp /= cnt
    average_min_temp /= cnt
    average_max_temp /= cnt
    average_temp = round(average_temp,2)
    average_min_temp = round(average_min_temp, 2)
    average_max_temp = round(average_max_temp, 2)

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: {0:.2f} Celsius".format(average_temp,2))
    print("Average Minimum Temperature: {0:.2f} Celsius".format(average_min_temp,2))
    print("Average Maximum Temperature: {0:.2f} Celsius".format(average_max_temp,2))

if __name__=="__main__":
    main()
