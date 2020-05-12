# https://liveyourit.tistory.com/57
import os
import traceback

from konlpy.tag import Okt
import olefile

import time

start = time.time()  # 시작 시간 저장
noun = []
nouncount = []
okt = Okt()
original_filename = "1.xlsx"
# 한글 파일일 경우

f = olefile.OleFileIO('1.hwp')
encoded_text = f.openstream('PrvText').read()
decoded_text = encoded_text.decode('UTF-16')
print(decoded_text)
'''
# 엑셀 파일일 경우
from openpyxl import load_workbook
load_wb = load_workbook(original_filename, data_only=True)
load_ws = load_wb['rudrl1119']
for row in load_ws.rows:
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
'''

try:
    for i in okt.nouns(decoded_text):
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
print("단어")
print(noun_list_sort)
for i in noun_list_sort:
    wordfilename = "word/"+i[0] + ".txt"
    if os.path.isfile(wordfilename):
        print("파일존재")
        wordfile = open(wordfilename, 'a')
        wordfile.write(original_filename+'\n')
        wordfile.close()

    else:
        print("파일없음 생성필요")
        wordfile = open(wordfilename, 'w')
        wordfile.write(original_filename+'\n')
        wordfile.close()

print("소요시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

'''
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
        wordfile.write(original_filename+'\n')
        wordfile.close()

    else:
        print("파일없음 생성필요")
        wordfile = open(wordfilename, 'w')
        wordfile.write(original_filename+'\n')
        wordfile.close()

print("소요시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
'''