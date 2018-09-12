import re

lst = []

def read_line():
    with open("test.txt", "r") as f:                                    #opens the file and reads multiple lines
        for line in f:
            find_float = float(re.search(r'\d+\.\d+', line).group())    #finds the float in the document
#            print(find_float)
            lst.append(find_float)                                      #appends the floats to the list



def count_floats(lst):
    counted = sum(map(float, lst))
    print(counted)


read_line()
count_floats(lst)