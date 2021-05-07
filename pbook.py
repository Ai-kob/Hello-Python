import re
import os

filename =  './number_list.txt'
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
    print('名前を入力してください')
    name = input('名前：')
    print('電話番号を入力してください')
    phone_num = input('電話番号：')
    with open(filename, 'r', encoding = 'UTF-8') as f:
        for line in f:
            if name in line or phone_num in line:
                print(line)
    with open(filename, 'w' , encoding = 'UTF-8') as of:
        of.writelines(line)
        print('名前：' + name +'電話番号：' + phone_num + 'を削除しました。')

#表示する
def open_phone():
    print('-----------------------------------')
    with open(filename, 'r', encoding = 'UTF-8') as f:
            phone_lists = f.read().split(',')
    for phone_list in phone_lists:
        print(phone_list)

#検索する
def search_phone():
    print('名前で検索する場合は１、電話番号で検索する場合は2をおしてください。')
    search = int(input())
    if search == 1:
        c_name = input('名前をいれてください：')
        with open(filename, 'r', encoding = 'UTF-8') as f:
            phone_lists = f.readlines()
            for phone_list in phone_lists:
                if phone_list.find(c_name) >= 0:
                    print(phone_list[:-1] + 'がみつかりました。')
                    
                
    if search == 2:
        c_phone = input('電話番号をいれてください：')
        with open(filename, 'r', encoding = 'UTF-8') as f:
            phone_lists = f.readlines()
            for phone_list in phone_lists:
                if phone_list.find(c_phone) >= 0:
                    print(phone_list[:-1] + 'がみつかりました。')
        
    
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
            #for regist in regist_phone():
                f.write(str(regist_phone())+ '\n') 
                print('登録が完了しました' + '\n')
    elif choice == 'd':#deleteを選択した動作　テキストファイルから削除する　未
        delete_phone()
        print('登録を削除しました' + '\n')
    elif choice == 'l':#listを選択した動作　　コンソールに一覧表示する 済
        open_phone()
    elif choice == 's':#searchを選択した動作　検索結果を表示する　済
        search_phone()
    elif choice == 'c':#clearを選択した動作　全部一括初期化する　済
        clear_phone()
    elif choice == 'q':#quitを選択した動作　作業を終了する　済
        quit_phone()
        break
