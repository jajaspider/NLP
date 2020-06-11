import os
import shutil

target_directory = "H:/nfds/2019/"
move_directory = "I:/2019/"
# for i in os.listdir(target_directory):
#     print(i)


def filelistget(target_directory):
    file_list = []
    for i in os.listdir(target_directory):
        file_list.append(i)

    return file_list


# def filelistcal(file_list):
#     print("총 파일 갯수 : " + str(len(filelist)))


def movefile(file_name):
    # print("처리중인 파일 명 : " + file_name)
    if not os.path.isdir(move_directory + "20" + file_name[0:2]):
        os.mkdir(move_directory + "20" + file_name[0:2])
        print(move_directory + "20" + file_name[0:2] + " 폴더 생성 완료")
    if not os.path.isdir(move_directory + "20" + file_name[0:2] + "/" + file_name[2:4]):
        os.mkdir(move_directory + "20" + file_name[0:2] + "/" + file_name[2:4])
        print(move_directory + "20" + file_name[0:2] + "/" + file_name[2:4] + " 폴더 생성 완료")

    f = open(target_directory + file_name, 'rb')
    metadata = f.read(16)
    if metadata[0:10] == b'%PDF-1.4\n%':
        # print("PDF")
        shutil.copy(target_directory + file_name,
                    move_directory + "20" + file_name[0:2] + "/" + file_name[2:4] + "/" + file_name)
    elif metadata == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1\x00\x00\x00\x00\x00\x00\x00\x00':
        # print("HWP")
        shutil.copy(target_directory + file_name,
                    move_directory + "20" + file_name[0:2] + "/" + file_name[2:4] + "/" + file_name)
    # print("처리완료 파일 명 : " + file_name)


filelist = filelistget(target_directory)
for i in range(0, len(filelist)):
    # print("총 파일 " + str(len(filelist)) + "개 중 " + str(i) + "번째 파일 처리 중")
    # print(str(round((i / len(filelist)) * 100, 2)) + "% 처리 중")
    if filelist[i] is not "2007413200031_2" or filelist[i] is not "200841180000004_4" or filelist[i] is not "200845080000007_2" or filelist[i] is not "20074804000440_2" or filelist[i] is not "20074804000440_3" or filelist[i] is not "20074804000440_4" or filelist[i] is not "20074804000440_5" or filelist[i] is not "20074804000440_6" or filelist[i] is not "20074804000440_7" or filelist[i] is not "20074804000440_8" or filelist[i] is not "20074808000606_2":
        movefile(filelist[i])
