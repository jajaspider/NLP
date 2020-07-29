# NLP

NLP classifies the data of documents after statistics through natural language processing.

# 처리가능한 파일
현재는 hwp,pdf 만 처리 가능
#

# Psuedo code
    get filename of folder
    get extends of filename
    if extends == "hwp"
      do Convert hwp file to html. // When reading hwp files directly, there is a problem that cannot read the whole
      Extract textdata through parsing from html
    elif extends == "pdf"
      Extract textdata from pdf file through read_pdf_pdfminer function
    
    #text_processing
    get oktdata by textdata processed in okt.nouns function, NLP processing
    while oktdata
      do write_excel # Record the word and frequency, and the file name is 'reportnumber_number.xlsx'
    end
    
    #merge1
    while read_excel
      do write_excel # Accumulate and record word and frequency, and the file name is 'reportnumber.xlsx'
    end
    
    #merge2
    while merge1_read_excel
      do write_csv # Monthly data is sequentially accumulated in a file of the form'YYYYDD.csv'
    end
    
    --------------------------------------------
    
    func get_directory_file_list - 디렉토리의 파일리스트를 가져온다.
    func txt_processing - 확장자에따라 텍스트 처리를 한다.
    func html2text - html에서 text형태만 추출한다.
    func read_pdf_PDFMINER - pdf형태에서 text만 읽어온다.
    func okt.nouns - text를 NLP 처리한다.
    func merge_1 - 1차 결과를 추출한다. 결과는 데이터의 같은 보고서 번호를 병합하여 '보고서번호.xlsx' 형태의 파일로 word와 frequency열을 포함한다.
    func merge_2 - 2차 결과를 추출한다. merge1의 데이터를 이용하고 'YYYYDD.csv' 형태의 파일로 월별 데이터를 순차적으로 누적한다.

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
