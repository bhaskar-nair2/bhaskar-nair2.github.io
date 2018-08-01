import urllib.request as req
import re
import sqlite3 as sql


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
    # cap = re.findall(r'"text"\s*:\s*"(.+?)"', str(respData))
    rec = []
    for x in dat:
        if re.search("/s640x640/", x):
            rec.append(x)
    return rec


def getPosts():
    con = sql.Connection('static/blog')
    cur = con.cursor()
    lst = []
    rs = cur.execute('select * from blog order by data desc')
    for i in rs:
        lst.append(i)
    return lst

if __name__ == '__main__':
    print(getPosts())
