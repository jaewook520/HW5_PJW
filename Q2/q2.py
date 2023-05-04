import csv

def main():
    f = open('q2.csv','r')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    temp_diff_min = 10000
    temp_diff_max = 0
    day_min = ''
    day_max = ''
    
    for row in data:
        if(row[2] != '' and row[3] != '' and row[4] != ''): 
            if (temp_diff_min > float(row[4]) - float(row[3])):
                temp_diff_min = float(row[4]) - float(row[3])
                day_min = row[0]
                
            if (temp_diff_max < float(row[4]) - float(row[3])):
                temp_diff_max = float(row[4]) - float(row[3])
                day_max = row[0]
    f.close()
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temperature Variation: {0:s}".format(day_max))
    print("Maximum Temperature Difference: {0:.1f} Celsius".format(temp_diff_max))
    print("Day with the Smallest Temperature Variation: {0:s}".format(day_min))
    print("Minimum Temperature Difference: {0:.1f} Celsius".format(temp_diff_min))
    
if __name__=="__main__":
    main()
