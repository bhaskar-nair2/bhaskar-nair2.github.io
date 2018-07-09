import urllib.request as req
import re

def is_ascii(s):
    try:
        s.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False


def imLS():
    url = 'https://www.instagram.com/bas_kar_na_yar/?hl=en'
    data = req.Request(url)
    resp = req.urlopen(data)
    respData = resp.read()

    dat = re.findall(r'"src"\s*:\s*"(.+?)"', str(respData))
    #cap = re.findall(r'"text"\s*:\s*"(.+?)"', str(respData))
    rec = []
    for x in dat:
        if re.search("/s640x640/", x):
            rec.append(x)
    return rec

# cap = re.findall(r'"text"\s*:\s*"(.+?)"', str(respData))