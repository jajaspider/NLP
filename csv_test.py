import os

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
'''
for i in file_list_excel:
    print(i)
    
    f = open("./csv/" + i, 'r', encoding='CP949')
    for _ in range(0, 1):
        line = f.readline()
        print(line)
'''
f = open("./csv/" + "TB_MTA_FRIG_화재안전특별조사와 재난번호_연결 202005121020.csv", 'r', encoding='CP949')
for _ in range(0, 10):
    line = f.readline()
    print(line)
