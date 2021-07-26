# -*- coding: utf-8 -*-
import os, re
import PySimpleGUI as sg
import phonenumbers
import FileTest

filename =  './number_list4.txt'
patternz = '0\d{1,4}-\d{1,4}-\d{3,4}' 
file_open = FileTest.FileOperation("")
file_open2 = FileTest.FileOperation2("","")
file_open4 = FileTest.FileOperation4()

class NameNum:
    def __init__(self):
        self._name = values['name']
        if len(self._name) == 0:
            sg.popup_error('名前を正しく入力してください')
        else:
            self._phone_num = values['num']
            if not self._phone_num =='':
                try:
                    hyphen = phonenumbers.parse(self._phone_num, 'JP')
                    self._phone_num = phonenumbers.format_number(hyphen, phonenumbers.PhoneNumberFormat.NATIONAL)
                except Exception:
                    sg.popup_error('電話番号が間違っています')
                else:
                    if not re.match(patternz, self._phone_num):
                        sg.popup_error('電話番号を正しく入力してください')
            else:
                sg.popup_error('電話番号を正しく入力してください')
            self._regist = ["名前：" + self._name, "電話番号:" + self._phone_num]


#GUI表示できるようにprint部分をpopupに変更
class Regist(NameNum):
    def regist_phone(self):
        if self._name and re.match(patternz, self._phone_num):
            file_open.read_file()
            if self._name in file_open.read_file() or self._phone_num in file_open.read_file():
                sg.popup('すでに登録があります')
            elif self._regist:
                #print(self._regist)
                file_regist = FileTest.FileOperation(self._regist)
                file_regist.regist
                file_regist.write_file()
                sg.popup('登録が完了しました' + '\n')
            else:
                sg.popup_error('登録できませんでした')


class Delete(NameNum):
    def delete_phone(self):
        if self._name and re.match(patternz, self._phone_num):
            file_open.read_file()
            if self._name not in file_open.read_file() or self._phone_num not in file_open.read_file():
                    sg.popup_error('削除するデータは存在しません')
            else:
                fileOpenRw = FileTest.FileOperation2(self._regist, self._name)
                fileOpenRw.read_write_file()
                fileOpenRw.name
                fileOpenRw.regist


class Search:
    def search_phone(self):
        file_open4.readlines_file()
        ret = os.path.getsize(filename)
        if ret == 0:
           sg.popup('ファイルは空です ' + '\n')
        else:
            self._name = values['name']
            self._phone_num = values['num']
            if len(self._name) > 0:
                file_open4.readlines_file()
                for phone_list in file_open4.readlines_file():
                    if self._name in phone_list:
                        sg.popup(phone_list + 'が、みつかりました')
                file_open.read_file()
                if self._name not in file_open.read_file():
                    sg.popup(self._name + 'は、みつかません'+ '\n')
            elif len(self._phone_num) > 0:
                file_open4.readlines_file()
                for phone_list in file_open4.readlines_file():
                    if self._phone_num in phone_list:
                        sg.popup(phone_list + 'が、みつかりました')
                file_open.read_file()
                if self._phone_num not in file_open.read_file():
                    sg.popup_error(self._phone_num + 'は、みつかません' + '\n')


    @property
    def name(self):
        return self._name


    @property
    def phone_num(self):
        return self._phone_num

#PySimpleGUI用コード
sg.theme('SystemDefalt')
layout = [
          [sg.Text('登録、削除、検索は以下を入力してボタンをおしてください',
                   font=('メイリオ', 10), key='txt2')],
          [sg.Text('　　名前：'), sg.Input('', key='name', size=(35,1))],
          [sg.Text('電話番号：'), sg.Input('', key='num', size=(35,1))],

          ]

layout3 =  [
            [sg.Text('メニューを選択してください', font=('メイリオ', 10), key='txt1')],
            [sg.Button('0.add:登録', size=(13,1), key='-a-'),
            sg.Button('1.delete:削除', size=(13,1), key='-d-'),
            sg.Button('2.list:一覧表示', size=(13,1), key='-l-')],
            [sg.Button('3.search:検索', size=(13,1), key='-s-'),
            sg.Button('4.clear:初期化', size=(13,1), key='-c-'),
            sg.Button('5.quit:終了', size=(13,1), key='-q-')],
           ]

layout2 = [[sg.Frame('メニューリスト', layout3 , #title_color ='#ffff00',
            title_location = sg.TITLE_LOCATION_TOP_LEFT)],
           [sg.Frame('入力欄',layout)]]


window = sg.Window('電話帳アプリ', layout2)

while True:
    event, values = window.read()
    if event in (None, '-q-'):
        break
    
    if event == '-a-':
        Regist().regist_phone()
        
    elif event =='-d-':
        Delete().delete_phone()

    elif event == '-l-':
        file_open3 = FileTest.FileOperation3()
        ret = os.path.getsize(filename)
        if ret == 0:
            sg.popup('ファイルは空です ' + '\n')
        else:
            file_open3.readline_file()
    elif event == '-s-':
        Search().search_phone()
    elif event == '-c-':
        clear = sg.popup_yes_no('初期化しますか？', keep_on_top=True)
        if clear == 'Yes':
            file_open4 = FileTest.FileOperation4()
            file_open4.pass_file()
            sg.popup('初期化しました')
        elif clear == 'No':
            sg.popup('初期化をやめました')
            

window.close()

