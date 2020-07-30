# NLP

NLP classifies the data of documents after statistics through natural language processing.

# 처리가능한 파일
현재는 hwp,pdf 만 처리 가능
#

# Psuedo code
    var filelist is Store a list of files in a directory
    var extends is The file extension for filelist.
    var textdata is Save Text Data
    var noun_list is List of NLP results.
    
    --------------------------------------------
    
    function get_directory_file_list - Get a list of files in a directory.
    function html2text - Extract only text from html.
    function read_pdf_pdfminer - Open the pdf and return the text.
    function text_processing - Perform NLP through okt.nouns
    function write,read excel - Read and write as an Excel file.
    
    function merge_1 - First results are extracted. The result is a file in the form of'report number.xlsx' by merging the same report number of the data and includes the word and frequency columns.
    function merge_2 - Second results are extracted. The data of merge1 is used and monthly data is sequentially accumulated in a file of the form'YYYYDD.csv'.
    
    --------------------------------------------
    
    while filelist:
      if extends is "hwp"
        do Convert hwp file to html // When reading hwp files directly, there is a problem that cannot read the whole
        textdata <- through parsing from html
      elif extends is "pdf"
        textdata <- pdf file through read_pdf_pdfminer function
        
      noun_list <- text_processing(filelist)
    whileend
        
    while noun_list:
      do write_excel(noun_list) // Record the word and frequency, and the file name is 'reportnumber_number.xlsx'
    whileend
    
    while read_excel:
      do write_excel(read_excel) // Accumulate and record word and frequency, and the file name is 'reportnumber.xlsx'
    whileend
    
    while merge1_read_excel
      do write_csv(merge1_read_excel) # Monthly data is sequentially accumulated in a file of the form'YYYYDD.csv'
    whileend

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
