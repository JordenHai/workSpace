
import requests
import json
import schedule
bi_url = 'https://api.bilibili.com/x/member/web/sign/update'
bi_headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'215',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'buvid3=5EC5E81B-B451-489C-9721-699E92FD2A3B47161infoc; LIVE_BUVID=AUTO4515523689936642; sid=8ffharfi; rpdid=kmwqssklpxdossikxlwqw; fts=1552369305; UM_distinctid=169707288282ec-0939e7df374edc-4d045769-15f900-1697072882b2a7; finger=7360d3c2; im_notify_type_14639016=0; im_seqno_14639016=1; im_local_unread_14639016=0; DedeUserID=14639016; DedeUserID__ckMd5=de1ceeb7e753d098; SESSDATA=ffd31f60%2C1557915931%2C294e1841; bili_jct=17b57e908c099be03e48f899bd6c174e; bp_t_offset_14639016=242622358959118626; CURRENT_FNVAL=16; stardustvideo=1; bsource=seo_baidu; _dfcaptcha=219f5bf6ad15dc553b3d4604ba7b8933',
    'Origin':'https://space.bilibili.com',
    'Referer':'https://space.bilibili.com/14639016',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}

message = ''
csrf_my = '17b57e908c099be03e48f899bd6c174e'

def update(message,csrf):
    return {
    'user_sign':message,
    'jsonp':'jsonp',
    'csrf':csrf
    }

def update_sign(message,csrf):
    return requests.post(url=bi_url,headers=bi_headers,data=update(message,csrf))

# r = requests.post(url=bi_url,headers=bi_headers,data=update('1',csrf_my)).json()
# print(r)

interval = [0,5,11,14,18,22]

message_list=[
    '该睡觉了，亲',
    '早上好呀，小可爱',
    '中午好呀，小可爱',
    '下午好呀，亲',
    '晚上好呀，亲',
    '该睡觉了，亲'
]
for i in range(len(interval)):
    schedule.every().days.at('{:0>2d}:00'.format(interval[i])).do(update_sign,message_list[i],csrf_my)
