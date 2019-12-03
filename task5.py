#script from hmw 4
import re
import os
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
import os
import pandas as pd
filepath = os.path.join("/", "Users", "gkiar",
                        "Desktop", "diabetes.rwrite1.txt")
with open("C:\Users\Rogerio\Documents\Big Data Diploma\CEBD 1100\Homework\Homework week 5 oct_13_2019\Dataset\hwk4_data\breast-cancer-wisconsin.data", "r") as fHandler:
    # read next line
    line = fHandler.readline()
    # checking if line is not empty
    while line:
        print(line.strip())
        line = fHandler.readline()
        #print(data)
        print(data[:5].to_csv())

#file_object = open("C:\Users\Rogerio\Documents\Big Data Diploma\CEBD 1100\Homework\Homework week 5 oct_13_2019\Dataset\hwk4_data\breast-cancer-wisconsin.data")
#data = file_object.read()

#print(data)

#file_object.close()


def convert_type(element):
    # case 2: empty string, should be ignored
    if element == "": # len(element) == 0
        return None
        # case 4: is a # with no., should be integer
    try:
        return int(element)
    except ValueError:
        # case 3: has a . but is a #, should be float
        try:
            return float(element)
        except ValueError:
            # case 1: is a string, should remain string
            return element

# managing separators
df = pd.read_csv ("C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\Homework\\Homework week 5 oct_13_2019\\Dataset\\hwk4_data\\breast-cancer-wisconsin.data")
df = pd.read_table ("C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\Homework\\Homework week 5 oct_13_2019\\Dataset\\hwk4_data\\breast-cancer-wisconsin.data, sep = ",", " " index_col = column_x") 

filenames = ["C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\Homework\\Homework week 5 oct_13_2019\\Dataset\\hwk4_data\\breast-cancer-wisconsin.data",
            "C:\\Users\\Rogerio\\Documents\\Big Data Diploma\\CEBD 1100\Homework\\Homework week 5 oct_13_2019\\Dataset\\hwk4_data\\breast-cancer-wisconsin.names"]
if len(filenames) > 1:
    data = open(filenames[0]. 'r')
    names = open(filenames[1], 'r')
else:
    data = open(filenames[0], 'r')
    names = None
my_read_data = data.read()
print(my_read_data)

my_read_dataS = my_read_data.split('\n')

outer_list = []
for row in my_read_dataS:
    row_list = []
    for element in row.split(" "):
        new_element=convert_type(element)
        if new_element is not None:
            row_list.append(new_element)
        print(element, end = "\t")
        print(new_element, type(new_element))
    print(row_list)
    if len(row_list) > 0:
        outer_list += [row_list]

    our_dictionary = {}

    for location, column_headings in enumerate(outer_list[0]):
        print(column_headings)
        our_dictionary[column_headings] = list()
        for row in outer_list[1:]:
            our_dictionary[column_headings] += [row[location]]
        print(our_dictionary)

# adapting Script to the homework 5
# ploting the columns

import pandas as pd

import argparse

import matplotlib.pyplot as plt


pip3 install --user matplotlib

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

data = pd.read_csv('file path.csv', index_col = 'Group 1'

# Extract year from last 4 characters of each column name
years = data.columns.str.strip('gdpPercap_')
# Convert year values to integers, saving results back to dataframe
data.columns = years.astype(int)

data.loc['Group 1'].plot()

data.T.plot()
plt.ylabel('Group 1')

plt.style.use('ggplot')
data.T.plot(kind='bar')
plt.ylabel('Group 2')

plt.plot(x, y)

# comparing the csv files

import sys
import argparse
import csv

def get_dataset (f):
    return set(map(tuple, csv.reader(f)))

def main(f1, f2, outfile, sorting_column):
    set1 = get_dataset(f1)
    set2 = get_dataset(f2)
    different = set1 ^ set2

    output = csv.writer(outfile)

    for row in sorted(different, key=lambda x: x[sorting_column], reverse=True):
        output.writerow(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('infile', nargs=2, type=argparse.FileType('r'))
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument('-sc', '--sorting-column', nargs='?', type=int, default=0)

    args = parser.parse_args()

    main(*args.infile, args.outfile, args.sorting_column)

# open two files at the same time
with open("C:\Users\Rogerio\Documents\Big Data Diploma\CEBD 1100\Homework\Homework week 5 oct_13_2019\Dataset\hwk4_data\breast-cancer-wisconsin.data", "r")
            as file_obj_2, open("C:\Users\Rogerio\Documents\Big Data Diploma\CEBD 1100\Homework\Homework week 5 oct_13_2019\Dataset\hwk4_data\breast-cancer-wisconsin.names", "r")
            as file_objÉ1:
            data = file_obj_1.read()
            file_obj_2.read()

print(df[:5].to_csv())


# to deal with delimiters
reader = csv.reader(csvfile, delimiter="\t")
lst = []
for i, row in enumerate(reader):
    if i == 0:
        continue  # your custom header-handling code here
    lst.append(int(row[0].replace(',', '')))

