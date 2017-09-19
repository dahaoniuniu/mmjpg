import urllib.request
import re

mmnum = 1111 #最新套图编号
while mmnum >= 1100: #下到第几套
    x = 1
    page = str(mmnum)
    res = urllib.request.urlopen("http://m.mmjpg.com/mm/" + page)
    ret = res.read()
    ret = ret.decode('utf-8')
    max = re.findall(r'第\(1/(.*?)\)张', ret, re.S)
    maxnum = int(".".join(max))
    while x <= maxnum:
        picnum = str(x)
        res = urllib.request.urlopen("http://m.mmjpg.com/mm/" + page + "/" + picnum)
        ret = res.read()
        ret = ret.decode('utf-8')
        m = re.findall(r'<div class="picinfo">.*?<img src="(.*?)" alt="', ret, re.S)
        imgurl = ".".join(m)
        print(imgurl)
        filename = re.findall(r'<div class="picinfo">.*?" alt="(.*?)" /></a></div>', ret, re.S)
        name = str(filename)
        urllib.request.urlretrieve(imgurl, "./"+name+".jpg") #第一个引号中填入保存路径
        x += 1
    mmnum -= 1
