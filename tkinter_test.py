# -*-  coding:utf-8 -*-

import os, getpass, time  
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import urllib
from urllib import request
import re
import PIL
from PIL import Image 

def get_img():
	name = nameent.get().encode('utf-8')
	if not name :
		Messagebox.showinfo('请输入名字继续')
		return
	html = urllib.request().urlopen('http://www.uustv.com/',data='word={}%sizes=60%fonts=jfttf%fontcolour=%23000000'.format(name)).read()
	reg = r'<div class="tu">﻿<img src=".*?"/></div>'
	imgurl = re.findall(reg,html)[0]
	imgurl ='http://www.uustv.com/'+imgurl
	urllib.urlretrieve(imgurl,'%s.gif'%name.decode('utf-8').encode('gbk'))
	try:
		im =  image.open('%s.gif'%name.decode('utf-8').encode('gbk'))
		im.show()
		im.close()
	except:
		print('请自行打开图片')


root = tk.Tk()  
#top=Tkinter.Tk()#创建一个顶层窗口对象  
label=tk.Label(root,text="姓名：",font=('微软雅黑',15)).grid()
nameent=Entry(root,font=('微软雅黑',15))
nameent.grid(row=0,column=1)
Button(root,text='一键设计签名',font=('微软雅黑'),width='15',height='1',command=get_img).grid()
root.title('艺术签名设计') 
root.geometry('500x300+500+200')

root.mainloop()