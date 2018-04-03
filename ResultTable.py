"""
This program will order the rugby teams and presents it in a neat format
"""

#Reading Text File
def read_file(filename):
    with open(filename) as f:
        readlines = f.read().splitlines()
    file_out = [line.split(',') for line in readlines]
    for item in file_out:
        for index in range(1,len(item)):
            item[index] = int(item[index].strip())

    f.close()

    return file_out

#Ordering teams
def insertion_sort(a_list):
    for index_number in range(1, len(a_list)):
        item_to_insert = a_list[index_number]
        element = a_list[index_number][2]
        index = index_number - 1
        while index >= 0 and a_list[index][2] <= item_to_insert[2]:
            #Ideal scenario -> Item to insert is not equal to current item
            if a_list[index][2] != item_to_insert[2]: 
                if a_list[index][2] < item_to_insert[2]:
                    a_list[index + 1], a_list[index] = a_list[index], a_list[index + 1]

            #Orders the list by the next category if the points are equal
            elif a_list[index][2] == item_to_insert[2]:
                if (a_list[index][3]-a_list[index][4]) < (item_to_insert[3]-item_to_insert[4]):
                    a_list[index + 1], a_list[index] = a_list[index], a_list[index + 1]                    
                elif (a_list[index][3]-a_list[index][4]) == (item_to_insert[3]-item_to_insert[4]):
                    if a_list[index][4] < item_to_insert[4]:
                        a_list[index+1], a_list[index] = a_list[index], a_list[index + 1]
                    else:
                        item_to_insert = a_list[index]
                else:
                    item_to_insert = a_list[index]
                   
            index -= 1    
                
        #Moving to new item to insert
        a_list[index+1] = item_to_insert

def main_print(lines):
    print("    Team         Conference Points  Diff   Goals")
    #Loops through the lines list to and formats into columns
    for i in range(len(lines)):
        print("{0:>2}. {1:<14} {2:^10} {3:>2}   {4:>4} {5:5}:{6}".format(i+1, lines[i][0], lines[i][1], lines[i][2], (lines[i][3]-lines[i][4]), lines[i][3], lines[i][4]))

#Prints the teams ordered by conference
def sub_print(lines):
    
    print()
    conf_1, conf_2, conf_3, conf_4 = [], [], [], []
    #Contains all the conferences, ordered by conference number
    largest_list = []
    for i in range(len(lines)):
        if lines[i][1] == 1:
            conf_1.append(lines[i])
        elif lines[i][1] == 2:
            conf_2.append(lines[i])        
        elif lines[i][1] == 3:
            conf_3.append(lines[i])
        else:
            conf_4.append(lines[i])
    largest_list.append(conf_1)
    largest_list.append(conf_2)
    largest_list.append(conf_3)
    largest_list.append(conf_4)

    #Loopst through the largest_list to display the results
    for i in range(len(largest_list)):
        print(" Conference",i+1)
        print("    Team         Conference Points  Diff   Goals")
        for j in range(len(largest_list[i])):
            print("{0:>2}. {1:<14} {2:^10} {3:>2}   {4:>4} {5:5}:{6}".format(j+1, largest_list[i][j][0], \
                                                                             largest_list[i][j][1], largest_list[i][j][2], (largest_list[i][j][3]-largest_list[i][j][4]), \
                                                                             largest_list[i][j][3], largest_list[i][j][4]))
        print()

def main():
    lines = read_file('table1.txt')
    insertion_sort(lines)
    main_print(lines)
    sub_print(lines)


main()
