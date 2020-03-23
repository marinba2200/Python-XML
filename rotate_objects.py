import os
import xml.etree.ElementTree as ET
import math
from PIL import Image

fro_m = 'C:/Users/KENNY_WU/Desktop/test6666/test/512Annotations/'#來源XML
t_o = 'C:/Users/KENNY_WU/Desktop/test6666/test/test/xml/'#目的XML

fro_m2 = 'C:/Users/KENNY_WU/Desktop/test6666/test/512JPEGImages/'#影像來源資料夾
t_o2 = 'C:/Users/KENNY_WU/Desktop/test6666/test/test/photo/'#影像目的資料夾

m=[0]  #調整角度(向右旋轉)
r='r'  #檔名後增加字串: 原檔名 + '_' + r + 旋轉角度
n = 'a'  #檔名前增加字串 : n + 原檔名
ext = '.png'  #影像檔格式
qua = 100  #quality



sum3 = 0
sum6 = 0

while True:
    print('1.影像檔格式不變更')
    print('2.影像檔格式改為自行設定之格式')
    k = input('請輸入需執行:')
    if (k == '1')|(k == '2'):
        break
                
    else:
        print('輸入錯誤，請重新輸入。')
for i in m:
    A = '_' + r + str(i)
    if (i == 0):
        A=''
    sum1,sum2 = 0,0
    sum4,sum5 = 0,0
    for file in os.listdir(fro_m):  #來源XML
        sum1 +=1
        if (os.path.splitext(fro_m + file)[-1]) == '.xml':  #判斷是否為xml檔
            sum2 += 1

            tree = ET.parse(fro_m + file)  #開啟xml檔
            root = tree.getroot()

            for file2 in os.listdir(fro_m2):  #影像來源
                sum4 +=1
                if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                    ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                    ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
                    sum5 +=1
                    if (file.split('.')[0]) == (file2.split('.')[0]):
                        
                        im = Image.open(fro_m2 + file2)
                        im2 = im.rotate(-i,expand=True)

                        if (k == '1'):
                            im2.save(t_o2 + n + file2.split('.')[0] + A + '.' + file2.split('.')[1] , quality=qua)
                            
                            for names in root.iter('filename'):
                                filename = names.text  #獲取內容
                                new_names = n + file.split('.')[0] + A + '.' + file2.split('.')[1]  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                names.text = new_names   #修改內容
                            for paths in root.iter('path'):
                                path = paths.text  #獲取內容
                                new_paths = t_o + n + file.split('.')[0] + A+ '.' + file2.split('.')[1]  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                paths.text = new_paths   #修改內容
                            print(file2,i)
                            sum6 +=1
                        if (k == '2'):
                            im2.save(t_o2 + n + file2.split('.')[0] + A + ext , quality=qua)
                            
                            for names in root.iter('filename'):
                                filename = names.text  #獲取內容
                                new_names = n + file.split('.')[0] + A + ext  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                names.text = new_names   #修改內容
                            for paths in root.iter('path'):
                                path = paths.text  #獲取內容
                                new_paths = t_o + n + file.split('.')[0] + A + ext  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                paths.text = new_paths   #修改內容
                            print(file2,i)
                            sum6 +=1
                        (a,b) = im2.size

                        
                        for sizes1 in root.iter('width'):
                            width = float(sizes1.text)  #獲取內容
                            w_xmax = width
                            w_xmin = 0
                            #影像檔的WH為xmax與ymax 00為min，做旋轉，xy各四個值，最大值最小值相減即為新WH，除以2得新中心點，與原中心點相減即為誤差，將誤差與新物件座標相加
                            #new_size = math.cos(i*math.pi/180)*(width/2)  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                            #sizes.text = str(new_size+(width/2))  #修改內容
                        for sizes2 in root.iter('height'):
                            height = float(sizes2.text)  #獲取內容
                            h_ymax = height
                            h_ymin = 0
                            #new_size = math.cos(i*math.pi/180)*(height/2)  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                            #sizes.text = str(new_size+(height/2))  #修改內容
                        cos_w_xmin = round(math.cos(i*math.pi/180)*(w_xmin-(width/2)))
                        cos_w_xmax = round(math.cos(i*math.pi/180)*(width/2))
                        sin_w_xmin = round(math.sin(i*math.pi/180)*(w_xmin-(width/2)))
                        sin_w_xmax = round(math.sin(i*math.pi/180)*(width/2))
                        cos_h_ymin = round(math.cos(i*math.pi/180)*(h_ymin-(height/2)))
                        cos_h_ymax = round(math.cos(i*math.pi/180)*(height/2))
                        sin_h_ymin = round(math.sin(i*math.pi/180)*(h_ymin-(height/2)))
                        sin_h_ymax = round(math.sin(i*math.pi/180)*(height/2))
                        

                        w_xmin_1 = cos_w_xmin - sin_h_ymax
                        w_xmin_2 = cos_w_xmin - sin_h_ymin
                        w_xmax_1 = cos_w_xmax - sin_h_ymax
                        w_xmax_2 = cos_w_xmax - sin_h_ymin
                        h_ymin_1 = sin_w_xmin + cos_h_ymax
                        h_ymin_2 = sin_w_xmin + cos_h_ymin
                        h_ymax_1 = sin_w_xmax + cos_h_ymin
                        h_ymax_2 = sin_w_xmax + cos_h_ymax

                        new_w_xmin_ = min(w_xmin_1,w_xmin_2,w_xmax_1,w_xmax_2)+(width/2)
                        new_w_xmax_ = max(w_xmin_1,w_xmin_2,w_xmax_1,w_xmax_2)+(width/2)
                        new_h_ymin_ = min(h_ymin_1,h_ymin_2,h_ymax_1,h_ymax_2)+(height/2)
                        new_h_ymax_ = max(h_ymin_1,h_ymin_2,h_ymax_1,h_ymax_2)+(height/2)

                        

                        new_w_xmin = int(new_w_xmin_)
                        new_w_xmax = math.ceil(new_w_xmax_)
                        new_h_ymin = int(new_h_ymin_)
                        new_h_ymax = math.ceil(new_h_ymax_)

                        new_width = new_w_xmax-new_w_xmin
                        new_height = new_h_ymax-new_h_ymin

                        sizes1.text = str(a)
                        sizes2.text = str(b)

                        for node in root.findall('object'):
                            for bndbox in node.findall('bndbox'):#繼續找到bndbox的標籤
                                for x_min in bndbox.findall('xmin'):
                                    xmin = x_min.text
                                for x_max in bndbox.findall('xmax'):
                                    xmax = x_max.text
                                for y_min in bndbox.findall('ymin'):
                                    ymin = y_min.text
                                for y_max in bndbox.findall('ymax'):
                                    ymax = y_max.text

                                cos_xmin = math.cos(i*math.pi/180)*(float(xmin)-(width/2))
                                cos_xmax = math.cos(i*math.pi/180)*(float(xmax)-(width/2))
                                sin_xmin = math.sin(i*math.pi/180)*(float(xmin)-(width/2))
                                sin_xmax = math.sin(i*math.pi/180)*(float(xmax)-(width/2))
                                cos_ymin = math.cos(i*math.pi/180)*(float(ymin)-(height/2))
                                cos_ymax = math.cos(i*math.pi/180)*(float(ymax)-(height/2))
                                sin_ymin = math.sin(i*math.pi/180)*(float(ymin)-(height/2))
                                sin_ymax = math.sin(i*math.pi/180)*(float(ymax)-(height/2))
                                
                                xmin_1 = cos_xmin - sin_ymax
                                xmin_2 = cos_xmin - sin_ymin
                                xmax_1 = cos_xmax - sin_ymax
                                xmax_2 = cos_xmax - sin_ymin
                                ymin_1 = sin_xmin + cos_ymax
                                ymin_2 = sin_xmin + cos_ymin
                                ymax_1 = sin_xmax + cos_ymin
                                ymax_2 = sin_xmax + cos_ymax

                                a1 = int(min(xmin_1,xmin_2,xmax_1,xmax_2)+(new_width/2))
                                b1 = math.ceil(max(xmax_1,xmax_2,xmin_1,xmin_2)+(new_width/2))
                                c1 = int(min(ymin_1,ymin_2,ymax_1,ymax_2)+(new_height/2))
                                d1 = math.ceil(max(ymax_1,ymax_2,ymin_1,ymin_2)+(new_height/2))

                                if (a1 < 0 ):
                                    a1 = 0
                                if (b1 > a ):
                                    b1 = a-1
                                if (c1 < 0 ):
                                    c1 = 0
                                if (d1 > b ):
                                    d1 = b-1

                                x_min.text = str(a1)
                                x_max.text = str(b1)
                                y_min.text = str(c1)
                                y_max.text = str(d1)
                                

                        tree.write(t_o + n + file.split('.')[0] + A + '.' + file.split('.')[1])  #目的XML
                        print(file,i)
                        sum3 +=1
        
print('xml資料夾檔案總數',sum1)
print('輸入xml',sum2)
print('輸出xml',sum3)

print('影像資料夾檔案總數',sum1)
print('輸入影像',sum2)
print('輸出影像',sum3)
