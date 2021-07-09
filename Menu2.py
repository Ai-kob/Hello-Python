#  Menuをより良くなるように書いてみる

import Titles2
#初期の動作をする（メニュー選択）
class MenuContents(object):
    def __init__(self, name):
       self.__name = name

    
    @property
    def info(self):
        return self.__name

#メニューの選択をする
    @classmethod
    def menu_choice(cls):
        while True:
            print('-----------------------------------')
            menu_contents0 = MenuContents('add:登録')
            menu_contents1 = MenuContents('delete:削除')
            menu_contents2 = MenuContents('list:一覧表示')
            menu_contents3 = MenuContents('search:検索')
            menu_contents4 = MenuContents('clear:初期化')
            menu_contents5 = MenuContents('quit:終了')
    
            menu_contents = [
                             menu_contents0,
                             menu_contents1,
                             menu_contents2,
                             menu_contents3,
                             menu_contents4,
                             menu_contents5
                             ]
            index = 0
            for menu in menu_contents:
                print(str(index) + '.' + menu.info)
                index +=1
            print('-----------------------------------')
            try:
                choice = int(input('項目を数字で選択してください:'))
                selected_menu = menu_contents[choice]
            except:
                print('正しく数字を入力してください')
    
            else:
                print('選択されたメニュー: ' + selected_menu.info)
    
                if choice == 0:
                    choice0 = Titles2.Regist()
                    choice0.regist_phone()
                    if choice0.name:
                        choice0.phone_num
                elif choice == 1:
                    choice1 = Titles2.Delete()
                    choice1.delete_phone()
                    if choice1.name:
                        choice1.phone_num
                elif choice == 2:
                    choice2 = Titles2.Open()
                    choice2.open_phone()
                elif choice == 3:
                    choice3 = Titles2.Search()
                    choice3.search_phone()
                    try:
                        choice3.name or choice3.phone_num
                    except AttributeError:
                        pass                    
                elif choice == 4:
                    choice4 = Titles2.Clear()
                    choice4.clear_phone()
                elif choice == 5:
                    choice5 = Titles2.Quit()
                    choice5.quit_phone()
                    break

MenuContents.menu_choice()
