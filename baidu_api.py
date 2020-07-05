# -*- coding: utf-8 -*-
"""
# Talk is cheap,show me the codes!

@Author billie
@Time 2020/7/4 2:17 下午
@Describe 

"""
import requests


class Baidu_API():
    def __init__(self):
        self.headers={'Content-Type': 'application/json; charset=UTF-8'}
        self.AppID = '20705833'  # 百度应用账号ID
        self.APIKey = 'oeuVfpCfOrGOdtNtXUvpqMIY'  # 针对接口访问的授权方式
        self.SecretKey = 'qZoZAVzROfcs5sbYXUocHfSTcAq4nD1S'  # 密钥
    #获取access token值
    def get_access_token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(self.APIKey,self.SecretKey)
        response = requests.get(host,self.headers)
        if response:
            access_token=response.json()['access_token']
            # print(access_token)
            return access_token
        else:print("access_token获取失败")
    #获取转换图片格式为base64的图片数据
    def get_img_base64(self,img_path):
        # 先以二进制的格式读取图片，再转化为base64格式（使用二进制转base64格式的函数）
        import base64
        with open(img_path,'rb')as f:
            # base64编码
            img=base64.b64encode(f.read())
            # str强类型转换
            img_data=str(img,'utf-8')
        return img_data
    #功能1、对颜值进行评分
    def face_detect(self,img_path):
        try:
            # 访问人脸检测api
            base_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
            # 基本参数
            request_url = base_url + "?access_token=" + self.get_access_token()
            params = {"image": self.get_img_base64(img_path),
                      "image_type": "BASE64",
                      "face_field": "faceshape,facetype,beauty,age,beauty,glasses,gender,race"}
            # 开始访问
            response = requests.post(url=request_url,
                                      data=params,
                                      headers=self.headers)  # <class 'requests.models.Response'>
            re = response.json()  # <class 'dict'>
            print(re)
            score = re["result"]["face_list"][0]['beauty']
            age = re["result"]["face_list"][0]['age']
            gender = re["result"]["face_list"][0]['gender']['type']
            race = re["result"]["face_list"][0]['race']['type']
            # 返回数据
            return score,age,gender,race
        except:
            return '未能正确识别，请重试'

    #功能2、手势识别
    def gesture(self,img_path):
        try:
            base_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/gesture'
            # 基本参数
            request_url = base_url + "?access_token=" + self.get_access_token()
            params = {"image": self.get_img_base64(img_path),
                      "image_type": "BASE64"}
            # 开始访问
            response = requests.post(url=request_url,
                                     data=params,
                                     headers=self.headers)  # <class 'requests.models.Response'>
            re = response.json()  # <class 'dict'>
            print(re)
            classname_en = re["result"][0]['classname']
            classname_zh = translate(classname_en)
            return classname_en,classname_zh
        except:
            return '未能正确是识别，请重试'
    #功能3、识别银行卡号码
    def bankcard(self,img_path):
        try:
            base_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard'
            # 基本参数
            request_url = base_url + "?access_token=" + self.get_access_token()
            params = {"image": self.get_img_base64(img_path)}
            # 开始访问
            response = requests.post(url=request_url,
                                     data=params,
                                     headers=self.headers)  # <class 'requests.models.Response'>
            re = response.json()  # <class 'dict'>
            print(re)
            bank_card_number,bank_name = re["result"]['bank_card_number'],re["result"]['bank_name']
            return bank_card_number,bank_name
        except:
            return '未能正确识别，请重试'
    #功能4、识别植物
    def plant(self,img_path):
        try:
            base_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/plant'
            # 基本参数
            request_url = base_url + "?access_token=" + self.get_access_token()
            params = {"image": self.get_img_base64(img_path)}
            # 开始访问
            response = requests.post(url=request_url,
                                     data=params,
                                     headers=self.headers)  # <class 'requests.models.Response'>
            re = response.json()  # <class 'dict'>
            print(re)
            name,score,els = re["result"][0]['name'],re["result"][0]['score'],[i['name'] for i in re['result'][1:]]
            return name,score,els
        except:
            return '未能正确识别，请重试'

#翻译
def translate(query):
    url = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}'.format(query)
    r = requests.post(url=url)
    return r.json()['translateResult'][0][0]['tgt'].strip('的')