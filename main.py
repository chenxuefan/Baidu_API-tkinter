# -*- coding: utf-8 -*-
"""
# Talk is cheap,show me the codes!

@Author billie
@Time 2020/7/1 8:11 下午
@Describe 

"""
import tkinter as tk
from pprint import pprint
from tkinter import *
from tkinter import filedialog
from tkinter import ttk #下拉框依赖库
from tkinter import scrolledtext #滚动文本框依赖库
import cv2 as cv #pip install opencv-python
import os,time
#引入Baidu_API类
from baidu_api import Baidu_API


#拍照
def take_a_photo():
    # 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
    cap = cv.VideoCapture(0)
    img_path = "./screenshot.jpg"
    while True:
        # 从摄像头读取图片
        sucess, img = cap.read()
        # 转为灰度图片
        # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)#
        # 显示摄像头
        cv.imshow('----------please enter "s" to take a picture----------', img)
        # 保持画面的持续,无限期等待输入
        k = cv.waitKey(1)
        if k == 27:
            # 通过esc键退出摄像
            cv.destroyAllWindows()
            break
        elif k == ord("s"):
            # 通过s键保存图片，并退出。
            cv.imwrite(img_path, img)
            cv.destroyAllWindows()
            break
    # 关闭摄像头
    cap.release()
    # 打印日志
    scr.insert(tk.END, '[{}]拍摄成功...\n'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
    # 返回图像
    return img_path


#----------图形界面各个组件功能的设计----------
#清除窗口日志
def clear_the_window():
    scr.delete(1.0,tk.END)
#退出软件
def exit():
    win.quit()
#下拉框选项选择
def select_ttk(event):
    global numberChosen
    #颜值评分
    if numberChosen.current()==1:
        # 获取图像
        img_path = take_a_photo()

        try:
            # 向API发送图像并获取信息
            score,age,gender,race = Baidu_API().face_detect(img_path=img_path)

            # 打印日志
            scr.insert(tk.END, '[{}]年龄「{}」性别「{}」人种「{}」\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'),age,gender,race))
            scr.insert(tk.END, '[{}]颜值评分为：{}/100 分\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'),score))
        except:
            scr.insert(tk.END, '[{}]{}'.format(time.strftime(time.strftime('%Y-%m-%d %H:%M:%S')),Baidu_API().face_detect(img_path=img_path)))
    #手势识别
    if numberChosen.current()==2:
        scr.insert(tk.END,'[{}]请将您的手势放置摄像头前...\n'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
        time.sleep(0.1)
        img_path = take_a_photo()
        try:
            classname_en,classname_zh = Baidu_API().gesture(img_path=img_path)
            scr.insert(tk.END,'[{}]手势大意：{}({})\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'),classname_zh,classname_en))
        except:
            scr.insert(tk.END,'[{}]{}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'),Baidu_API().gesture(img_path=img_path)))
    #银行卡号码识别
    if numberChosen.current()==3:
        scr.insert(tk.END,'[{}]请将您的银行卡放置摄像头前...\n'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
        img_path = take_a_photo()
        try:
            bank_card_number,bank_name = Baidu_API().bankcard(img_path=img_path)
            scr.insert(tk.END, '[{0}]您的银行卡号码（{2}）:{1}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'), bank_card_number, bank_name))
        except:
            scr.insert(tk.END, '[{}]{}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'),Baidu_API().bankcard(img_path=img_path)))
    #植物识别
    if numberChosen.current()==4:
        scr.insert(tk.END,'[{}]请将您的植物放置摄像头前...\n'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
        img_path = take_a_photo()
        try:
            name,score,els = Baidu_API().plant(img_path=img_path)
            scr.insert(tk.END, '[{}]植物名称：{}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'), name))
            scr.insert(tk.END, '[{}]还有可能是：{}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'), els))
        except:
            scr.insert(tk.END, '[{}]{}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'),Baidu_API().bankcard(img_path=img_path)))






#-------------创建窗口--------------
win = tk.Tk()
win.title('客官，来点啥？')
win.geometry('600x300')

#------------窗口组件设计-----------
#grid参数：column, columnspan, in, ipadx, ipady, padx, pady, row, rowspan,sticky

#下拉框组件
number=tk.StringVar
numberChosen  = ttk.Combobox(win,textvariable=number)
numberChosen['value']=('please select','给我的颜值打个分吧！','识别一下我的手势','识别一下我的银行卡号码','识别一下我的植物')
numberChosen.current(0)#设置默认值为第一个，即默认下拉框中的内容
numberChosen.grid(row=1,column=1,rowspan=1,sticky=N+E+S+W)
#下拉框触发动作
numberChosen.bind('<<ComboboxSelected>>',select_ttk)

#清除按钮组件
tk.Button(win,cnf={'text':'clear','command':clear_the_window})\
       .grid(row=1,column=2,ipadx=1,sticky=N+E+S+W)

#退出按钮组件
tk.Button(win,cnf={'text':'exit','command':exit})\
       .grid(row=1,column=3,ipadx=1,sticky=N+E+S+W)

#滚动文本框组件
scr = scrolledtext.ScrolledText(win)
scr.grid(row=2,column=1,columnspan=3,rowspan=1)

#使窗口一直显示
win.mainloop()
#