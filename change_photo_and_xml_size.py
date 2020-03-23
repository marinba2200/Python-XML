import os
import xml.etree.ElementTree as ET
import math
from PIL import Image

fro_m = 'C:/Users/KENNY_WU/Desktop/test/'#來源XML
t_o = 'C:/Users/KENNY_WU/Desktop/test3/'#目的XML

fro_m2 = 'C:/Users/KENNY_WU/Desktop/photo/'#影像來源資料夾
t_o2 = 'C:/Users/KENNY_WU/Desktop/photo/123/'#影像目的資料夾

i = 300  #縮放設定
min_ = 30  #xml最小物件

name = 'a'  #檔名前增加字串 : n + 原檔名
ext = '.jpg'  #影像檔格式
qua = 100  #quality
proportion = 2 #影像長寬比，超出比例則跳過


def test1():
    global width_size
    width_size = i/width

def test2():
    global height_size 
    height_size = i/height

width_size = 0
height_size = 0

sum1,sum2,sum3,sum4,sum5,sum6 = 0,0,0,0,0,0

while True:
    print('1.影像檔格式不變更')
    print('2.影像檔格式改為自行設定之格式')
    m = input('請輸入需執行:')
    if (m == '1')|(m == '2'):                   
        break
    else:
         print('輸入錯誤，請重新輸入。')
         
while True:
    print('')
    print('1.僅執行xml檔縮小')
    print('2.僅執行影像檔縮小')
    print('3.xml檔與影像檔皆執行縮小')
    k = input('請輸入需執行:')
    if (k == '1')|(k == '2')|(k == '3'):
        break                  
    else:
        print('輸入錯誤，請重新輸入。')
                    
while True:
    print('')
    print('若原影像小於修改尺寸的影像則:')
    print('1.全部修改')
    print('2.全部不修改')
    print('3.逐一詢問是否修改')
    g = input('請輸入需執行:')
    if (g == '1')|(g == '2')|(g == '3'):
        break     
    else:
        print('輸入錯誤，請重新輸入。')
        
        
for file2 in os.listdir(fro_m2):  
    sum4 +=1
for file1 in os.listdir(fro_m):  #xml來源
    sum1 +=1
    if (os.path.splitext(fro_m + file1)[-1]) == '.xml':  #判斷是否為xml檔
        sum2 +=1
        tree = ET.parse(fro_m + file1)  #開啟xml檔
        root = tree.getroot()
        for file2 in os.listdir(fro_m2):  #影像來源
            if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
                if (file1.split('.')[0]) == (file2.split('.')[0]):
                     sum5 +=1
                     im = Image.open(fro_m2 + file2)
                     (a,b) = im.size
                     if (a/b > proportion)|(b/a > proportion):
                        print(file2,'超出長寬比',proportion,'不做處理')
                     else:
                         if (k == '2')|(k == '3'):
                            if (g == '1'):
                                    
                                im_ = im.resize( (i,i), Image.BILINEAR )
                                if (m == '1'):
                                    im_.save(t_o2 + name + file2 , quality=qua)
                                if (m == '2'):
                                    im_.save(t_o2 + name + file2.split('.')[0] + ext , quality=qua)
                                print(file2,'縮放成功')
                                sum6 +=1

                                    
                            if (g == '2'):
                                        
                                if (a < i)|(b < i):

                                    print(file2,'影像檔',a,'x',b,'小於',i,'直接複製')
                                    sum6 +=1
                                    if (m == '1'):
                                        im.save(t_o2 + name + file2 , quality=qua)
                                    if (m == '2'):
                                        im.save(t_o2 + name + file2.split('.')[0] + ext , quality=qua)
                                                    
                                else:
                                    im_ = im.resize( (i,i), Image.BILINEAR )
                                    if (m == '1'):
                                        im_.save(t_o2 + name + file2 , quality=qua)
                                    if (m == '2'):
                                        im_.save(t_o2 + name + file2.split('.')[0] + ext , quality=qua)
                                    print(file2,'縮放成功')
                                    sum6 +=1
                
                            if (g == '3'):
                                        
                                if (a < i)|(b < i):
                                            
                                    while True:
                                        print(file2,'影像檔',a,'x',b,'小於',i)
                                        h = input('是否覆蓋Y/N:')
                                        if (h == 'Y')|(h == 'y')|(h == 'N')|(h == 'n'):
                                            break
                                                
                                        else:
                                            print('輸入錯誤，請重新輸入。')
                                                    
                                    if (h == 'Y')|(h == 'y'):        
                                        im_ = im.resize( (i,i), Image.BILINEAR )
                                        if (m == '1'):
                                            im_.save(t_o2 + name + file2 , quality=qua)
                                        if (m == '2'):
                                            im_.save(t_o2 + name + file2.split('.')[0] + ext , quality=qua)
                                        print(file2,'縮放成功')
                                        sum6 +=1


                                    else:
                                        print(file2,'影像檔','直接複製')
                                        sum6 +=1
                                        if (m == '1'):
                                            im.save(t_o2 + name + file2 , quality=qua)
                                        if (m == '2'):
                                            im.save(t_o2 + name + file2.split('.')[0] + ext , quality=qua)
                                                    
                                else:
                                    im_ = im.resize( (i,i), Image.BILINEAR )
                                    if (m == '1'):
                                        im_.save(t_o2 + name + file2 , quality=qua)
                                    if (m == '2'):
                                        im_.save(t_o2 + name + file2.split('.')[0] + ext , quality=qua)
                                    print(file2,'縮放成功')
                                    sum6 +=1

                                            
                         if (k == '1')|(k == '3'):
                                    if (m == '1'):    
                                        for names in root.iter('filename'):
                                            filename = names.text  #獲取內容
                                            new_names = name + file2  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                            names.text = new_names   #修改內容
                                        for paths in root.iter('path'):
                                            path = paths.text  #獲取內容
                                            new_paths =t_o2 + name + file2  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                            paths.text = new_paths   #修改內容
                                    if (m == '2'):
                                        for names in root.iter('filename'):
                                            filename = names.text  #獲取內容
                                            new_names = name + file2.split('.')[0] + ext  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                            names.text = new_names   #修改內容
                                        for paths in root.iter('path'):
                                            path = paths.text  #獲取內容
                                            new_paths = t_o2 + name + file2.split('.')[0] + ext  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                            paths.text = new_paths   #修改內容
                                    if (g == '1'):
                                        
                                        for sizes in root.iter('width'):
                                            width = int(sizes.text)  #獲取內容
                                            test1()
                                            new_size = str(round(float(width)*width_size))#調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                            sizes.text = new_size   #修改內容
                                        
                                        for sizes in root.iter('height'):
                                            height = int(sizes.text)  #獲取內容
                                            test2()
                                            new_size = str(round(float(height)*height_size))#調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                            sizes.text = new_size   #修改內容
                                            
                                    
                                        for node in root.iter('xmin'):  #修改xmin框框大小(無條件捨去)
                                            xmin = node.text  #獲取內容
                                            new_size = str(int(float(xmin)*width_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                            node.text = new_size  #修改內容
                                                        
                                        for node in root.iter('ymin'):  #修改xmin框框大小(無條件捨去)
                                            ymin = node.text  #獲取內容
                                            new_size = str(int(float(ymin)*height_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                            node.text = new_size  #修改內容
                                                
                                        for node in root.iter('xmax'):
                                            xmax = node.text  #獲取內容
                                            new_size3 = str(math.ceil(float(xmax)*width_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                            node.text = new_size3  #修改內容
                                                
                                        for node in root.iter('ymax'):
                                            ymax = node.text  #獲取內容
                                            new_size3 = str(math.ceil(float(ymax)*height_size))  #調整大小:節點資料為字串，先轉換成整數型態做修改後再轉換回字串
                                            node.text = new_size3  #修改內容
                                                
                                            
                                        for node in root.findall('object'):
                                            for bndbox in node.findall('bndbox'):#繼續找到bndbox的標籤
                                                xmin = float(bndbox.find('xmin').text)#繼續找到xmin的標籤
                                                xmax = float(bndbox.find('xmax').text)#繼續找到xmin的標籤
                                                ymin = float(bndbox.find('ymin').text)#繼續找到xmin的標籤
                                                ymax = float(bndbox.find('ymax').text)#繼續找到xmin的標籤
                                                if (float(xmax)-float(xmin))*(float(ymax)-float(ymin)) < min_:  #最小門檻
                                                    root.remove(node)#移除這個標籤
                                    if (g == '2'):
                                        if (a < i)|(b < i):
                                            pass
                                        else:
                                            for sizes in root.iter('width'):
                                                width = int(sizes.text)  #獲取內容
                                                test1()
                                                new_size = str(round(float(width)*width_size))#調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                sizes.text = new_size   #修改內容
                                            
                                            for sizes in root.iter('height'):
                                                height = int(sizes.text)  #獲取內容
                                                test2()
                                                new_size = str(round(float(height)*height_size))#調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                sizes.text = new_size   #修改內容
                                                
                                        
                                            for node in root.iter('xmin'):  #修改xmin框框大小(無條件捨去)
                                                xmin = node.text  #獲取內容
                                                new_size = str(int(float(xmin)*width_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                node.text = new_size  #修改內容
                                                            
                                            for node in root.iter('ymin'):  #修改xmin框框大小(無條件捨去)
                                                ymin = node.text  #獲取內容
                                                new_size = str(int(float(ymin)*height_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                node.text = new_size  #修改內容
                                                    
                                            for node in root.iter('xmax'):
                                                xmax = node.text  #獲取內容
                                                new_size3 = str(math.ceil(float(xmax)*width_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                node.text = new_size3  #修改內容
                                                    
                                            for node in root.iter('ymax'):
                                                ymax = node.text  #獲取內容
                                                new_size3 = str(math.ceil(float(ymax)*height_size))  #調整大小:節點資料為字串，先轉換成整數型態做修改後再轉換回字串
                                                node.text = new_size3  #修改內容
                                                    
                                                
                                            for node in root.findall('object'):
                                                for bndbox in node.findall('bndbox'):#繼續找到bndbox的標籤
                                                    xmin = float(bndbox.find('xmin').text)#繼續找到xmin的標籤
                                                    xmax = float(bndbox.find('xmax').text)#繼續找到xmin的標籤
                                                    ymin = float(bndbox.find('ymin').text)#繼續找到xmin的標籤
                                                    ymax = float(bndbox.find('ymax').text)#繼續找到xmin的標籤
                                                    if (float(xmax)-float(xmin))*(float(ymax)-float(ymin)) < min_:  #最小門檻
                                                        root.remove(node)#移除這個標籤
                                            
                                    if (g == '3'):
                                        if (a < i)|(b < i):
                                            if (h == 'Y')|(h == 'y'):
                                                for sizes in root.iter('width'):
                                                    width = int(sizes.text)  #獲取內容
                                                    test1()
                                                    new_size = str(round(float(width)*width_size))#調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                    sizes.text = new_size   #修改內容
                                                
                                                for sizes in root.iter('height'):
                                                    height = int(sizes.text)  #獲取內容
                                                    test2()
                                                    new_size = str(round(float(height)*height_size))#調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                    sizes.text = new_size   #修改內容
                                                    
                                            
                                                for node in root.iter('xmin'):  #修改xmin框框大小(無條件捨去)
                                                    xmin = node.text  #獲取內容
                                                    new_size = str(int(float(xmin)*width_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                    node.text = new_size  #修改內容
                                                                
                                                for node in root.iter('ymin'):  #修改xmin框框大小(無條件捨去)
                                                    ymin = node.text  #獲取內容
                                                    new_size = str(int(float(ymin)*height_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                    node.text = new_size  #修改內容
                                                        
                                                for node in root.iter('xmax'):
                                                    xmax = node.text  #獲取內容
                                                    new_size3 = str(math.ceil(float(xmax)*width_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                    node.text = new_size3  #修改內容
                                                        
                                                for node in root.iter('ymax'):
                                                    ymax = node.text  #獲取內容
                                                    new_size3 = str(math.ceil(float(ymax)*height_size))  #調整大小:節點資料為字串，先轉換成整數型態做修改後再轉換回字串
                                                    node.text = new_size3  #修改內容
                                                        
                                                    
                                                for node in root.findall('object'):
                                                    for bndbox in node.findall('bndbox'):#繼續找到bndbox的標籤
                                                        xmin = float(bndbox.find('xmin').text)#繼續找到xmin的標籤
                                                        xmax = float(bndbox.find('xmax').text)#繼續找到xmin的標籤
                                                        ymin = float(bndbox.find('ymin').text)#繼續找到xmin的標籤
                                                        ymax = float(bndbox.find('ymax').text)#繼續找到xmin的標籤
                                                        if (float(xmax)-float(xmin))*(float(ymax)-float(ymin)) < min_:  #最小門檻
                                                            root.remove(node)#移除這個標籤
                                            if (h == 'N')|(h == 'n'):
                                                pass
                                        else:
                                                for sizes in root.iter('width'):
                                                    width = int(sizes.text)  #獲取內容
                                                    test1()
                                                    new_size = str(round(float(width)*width_size))#調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                    sizes.text = new_size   #修改內容
                                                
                                                for sizes in root.iter('height'):
                                                    height = int(sizes.text)  #獲取內容
                                                    test2()
                                                    new_size = str(round(float(height)*height_size))#調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                    sizes.text = new_size   #修改內容
                                                    
                                            
                                                for node in root.iter('xmin'):  #修改xmin框框大小(無條件捨去)
                                                    xmin = node.text  #獲取內容
                                                    new_size = str(int(float(xmin)*width_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                    node.text = new_size  #修改內容
                                                                
                                                for node in root.iter('ymin'):  #修改xmin框框大小(無條件捨去)
                                                    ymin = node.text  #獲取內容
                                                    new_size = str(int(float(ymin)*height_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                    node.text = new_size  #修改內容
                                                        
                                                for node in root.iter('xmax'):
                                                    xmax = node.text  #獲取內容
                                                    new_size3 = str(math.ceil(float(xmax)*width_size))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                                    node.text = new_size3  #修改內容
                                                        
                                                for node in root.iter('ymax'):
                                                    ymax = node.text  #獲取內容
                                                    new_size3 = str(math.ceil(float(ymax)*height_size))  #調整大小:節點資料為字串，先轉換成整數型態做修改後再轉換回字串
                                                    node.text = new_size3  #修改內容
                                                        
                                                    
                                                for node in root.findall('object'):
                                                    for bndbox in node.findall('bndbox'):#繼續找到bndbox的標籤
                                                        xmin = float(bndbox.find('xmin').text)#繼續找到xmin的標籤
                                                        xmax = float(bndbox.find('xmax').text)#繼續找到xmin的標籤
                                                        ymin = float(bndbox.find('ymin').text)#繼續找到xmin的標籤
                                                        ymax = float(bndbox.find('ymax').text)#繼續找到xmin的標籤
                                                        if (float(xmax)-float(xmin))*(float(ymax)-float(ymin)) < min_:  #最小門檻
                                                            root.remove(node)#移除這個標籤

                                    
                                    tree.write(t_o + name + file1)  #目的XML
                                    sum3 +=1
                                    print(file1)

print('xml資料夾輸入總數',sum1)
print('xml檔案總數',sum2)
print('完成縮放xml總數',sum3)

print('影像資料夾檔案總數',sum4)
print('影像檔案總數',sum5)
print('完成縮放影像總數',sum6)
