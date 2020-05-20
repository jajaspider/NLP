import time
from konlpy.tag import Okt
from openpyxl import load_workbook

start = time.time()  # 시작 시간 저장
noun = []
nouncount = []
okt = Okt()

# 연결 파일 명 정리
excel_filename = "template.xlsx"
load_wb = load_workbook(excel_filename, data_only=True)
# load_ws = load_wb['rudrl1119']
for sheet in load_wb:
    for row in sheet.rows:
        if "xlsx" in row[3].value:
            print(row[3].value)
