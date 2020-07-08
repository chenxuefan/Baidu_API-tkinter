# Baidu_API-tkinter

1.前言
---
1.1.	引言<br>
###
GUI应用程序，也称图形界面开发，或“上位机“，是采用图形方式显示的计算机操作用户界面。图形用户界面是一种人与计算机通信的界面显示格式，允许用户使用鼠标等输入设备操纵屏幕上的图标或菜单选项，以选择命令、调用文件、启动程序或执行其它一些日常任务。用户只要打开程序，程序的界面会让用户在最短的时间内找到他们需要的功能，同时主动带领用户完成他们的工作并得到最好的体验。<br><br>
1.2.	编写目的<br>	
###
本项目结合人工智能和GUI图形界面开发，满足用户对图像识别方面的需求。
	
2.项目阐述
---
2.1.	产品功能<br>
###
调用电脑摄像头实现拍照，并使用百度API接口实现图像识别<br><br>
2.2.	预期用户量<br>
###
由于宣传力度有限，暂定100<br><br>
2.3.	实用性<br>
###
本项目围绕图像识别，通过调用百度API接口，可以实现很多人性化的功能，比如识别图像信息、比对图像差异以及颜值打分等功能<br><br>
2.4.	产品价值<br>
###
每个人都会对新兴事物抱有强烈的好奇心，人工智能亦是如此，本项目通过应用摄像头进行拍照识别的交互方式，给予用户足够的新鲜感，同时其功能也具有一定的实用性。

3.面向用户分析
---
3.1.	年龄段<br>
###
本产品不局限于使用的年龄段，任何人都能够在短时间内，根据软件的指引进行操作，并且很快就能够上手。<br><br>

3.2.	群体<br>
###
本产品不局限于使用的群体，不管是对于学生老师还是职场人士，本产品都会受到青睐。<br>

4.功能需求分析
---
4.1.	功能结构图<br>
###
![](https://github.com/chenxuefan/Baidu_API-tkinter/blob/master/img/structure.png)<br>
4.2.	具体功能列表<br>
###

| 颜值评分（face_detect） | 调用摄像头进行拍照识别，识别结果包括「年龄」「性别」「人种」「颜值评分」 | https://aip.baidubce.com/rest/2.0/face/v3/detect |
<br>
| 手势识别（gesture） | 调用摄像头进行拍照识别，识别结果为手势的「中文大意」和「英文大意」 | https://aip.baidubce.com/rest/2.0/image-classify/v1/gesture |
<br>
| 银行卡识别（bankcard） | 调用摄像头进行拍照识别，识别结果为「银行卡号码」和「银行名称」 | https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard |
<br>
| 植物识别（plant） | 调用摄像头进行拍照识别，识别结果为「植物名称」和「其他可能的结果」 | https://aip.baidubce.com/rest/2.0/image-classify/v1/plant |


5.技术需求分析
---
5.1.	程序开发技术
###
![](https://github.com/chenxuefan/Baidu_API-tkinter/blob/master/img/main_tec.png)<br>
5.2.	API接口技术 
###
![](https://github.com/chenxuefan/Baidu_API-tkinter/blob/master/img/api_tec.png)<br>
5.3.	性能需求
###
暂无测试

6.团队计划和分工
---
6.1.	项目名称：客官，来点啥？<br>
###
6.2.	组员：陈学帆、周深<br>
###
6.3.	团队分工：<br>
###
陈学帆	百度API接口的使用、拍照功能<br>
周深	图形界面的开发<br>
6.4.	Issue截图
###
![](https://github.com/chenxuefan/Baidu_API-tkinter/blob/master/img/scr_shot.png)<br>

7.团队GitHub仓库
---
仓库地址：https://github.com/chenxuefan/Baidu_API-tkinter
	

8.总结和感想
---
这次项目的开发，学到了很多关于人工智能方面的有趣的知识，也是一次很成功的尝试，期待以后能够多多在这方面实践一下。



