import requests,sys,time,os
from pystyle import Write,Colors,System
# <!--- Colors ---!>
_Black_ = '\033[1;30m'
_Red_ = '\033[1;31m'
_Green_ = '\033[1;32m'
_Yellow_ = '\033[1;33m'
_Blue_ = '\033[1;34m'
_Purple_ = '\033[1;35m'
_Cyan_ = '\033[1;36m'
_White_ = '\033[1;37m'
# <!--- Colors ---!>
try:
    os.remove('list_cookie.txt')
except:
    pass
file = open('list_cookie.txt','a+')
list_page_die = []
def __gach__():
    Write.Print('────────────────────────────────────────────────────────\n', Colors.cyan_to_green, interval=0.00125)
class Copyright():
    def __Banner__(self):
        System.Clear()
        ban = f'''
{_Blue_}██╗  ██╗███████╗██╗  ██╗██╗  ██╗ ██████╗      ██╗██╗
{_White_}██║ ██╔╝██╔════╝╚██╗██╔╝██║ ██╔╝██╔═══██╗     ██║██║
{_Blue_}█████╔╝ ███████╗ ╚███╔╝ █████╔╝ ██║   ██║     ██║██║
{_White_}██╔═██╗ ╚════██║ ██╔██╗ ██╔═██╗ ██║   ██║██   ██║██║
{_Blue_}██║  ██╗███████║██╔╝ ██╗██║  ██╗╚██████╔╝╚█████╔╝██║
{_White_}╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚═╝
{_Cyan_}────────────────────────────────────────────────────────
{_Red_}[{_Yellow_}🔰{_Red_}] {_Green_}AUTHOR : {_Yellow_}Dương Phú Quốcc ( KsxKoji )
{_Red_}[{_Yellow_}🔰{_Red_}] {_White_}FACEBOOK ME : {_Green_}https://facebook.com/100042415576964
{_Red_}[{_Yellow_}🔰{_Red_}] {_Red_}YOUTUBE ME : {_Cyan_}https://youtube.com/@KsxKoji
{_Cyan_}────────────────────────────────────────────────────────
'''
        for h in ban:
            sys.stdout.write(h)
            sys.stdout.flush()
            time.sleep(0.0025)
    def __Loading__(self, o):
        while o != 0:
            o = o - 1
            print(f'{_Cyan_}[{_Yellow_}/{_Cyan_}] {_Red_}Đang {_Green_}Loading{_Black_}, {_Yellow_}Còn {_Blue_}{o} {_Purple_}Giây {_Cyan_}Nữa      ', end='\r'); time.sleep(1/6)
            print(f'{_Cyan_}[{_Yellow_}-{_Cyan_}] {_Cyan_}Đang {_Red_}Loading{_Black_}, {_Green_}Còn {_Yellow_}{o} {_Blue_}Giây {_Purple_}Nữa      ', end='\r'); time.sleep(1/6)
            print(f'{_Cyan_}[{_Yellow_}\\{_Cyan_}] {_Purple_}Đang {_Cyan_}Loading{_Black_}, {_Red_}Còn {_Green_}{o} {_Yellow_}Giây {_Blue_}Nữa     ', end='\r'); time.sleep(1/6)
            print(f'{_Cyan_}[{_Yellow_}|{_Cyan_}] {_Blue_}Đang {_Purple_}Loading{_Black_}, {_Cyan_}Còn {_Red_}{o} {_Green_}Giây {_Yellow_}Nữa      ', end='\r'); time.sleep(1/6)
class KsxKoji():
    def __init__(self) -> None:
        __AUTHOR__ = 'Dươngg Phú Quốcc ( KsxKoji )'
        __FACEBOOK__ = 'https://fb.com/100042415576964'
        __YOUTUBE__ = 'https://youtube.com/@KsxKoji'
    def __Get_ThongTin__(self, cookie):
        self.id_ck = cookie.split('c_user=')[1].split(';')[0]
        a = requests.get('https://mbasic.facebook.com/profile.php?='+self.id_ck, headers={'cookie': cookie}).text
        try:
            self.name = a.split('<title>')[1].split('</title>')[0]
            self.fb_dtsg = a.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
            self.jazoest = a.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
            return True
        except:
            return False
    def __Get_PageDie__(self, cookie):
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'dpr': '1',
            'referer': 'https://www.facebook.com/settings/?tab=profile_recommendations&show_recommendable_nux=1000',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }

        params = {
            'category': 'your_pages',
            'ref': 'bookmarks',
        }

        response = requests.get('https://www.facebook.com/pages/', params=params, headers=headers)
        self.dem = 0
        while True:
            try:
                self.dem += 1
                self.name = response.text.split('{"__typename":"User","name":"')[self.dem].split('","')[0]
                self.id = response.text.split('"uri_token":"')[self.dem].split('","')[0]
                list_page_die.append(self.id)
            except:
                break
    def __Activation__(self, cookie, id):
        headers = {'accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cache-control': 'max-age=0','content-encoding': 'br','content-type': 'application/x-www-form-urlencoded','cookie': cookie,'origin': 'https://www.facebook.com','referer': 'https://www.facebook.com','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','sec-gpc': '1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',}

        data = {
            'av': self.id_ck,
            '__user': self.id_ck,
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'variables': '{"profile_id":"'+id+'","delegate_page_id":null}',
            'server_timestamps': 'true',
            'doc_id': '6365256943526229',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()

        try:
            a = response['data']['reactivate_profile']
            self.name, self.idd = a['name'], a['id']
            return True
        except:
            return False
def __Main__():
    f = KsxKoji(); a = Copyright()
    dem_ck = 0; a.__Banner__()
    while True:
            try:
                cookie = input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập Cookie Account Chứa Page Die {_Cyan_}[{_Purple_}{dem_ck}{_Cyan_}]{_Yellow_}: {_Green_}')
                if cookie != '' and 'c_user=' in cookie:
                    fb = f.__Get_ThongTin__(cookie)
                    if fb == True:
                        f.__Get_PageDie__(cookie)
                        __gach__()
                        print(f'{_Cyan_}(*) {_Green_}Name Profile: {_Yellow_}{f.name} {_Red_}| {_Green_}Có {_Yellow_}{len(list_page_die)} {_Green_}Page Die')
                        __gach__()
                        list_page_die.clear()
                        dem_ck += 1
                        save = open('list_cookie.txt','a+').write(cookie+'\n')
                elif cookie == '' and dem_ck >= 1:
                    break
                else:
                    print(f'{_Red_} Bắt Buộc Nhập Ít Nhất 1 Cookie !!!')
                    __gach__()
            except KeyboardInterrupt:
                quit()
    a.__Banner__()
    so_luong = int(input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập Số Lượng Muốn Kích Hoạt{_Yellow_}: {_Green_}'))
    delay = int(input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập Thời Gian Delay{_Yellow_}: {_Green_}'))
    __gach__()
    x = 0; dem = 0; dem_ck = 0
    open_file = open('list_cookie.txt','r').read().split('\n')
    list_page_die.clear()
    while True:
        try:
            cookie = open_file[dem_ck]
            f.__Get_ThongTin__(cookie)
            f.__Get_PageDie__(cookie)
            print(f' Đang Cấu Hình Account {f.name}', end='\r')
            while True:
                try:
                    dem += 1
                    id = list_page_die[x]
                    kich_hoat = f.__Activation__(cookie,id)
                    if kich_hoat == True:
                        print(f'{_Cyan_}[{_Red_}{dem}{_Cyan_}] {_Purple_}| {_Green_}KsxKoji~ {_Purple_}| {_Green_}UID: {_Yellow_}{id} {_Purple_}| {_Yellow_}Kích Hoạt Thành Công')
                    elif kich_hoat == False:
                        print(f'{_Cyan_}[{_Red_}{dem}{_Cyan_}] {_Purple_}| {_Green_}KsxKoji~ {_Purple_}| {_Green_}UID: {_Yellow_}{id} {_Purple_}| {_Red_}Kích Hoạt Thất Bại')
                    a.__Loading__(delay)
                    if dem >= so_luong:
                        print(f'{_Cyan_} Đã Xong, Out !!                         ')
                        quit()
                except:
                    print(f'{_Cyan_} Hết Page Die, Chuyển Account !!                                      ', end='\r')
                    list_page_die.clear()
                    time.sleep(2)
                    dem_ck += 1
                    print(' '*100, end='\r')
                    break
        except:
            print(f'{_Cyan_} Hết Cookie Chứa Page Die, Out !!                                      ')
            quit()
try:
    __Main__()
except KeyboardInterrupt:
    quit()