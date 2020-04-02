#!/usr/bin/env python3

import urllib.request
import os
import subprocess
import sys
import zipfile
from bs4 import BeautifulSoup
import ssl

url2 = "https://felis.kernelblog.org/aseo/aseo.zip"
context = ssl._create_unverified_context()

prefix = "/usr"
sudo = "sudo"

os.system(sudo+"pip3 install beautifulsoup4 requests PyQt5 --upgrade")

veri = urllib.request.urlopen(url2, context = context)
f = open("aseo.zip", 'wb')
f.write(veri.read())
f.close()
feliszip = zipfile.ZipFile("aseo.zip","r")
feliszip.extractall(path=None, members=None)
os.system("rm aseo.zip")
ls = os.popen("ls "+os.getcwd()+"/aseo")
ls = list(ls)
for i in ls:
	i = i.replace("\n","")
	if i == "aseo":
		os.system(sudo+"rm "+prefix+"/bin/aseo")
		os.system(sudo+"mv "+os.getcwd()+"/aseo/aseo "+prefix+"/bin/")
		os.system(sudo+"chmod 755 "+prefix+"/bin/aseo")
	elif i == "kur.sh":
		pass
	elif i == "ekstra.py":
		os.system("python3 "+os.getcwd()+"/aseo/ekstra.py")
	else:
		os.system(sudo+"rm "+prefix+"/share/aseo/"+i)
		os.system(sudo+"mv "+os.getcwd()+"/aseo/"+i+" "+prefix+"/share/aseo/")
		os.system(sudo+"chmod 755 "+prefix+"/share/aseo/"+i)
print("\nA+SEO Başarıyla Güncellendi.")
os.system("rm -r aseo")
