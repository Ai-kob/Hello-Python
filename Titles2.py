#  Titlesをより良くなるようにやってみる
import os, re
import phonenumbers
import Fileope2
file_open = Fileope2.FileOperation("")
file_open2 = Fileope2.FileOperation2("","")
file_open4 = Fileope2.FileOperation4()
filename =  './number_list4.txt'
patternz = '0\d{1,4}-\d{1,4}-\d{3,4}' 
     
#名前と電話番号入力の土台を作成
class NameNum(object):
    def __init__(self):
        self._name = input('名前を入力してください：')
        if len(self._name) == 0:
            print('名前を正しく入力してください')
        else:
            self._phone_num = input('電話番号を入力してください：')
            if not self._phone_num =='':
                try:
                    hyphen = phonenumbers.parse(self._phone_num, 'JP')
                    self._phone_num = phonenumbers.format_number(hyphen, phonenumbers.PhoneNumberFormat.NATIONAL)
                except Exception:
                    print('電話番号が間違っています')
                else:
                    if not re.match(patternz, self._phone_num):
                        print('電話番号を正しく入力してください')
            else:
                print('電話番号を正しく入力してください')
            self._regist = ["名前：" + self._name, "電話番号:" + self._phone_num]
        
        
    @property
    def name(self):
        return self._name
    
    
    @property
    def phone_num(self):
        return self._phone_num

    
    @property
    def regist(self):
        return self._regist

    
#機能別にクラスを作成（Regist、Deleteは継承）
class Regist(NameNum):
    def regist_phone(self):
        if self._name and re.match(patternz, self._phone_num):
            file_open.read_file()
            if self._name in file_open.read_file() or self._phone_num in file_open.read_file():
                print('すでに登録があります')
            elif self._regist:
                print(self._regist)
                file_regist = Fileope2.FileOperation(self._regist)
                file_regist.regist
                file_regist.write_file()
                print('登録が完了しました' + '\n')
            else:
                print('登録できませんでした')


class Delete(NameNum):
    def delete_phone(self):
        if self._name and re.match(patternz, self._phone_num):
            file_open.read_file()
            if self._name not in file_open.read_file() or self._phone_num not in file_open.read_file():
                    print('削除するデータは存在しません')
            else:
                fileOpenRw = Fileope2.FileOperation2(self._regist, self._name)
                fileOpenRw.read_write_file()
                fileOpenRw.name
                fileOpenRw.regist


class Open(object):
    def open_phone(self):
        print('-----------------------------------')
        file_open3 = Fileope2.FileOperation3()
        ret = os.path.getsize(filename)
        if ret == 0:
            print('ファイルは空です ' + '\n')
        else:
            file_open3.readline_file()


class Search(object):
    def search_phone(self):
        file_open4.readlines_file()
        ret = os.path.getsize(filename)
        if ret == 0:
            print('ファイルは空です ' + '\n')
        else:
            print('名前で検索する場合は１、電話番号で検索する場合は2、終了する場合は３をおしてください')
            try:
                search:int = int(input('番号：'))
            except ValueError:
                print('数字で入力してください')
            else:
                if search ==  1:
                    self._name = input('名前をいれてください：')
                    if len(self._name) > 0:
                        file_open4.readlines_file()
                        for phone_list in file_open4.readlines_file():
                            if self._name in phone_list:
                                print(phone_list + 'が、みつかりました')
                        file_open.read_file()
                        if self._name not in file_open.read_file():
                            print(self._name + 'は、みつかません'+ '\n')
                    else:
                        print('名前を正しく入力してください')
                elif search == 2:
                    try:
                        self._phone_num = input('電話番号：')
                        hyphen = phonenumbers.parse(self._phone_num, 'JP')
                        self._phone_num = phonenumbers.format_number(hyphen, phonenumbers.PhoneNumberFormat.NATIONAL)
                    except Exception:
                        print('電話番号を正しく入力してください')
                    else:
                        file_open4.readlines_file()
                        for phone_list in file_open4.readlines_file():
                             if self._phone_num in phone_list:
                                print(phone_list + 'が、みつかりました')
                        file_open.read_file()
                        if self._phone_num not in file_open.read_file():
                            print(self._phone_num + 'は、みつかません' + '\n')
                elif search == 3:
                    print('検索を終了しました' + '\n')
                    #break
                else:
                    print('番号が正しくありません' + '\n')


    @property
    def name(self):
        return self._name


    @property
    def phone_num(self):
        return self._phone_num


class Clear(object):
    def clear_phone(self):
        try:
            print('初期化しますか？')
            clear:int = int(input('YESは1を、NOは2を押してください:'))
        except ValueError:
            print('数字を入力してください')
        else:
            if clear == 1:
                print('初期化されました' + '\n')
                file_open4.pass_file()
            elif clear == 2:
                print('初期化をやめました' + '\n')
            else:
                print('番号が正しくありません' + '\n')


class Quit(object):
    def quit_phone(self):
        return print('終了しました')
