import os
import xml.etree.ElementTree as ET
import math

fro_m = 'C:/Users/KENNY_WU/Desktop/test/'#來源XML
t_o = 'C:/Users/KENNY_WU/Desktop/test3/'#目的XML
i=300  #xml比例調整
min_=30  #xml最小物件

width_size = 0
height_size = 0

def test1():
    global width_size
    width_size = i/width

def test2():
    global height_size 
    height_size = i/height

sum1 = 0
sum2 = 0
sum3 = 0
for file in os.listdir(fro_m):  #來源XML
    sum1 +=1
    if (os.path.splitext(fro_m + file)[-1]) == '.xml':  #判斷是否為xml檔
        sum2 += 1

        tree = ET.parse(fro_m + file)  #開啟xml檔
        root = tree.getroot()
        
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
                if (float(xmax)-float(xmin))< min_ judge (float(ymax)-float(ymin)) < min_:  #最小門檻
                    root.remove(node)#移除這個標籤
                

        tree.write(t_o + file)  #目的XML
        print(file)
        sum3 +=1
        
print('輸入總數',sum1)
print('輸入xml',sum2)
print('輸出xml',sum3)

