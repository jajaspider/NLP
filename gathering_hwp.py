# https://liveyourit.tistory.com/57
import os
import traceback
from konlpy.tag import Okt
import olefile
import time
import network_hwp as nh
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc
from networkx.drawing.nx_pydot import to_pydot
from IPython.core.display import Image, display

start = time.time()  # 시작 시간 저장
noun = []
nouncount = []
okt = Okt()


# 한글 파일일 경우
file_list_excel = []
path = "./hwp"
if os.path.isdir(path):
    file_list = os.listdir(path)
    file_list_excel = [file for file in file_list if file.endswith(".hwp")]
    if file_list:
        print("file_list: {}".format(file_list_excel))
    else:
        print("excel file not exist")
else:
    print("input your excel file in 'hwp' forder")

for hwp_name in file_list_excel:
    hwp_filename = "./hwp/" + hwp_name
    f = olefile.OleFileIO(hwp_filename)
    encoded_text = f.openstream('PrvText').read()
    decoded_text = encoded_text.decode('UTF-16')
    print(decoded_text)

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
        wordfilename = "word/" + i[0] + ".txt"
        if os.path.isfile(wordfilename):
            print("파일존재")
            wordfile = open(wordfilename, 'a')
            wordfile.write(hwp_filename + '\n')
            wordfile.close()

        else:
            print("파일없음 생성필요")
            wordfile = open(wordfilename, 'w')
            wordfile.write(hwp_filename + '\n')
            wordfile.close()

nhcom = nh.get_combination(noun)
print(nhcom)
g1 = nx.Graph()
for i in noun:
    g1.add_node(i)
for j in nhcom:
    g1.add_edge(j[0], j[1])

path = './NanumGothic.otf'
font_name = fm.FontProperties(fname=path, size=50).get_name()
print(font_name)
plt.rc('font', family=font_name)

plt.subplot(111)
nx.draw(g1, with_labels=True, node_size=5, width=0.05)
plt.savefig("networkGraph.png")
plt.show()

print("소요시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
