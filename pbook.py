import re
import os
#テキストファイルを読み込む
filename =  './number_list.txt'
#with open(filename, 'r', encoding = 'UTf-8') as f:
 #   datas = f.read()
  #  print(datas)
print('-----------------------------------')

#登録する(正規表現で桁数などの調整は未)
def regist_phone():
    print('名前を入力してください')
    name = input('名前：')
    print('電話番号を入力してください')
    phone_num = input('電話番号：')
    return ["名前：" + name, "電話番号:" + phone_num]

#削除する
def delete_phone():
    print('名前をl入力してください')
    name = input('名前：')
    print('電話番号を入力してください')
    phone_num = input('電話番号：')
    ["名前：" + name, "電話番号:" + phone_num]
    with open(filename, 'r', encoding = 'UTF-8') as f:
        for line in f:
            if name in line:
                print(name + 'を削除しますか？')
                del_name = int(input('YESは1を、NOは2をおしてください：'))
                if del_name == 1:
                    print(line.index(name))
                

#表示する
def open_phone():
    print('-----------------------------------')
    with open(filename, 'r', encoding = 'UTF-8') as f:
            phone_lists = f.read().split(',')
    for phone_list in phone_lists:
        print(phone_list)

#検索する
def search_phone():
    print('検索したい名前または番号をいれてください')
    search = input()
    with open(filename, 'r', encoding = 'UTF-8') as f:
            phone_lists = f.read().split(',')
            return re.search(search,phone_lists)
    
#初期化する
def clear_phone():
    print('初期化しますか？')
    clear = int(input('YESは1を、NOは2を押してください:'))
    if clear == 1:
        print('初期化されました')
        os.remove(filename)


#終了する
def quit_phone():
    return print('終了しました')
    

while True:
    print('a/登録：add')
    print('d/削除：delete')
    print('l/一覧表示：list')
    print('s/検索：search')
    print('c/初期化：clear')
    print('q/終了：quit')
    choice = input('アルファベットで選択してください：')

    if choice == 'a':#addを選択した動作　テキストファイルに追記する　済（正規表現未）
        with open(filename, 'a', encoding = 'UTF-8') as f:
            for regist in regist_phone():
                f.write(str(regist) + '\n') 
                print('登録が完了しました' + '\n')
    elif choice == 'd':#deleteを選択した動作　テキストファイルから削除する　未
        delete_phone()
        del_l = input('取得した番号を入力してください：')
        print('登録を削除しました' + '\n')
    elif choice == 'l':#listを選択した動作　　コンソールに一覧表示する 済
        open_phone()
    elif choice == 's':#searchを選択した動作　検索結果を表示する　未
        if search_phone() == True:
            print(search_phone() + 'が見つかりました' + '\n')
        else:
            print('見つかりませんでした' + '\n')
    elif choice == 'c':#clearを選択した動作　全部一括初期化する　済
        clear_phone()
    elif choice == 'q':#quitを選択した動作　作業を終了する　済
        quit_phone()
        break
