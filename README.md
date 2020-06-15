# NLP

NLP classifies the data of documents after statistics through natural language processing.

# 처리가능한 파일
현재는 hwp,pdf 만 처리 가능
#

# V1.23
V1.22에서는 'complete', 'merge_1', 'merge_2'와 같이 하나의 폴더에 작업물을 모으게되어있었으나 각각 연도별 폴더를 생성하여 작업물을 기록하도록 함

# V1.22
V1.21에서 속도저하 이슈가 발생  
-print 제거  
-파일을 열고닫고 방식에서 열어두고, 모두 작성 후 닫고 저장  
-time 관련 데이터 모두 주석처리  

# V1.21
V1.1에서 생성된 데이터를 파일번호가 같은것으로 합병  
의미없는 한 글자 데이터 삭제  
항상 출현하는 임의의 데이터 삭제  
-> merge1.py  
위의 행동으로 추가된 데이터를 월별로 정리하고, csv 파일로 정리할 수 있도록 구현  
-> merge2.py  


# V1.1
전체적으로 구조 변경  
init 실행시 필요한 폴더 생성  
read_pdf_PDFMINER 매개변수에 파일경로(PDF) 지정 시 text만 반환  
html2text 매개변수에 파일경로(html) 지정 시 text만 반환  
txt_processing 매개변수에 처리에 필요한 확장자,파일경로 지정 시 NLP처리하여 complete 경로에 반환, 추가로 text데이터는 temp에 임시저장  
get_directory_file_list 처리에 필요한 경로 지정 시 재귀식으로 파일 데이터 전부 확인  

# V1.0
hwp, xlsx 파일의 데이터 처리  
README 작성
