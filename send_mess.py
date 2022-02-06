import requests;
import datetime;
import os;
import time;

long_id = "100015611230148"; # long
phu_id = "100070223828066";
mi_id = "100015963284971";
gr_id = "5140856542665765";
mess = 'sieu cap vip pro';
sticker_id = '';
cookie = 'sb=HHvrYdoqbscL8bSOQQoanaZD; datr=HHvrYQjSI7Y6igOnhyFWcJx1; c_user=100013739145965; dpr=1; xs=19%3A7K0xYDLntGL0yg%3A2%3A1642832718%3A-1%3A6215%3A%3AAcUB1gIjdiK08Gw4Pxr_pXo4KspP3Kekzh3i_tjapLc; fr=0e7obCJKhj8UTHSMz.AWVV75s2jFt5pKYR6TFSBvrMp1U.Bh_kbk.b7.AAA.0.0.Bh_kbk.AWWP1QqF1WU; m_pixel_ratio=1; x-referer=eyJyIjoiL21lc3NhZ2VzL3JlYWQvP3RpZD1jaWQuYy4xMDAwMTM3MzkxNDU5NjUlM0ExMDAwNzAyMjM4MjgwNjYmZW50cnlwb2ludD1qZXdlbCZzdXJmYWNlX2hpZXJhcmNoeT11bmtub3duIiwiaCI6Ii9tZXNzYWdlcy9yZWFkLz90aWQ9Y2lkLmMuMTAwMDEzNzM5MTQ1OTY1JTNBMTAwMDcwMjIzODI4MDY2JmVudHJ5cG9pbnQ9amV3ZWwmc3VyZmFjZV9oaWVyYXJjaHk9dW5rbm93biIsInMiOiJtIn0%3D; wd=1349x381';

class message:
    def __init__(self, id = '', mess = '', sticker_id = '', time = ["00", "00"], sended = False):
        self.id = id;
        self.mess = mess;
        self.sticker_id = sticker_id;
        self.time = time;
        self.sended = sended;
    def getData(self):
        return {
            'id': self.id,
            'mess': self.mess,
            'sticker_id': self.sticker_id,
            'time': self.time,
            'sended': self.sended
        }

def run(id_target , message , sticker , my_cookie):
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
        'referer': 'https://m.facebook.com/messages/read/?tid=cid.c.100013739145965%3A'+id_target+'&entrypoint=jewel&surface_hierarchy=unknown',
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
      'tids': 'cid.c.100013739145965:'+id_target+'',
      'wwwupp': 'C3',
      'ids['+id_target+']': id_target,
      'body': message,
      'waterfall_source': 'message',
      'sticker_id': sticker,
      'action_time': '1644057371835',
      'fb_dtsg': 'AQFdoVdWBKSZ8kQ:19:1642832718',
      'jazoest': '22002',
      'lsd': 'JCqqQkY08mWHnjPJ4bCKR3',
      '__dyn': '1KQEGiFoO13DzUjxC2GfDg9ppkdxu6ErwgEqyonw_iwqobEdEc8uwaS6Uhx60he3y4o2GwWwbm3C3y1gCwjE1xoswaq1Jwt8-0nSUS0na1gwwyo36w9yq3q0H8-7E2swp834wmE2ewnE2Lx-220n6azo11E2Zw',
      '__csr': '',
      '__req': '6',
      '__a': 'AYkY5FG6q2WoI5jT9iJWsaKZTgKBFQFu2f_E73HgzfF8TaSbhpjQSk68QLXPs0u26KF670Koz_O9qSl-NZ_VtUVqciS21HwXmcMVfB39E832Pg',
      '__user': '100013739145965'
    }

    response = requests.post('https://m.facebook.com/messages/send/', headers=headers, params=params, data=data);
    return response;


#create object
chucngungon = message(phu_id, mess, sticker_id, ["10", "45"]);

arr_mess = [
    chucngungon
];
# # time send mess

while True:
    time_now = str(datetime.datetime.now());
    arr_time_now = time_now.split(" ")[1].split(".")[0].split(":");
    for x in arr_mess:
        if(arr_time_now[0] == x.getData()['time'][0] and arr_time_now[1] == x.getData()['time'][1] and not x.getData()['sended']):
            a = run(x.getData()['id'], x.getData()['mess'], x.getData()['sticker_id'], cookie);
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