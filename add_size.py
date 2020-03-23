import os
import xml.etree.ElementTree as ET
import math

fro_m = 'C:/Users/KENNY_WU/Desktop/test/'#來源XML
t_o = 'C:/Users/KENNY_WU/Desktop/test3/'#目的XML



xmin_offset = 0  #xml物件增加數值(放大為- 縮小為+)
ymin_offset = 0  #xml物件增加數值(放大為- 縮小為+)
xmax_offset = 0  #xml物件增加數值(放大為+ 縮小為-)
ymax_offset = 0  #xml物件增加數值(放大為+ 縮小為-)
ext = '.png'

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
            width = int(float(sizes.text))  #獲取內容
        
        for sizes in root.iter('height'):
            height = int(float(sizes.text))  #獲取內容

        
        for name in root.iter('filename'):
            filename = name.text
            if filename.find('.') == (-1):
                name.text = filename + ext
            
        for node in root.iter('xmin'):  #修改xmin框框大小(無條件捨去)
            xmin = node.text  #獲取內容
            new_size = str(int(float(xmin)+xmin_offset))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
            if  int(new_size) < 0:
                node.text = '1'
            elif int(new_size) > width:
                node.text = str(width-1)
            else:
                node.text = str(int(new_size)+1)  #修改內容
                        
        for node in root.iter('ymin'):  #修改xmin框框大小(無條件捨去)
            ymin = node.text  #獲取內容
            new_size = str(int(float(ymin)+ymin_offset))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
            if int(new_size) < 0:
                node.text = '1'
            elif int(new_size) > height:
                node.text = str(height-1)
            else:
                node.text = str(int(new_size)+1)  #修改內容
                
        for node in root.iter('xmax'):
            xmax = node.text  #獲取內容
            new_size = str(math.ceil(float(xmax)+xmax_offset))  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
            if int(new_size) > width:
                node.text = str(width-1)
            elif  int(new_size) < 0:
                node.text = '1'
            else:
                node.text = str(int(new_size)-1)  #修改內容
                
        for node in root.iter('ymax'):
            ymax = node.text  #獲取內容
            new_size = str(math.ceil(float(ymax)+ymax_offset))  #調整大小:節點資料為字串，先轉換成整數型態做修改後再轉換回字串
            if int(new_size) > height:
                node.text = str(height-1)
            elif  int(new_size) < 0:
                node.text = '1'
            else:
                node.text = str(int(new_size)-1)  #修改內容
                

        tree.write(t_o + file)  #目的XML
        print(file)
        sum3 +=1
        
print('輸入總數',sum1)
print('輸入xml',sum2)
print('輸出xml',sum3)




