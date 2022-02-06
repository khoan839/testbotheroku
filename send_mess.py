import requests;
import datetime;
import os;
import time;
# <-----------------------NOTE---------------------->

# function change time VN -> US

def changeTimeVnToUs(vn):
    if(vn  < 7):
        return str(vn + 24 - 7);
    else:
        if(len(str(vn - 7)) == 2):
            return str(vn - 7)
        else:
            return "0" + str(vn - 7)
    
# <-----------------------NOTE---------------------->
long_id = "100015611230148"; # long
phu_id = "100070223828066";
mi_id = "100015963284971";
nam_id = "100013739145965";
gr_id = "5140856542665765";
mess = "Bot chào bạn nè, reply điiii";
sticker_id = '789355237820057';
cookie = 'sb=7KnuYYKiVhrCDNWvnTNCGpfj;datr=7KnuYfjwAS6urTHSIfbrzgbf;locale=vi_VN;c_user=100041633173329;m_pixel_ratio=1;x-referer=eyJyIjoiL21lc3NhZ2VzL3JlYWQvP3RpZD1jaWQuZy41MTQwODU2NTQyNjY1NzY1JmVudHJ5cG9pbnQ9amV3ZWwmc3VyZmFjZV9oaWVyYXJjaHk9dW5rbm93biIsImgiOiIvbWVzc2FnZXMvcmVhZC8%2FdGlkPWNpZC5nLjUxNDA4NTY1NDI2NjU3NjUmZW50cnlwb2ludD1qZXdlbCZzdXJmYWNlX2hpZXJhcmNoeT11bmtub3duIiwicyI6Im0ifQ%3D%3D;presence=C%7B%22t3%22%3A%5B%7B%22i%22%3A%22u.100041633173329%22%7D%5D%2C%22utc3%22%3A1644122576377%2C%22lm3%22%3A%22g.5140856542665765%22%2C%22v%22%3A1%7D;wd=354x695;xs=27%3AxX54TIvi3sX37Q%3A2%3A1644103964%3A-1%3A6291%3A%3AAcXc7nQiC_tLNHrhbZgelL5_kdba6slWtE_3rQfl2g;fr=0o0k76Oq380BFwE0y.AWUd_MFwQompwKHNP7Wr9g-BWFM.Bh_162.O1.AAA.0.0.Bh_162.AWWDcrx-8Bs;';

class message:
    def __init__(self,type_target = 'user',  id = '', mess = '', sticker_id = '', time = ["00", "00"], sended = False):
        self.type_target = type_target;
        self.id = id;
        self.mess = mess;
        self.sticker_id = sticker_id;
        self.time = time;
        self.sended = sended;
    def getData(self):
        return {
            'type_target': self.type_target,
            'id': self.id,
            'mess': self.mess,
            'sticker_id': self.sticker_id,
            'time': self.time,
            'sended': self.sended
        }

def run(target_type, id_target , message , sticker , my_cookie):
    headers = {
        'authority': 'm.facebook.com',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'x-msgr-region': 'PRN',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'x-response-format': 'JSONStream',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-lsd': 'JCqqQkY08mWHnjPJ4bCKR1',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://m.facebook.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://m.facebook.com/messages/read/?tid=' + 'cid.c.' + id_target if target_type == 'user' else  'cid.g.' + id_target+'&entrypoint=jewel&surface_hierarchy=unknown',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8,id;q=0.7',
        'cookie': my_cookie,
    }

    params = (
        ('icm', '1'),
        ('entrypoint', 'jewel'),
        ('surface_hierarchy', 'unknown'),
        ('refid', '12'),
    )

    data = {
      'tids': 'cid.c.'+id_target+':100041633173329' if target_type == 'user' else  'cid.g.' + id_target,
      'wwwupp': 'C3',
      'ids['+id_target+']': id_target,
      'body': message,
      'waterfall_source': 'message',
      'sticker_id': sticker,
      'action_time': '1644126731732',
      'fb_dtsg': 'AQHvmi176hVWWxI:27:1644103964',
      'jazoest': '22004',
      'lsd': 'bXkarx6FmEIP-Mh0z0zSj-',
      '__dyn': '1KQEGiFoO13DzUjxC2GfDg9ppkdxu6ErwgEqyonw_iwqobEdEc8uwaS6Uhx60he3y4o2GwWwbm3C3y1gCwjE1xoswaq1Jwt8-0nSUS0na1gwwyo36w9yq3q0H8-7E2swp834wmE2ewnE2Lx-220n6azo11E2Zw',
      '__csr': '',
      '__req': 'l',
      '__a': 'AYkofU8tG1d_YAsw3a6ZbvIMZSDxB8oxjUvtAlOrtzuoWXGUAPbqD34Q-2Jicxa4h9gwtwjp8auiGlw38dNl4VEtw3dGWMsbMfT4c0yOGZjikA',
      '__user': '100041633173329'
    }
    
    response = requests.post('https://m.facebook.com/messages/send/', headers=headers, params=params, data=data);
    return response;


#create object
chucngungon = message('user',nam_id, mess, sticker_id, [changeTimeVnToUs(22), "30"]);
chucngungon2 = message('user',nam_id, mess, sticker_id, [changeTimeVnToUs(4), "00"]);
chucngungon3 = message('user',nam_id, mess, sticker_id, [changeTimeVnToUs(22), "40"]);
# run(chucngungon.getData()['type_target'],chucngungon.getData()['id'], chucngungon.getData()['mess'], chucngungon.getData()['sticker_id'], cookie);
arr_mess = [
    chucngungon,
    chucngungon2,
    chucngungon3
];
# # time send mess

while True:
    time_now = str(datetime.datetime.now());
    arr_time_now = time_now.split(" ")[1].split(".")[0].split(":");
    for x in arr_mess:
        if(arr_time_now[0] == x.getData()['time'][0] and arr_time_now[1] == x.getData()['time'][1] and not x.getData()['sended']):
            a = run(chucngungon.getData()['type_target'],x.getData()['id'], x.getData()['mess'], x.getData()['sticker_id'], cookie);
            if(a.status_code == 200):
                x.sended = True;
                strin = x.getData()['mess'] + ' | ' + x.getData()['sticker_id'] + ' | ' + x.getData()['id'] + ' | ' + arr_time_now[0] + ':' + arr_time_now[1] + '\n';
                with open('file.txt',"a", encoding='UTF-8') as f:
                    f.write(strin);
                    f.close();
                print('sended');
            else:
                print("send error");
        else:
            print("Send time: " ,  x.getData()['time'] , ' -- now: ' , arr_time_now);
    print("running...");
    time.sleep(10);