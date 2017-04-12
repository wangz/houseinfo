# houseinfo

本程序在线地址：http://www.houseinfo.online

start:
uwsgi --http :80 --chdir /root/git/ljdata/  --wsgi-file ljdata/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191 &>> slog




http://www.cnblogs.com/frchen/p/5709533.html


用python的BeautifulSoup分析html
http://www.cnblogs.com/twinsclover/archive/2012/04/26/2471704.html
https://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#The%20basic%20find%20method:%20findAll%28name,%20attrs,%20recursive,%20text,%20limit,%20**kwargs%29
https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
