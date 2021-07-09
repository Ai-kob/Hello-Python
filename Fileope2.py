# Fileope.pyをより良いコードにする
import re
filename =  './number_list4.txt'
#ファイル操作のクラスをつくる
class FileOperation(object):
    def __init__(self, arg1):
        self._regist = arg1


    @property
    def regist(self):
        return self._regist


#regist,delete,searchに使用
    def read_file(self):
        with open(filename, 'r', encoding = 'UTf-8') as f: 
            file_text = f.read()
        return file_text


    def write_file(self):
        with open(filename, 'a', encoding = 'UTF-8') as f:
            f.write(str(self._regist) + '\n')


#delete_phoneに使用
class FileOperation2(object):
    def __init__(self, arg1, arg2):
        self._regist = arg1
        self._name = arg2


    @property
    def regist(self):
        return self._regist


    @property
    def name(self):
        return self._name


    def read_write_file(self):
            with open(filename, 'r', encoding = 'UTF-8') as f:
                lines = f.readlines()
                lines_strip = [line.strip() for line in lines]
                ans = [line for line in lines_strip if self._name in line]
                for answer in ans:
                    if answer == str(self._regist):
                        with open(filename, 'w', encoding = 'UTF-8') as f:
                            for line in lines:
                                if not(re.findall(self._name, line)):
                                    f.write(line)
                        print(str(self._regist) + 'を削除しました'+ '\n')
                    else:
                        print('名前と電話番号が一致していません' + '\n')

#open_phoneに使用
class FileOperation3(object):
    def readline_file(self):
        with open(filename, 'r', encoding = 'UTF-8') as f:
            phone_lists = f.read().split(',')
            for phone_list in phone_lists:
                print(phone_list)

#search_phoneに使用
class FileOperation4(object):                    
    def readlines_file(self):
            with open(filename, 'r', encoding = 'UTF-8') as f:
                phone_lists = f.readlines()
                return phone_lists

#clear_phoneに使用
    def pass_file(self):
        with open(filename, 'w', encoding = 'UTF-8') as f:
            pass

