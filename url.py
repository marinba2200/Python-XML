import random
from urllib.request import urlretrieve
import os
#下载300张验证码图片
url = 'http://www.moguproxy.com/proxy/validateCode/createCode?time={}'
path = os.path.dirname('C:/Users/KENNY_WU/Desktop/1234/test') #将下载的图片保存到当前目录下的origin_imgs文件夹中

for i in range(1531878604000,1531878604300):
    urlretrieve(url.format(i), path + str(i)[-3:] + '.jpg')
    print('成功下载 {} 张图片'.format(str(i)[-3:]))
