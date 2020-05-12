# https://liveyourit.tistory.com/57
import os
import traceback

from konlpy.tag import Okt
from openpyxl import load_workbook
import time
import os

start = time.time()  # 시작 시간 저장
noun = []
nouncount = []
okt = Okt()
file_list_excel = []
path = "./excel"
if os.path.isdir(path):
    file_list = os.listdir(path)
    file_list_excel = [file for file in file_list if file.endswith(".xlsx")]
    if file_list:
        print("file_list: {}".format(file_list_excel))
    else:
        print("excel file not exist")
else:
    print("input your excel file in 'excel' forder")

for excel_name in file_list_excel:
    excel_filename = "./excel/"+excel_name
    # 엑셀 파일일 경우
    load_wb = load_workbook(excel_filename , data_only=True)
    # load_ws = load_wb['rudrl1119']
    for sheet in load_wb:
        for row in sheet.rows:
            for cell in row:
                try:
                    for i in okt.nouns(cell.value):
                        if i in noun:
                            nouncount[noun.index(i)] += 1
                        else:
                            noun.append(i)
                            nouncount.append(1)
                except:
                    traceback.print_exc()

        noun_list = {}
        for i in noun:
            noun_list.setdefault(i, nouncount[noun.index(i)])

        noun_list_sort = sorted(noun_list.items(), key=lambda x: x[1], reverse=True)

    print("제외 단어 처리 전")
    print(noun_list_sort)
    noun_list_sort = dict(noun_list_sort)
    # except_word = open("1차결과제외단어.txt", mode='rt', encoding='utf-8')
    # for i in except_word.readlines():
    #     i = i.replace('\n', '')
    #     del noun_list_sort[i]

    print("제외 단어 처리 후")
    print(noun_list_sort)
    for i in noun_list_sort:
        wordfilename = "word/"+i + ".txt"
        if os.path.isfile(wordfilename):
            print("파일존재")
            wordfile = open(wordfilename, 'a')
            wordfile.write(excel_filename+'\n')
            wordfile.close()

        else:
            print("파일없음 생성필요")
            wordfile = open(wordfilename, 'w')
            wordfile.write(excel_filename+'\n')
            wordfile.close()

    print("소요시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
