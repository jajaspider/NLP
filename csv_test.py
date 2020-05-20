import os
import re

path = "./csv"
if os.path.isdir(path):
    file_list = os.listdir(path)
    file_list_excel = [file for file in file_list if file.endswith(".csv")]
    if file_list:
        print("file_list: {}".format(file_list_excel))
    else:
        print("excel file not exist")
else:
    print("input your excel file in 'excel' forder")

for i in file_list_excel:
    # print("create table " + i + "(")
    print(i)
    f = open("./csv/" + i, 'r', encoding='CP949')
    for _ in range(0, 1):
        line = f.readline()
        for j in line.split("|"):
            rugal = re.compile('[a-zA-Zㄱ-힣]+').findall(j)
            for k in rugal:
                print(k)
                # print(k+"                   char(5),")
    # print(");")
    print("")
'''
f = open("./csv/" + "T-.csv", 'r', encoding='CP949')
for _ in range(0, 10):
    line = f.readline()
    print(line)
'''
