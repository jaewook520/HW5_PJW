import csv

def find_line(line):
    if line=="1호선":
        return 1
    elif line=="2호선":
        return 2
    elif line=="3호선":
        return 3
    elif line=="4호선":
        return 4
    elif line=="5호선":
        return 5
    elif line=="6호선":
        return 6
    elif line=="7호선":
        return 7
    elif line=="8호선":
        return 8
    elif line=="9호선":
        return 9
    else: return 0

def main():
    f = open('q3.csv','r')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    subway = [0 for i in range(9)]
    
    for row in data:
        line_num = find_line(row[1])
        if(line_num != 0):
            subway[line_num - 1] = subway[line_num - 1] + int(row[4]) + int(row[5])
    f.close()

    print("*** Subway Report for Seoul on March 2023 ***")
    subway_sorted = subway[:]
    subway_sorted.sort()
    print("1st Busiest Line: Line {0:d} ({1:d})".format(subway.index(subway_sorted[8])+1,subway_sorted[8]))
    print("2nd Busiest Line: Line {0:d} ({1:d})".format(subway.index(subway_sorted[7])+1,subway_sorted[7]))
    print("1st Least used Line: Line {0:d} ({1:d})".format(subway.index(subway_sorted[0])+1,subway_sorted[0]))
    print("2nd Least used Line: Line {0:d} ({1:d})".format(subway.index(subway_sorted[1])+1,subway_sorted[1]))
    
if __name__=="__main__":
    main()
