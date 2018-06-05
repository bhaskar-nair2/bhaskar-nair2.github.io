import urllib.request as req
import re

def is_ascii(s):
    try:
        s.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False

# url='https://www.instagram.com/bas_kar_na_yar/?hl=en'
# #dat= urllib.parse.urlencode()
# #dat=dat.encode('utf-8')
#
# data= req.Request(url)
# resp= req.urlopen(data)
# respData= resp.read()
# #respData=respData.encode('utf-8')
#
# dat=re.findall(r'"src"\s*:\s*"(.+?)"',str(respData))
# cap=re.findall(r'"text"\s*:\s*"(.+?)"',str(respData))
# print (str(respData))
# i=0
# rec=[]
# for x in dat:
#     if re.search("/s640x640/",x):
#         rec.append(x)
# print(rec)


# for _ in cap:
#     #ls=_.replace('\\\\','')
#     ls=_.replace('\\\\n',' ')
#     ls=ls.replace('\\\\u2014','')
#     ls=ls.replace(r'\\','')
#     print(ls)

def imLS():
    url = 'https://www.instagram.com/bas_kar_na_yar/?hl=en'
    data = req.Request(url)
    resp = req.urlopen(data)
    respData = resp.read()

    dat = re.findall(r'"src"\s*:\s*"(.+?)"', str(respData))
    #cap = re.findall(r'"text"\s*:\s*"(.+?)"', str(respData))
    print(str(respData))
    i = 0
    rec = []
    for x in dat:
        if re.search("/s640x640/", x):
            rec.append(x)
    return rec