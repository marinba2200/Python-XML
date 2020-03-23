#讀檔
#讀取物件名稱
#判斷若物件名稱==van則更改物件名稱為car
#判斷若物件名稱==others則更改物件名稱為truck

import os,shutil
import xml.etree.ElementTree as ET

fro_m = 'C:/Users/KENNY_WU/Desktop/copy/copy/selectedXML/'#xml來源資料夾
t_o = 'C:/Users/KENNY_WU/Desktop/copy/copy/selectedXML_/'#xml儲存資料夾

object_name1 = 'man'
object_name2 = ''

needless_name1 = 'person'
needless_name2 = ''


sum1 = 0
sum2 = 0
sum3 = 0
for file in os.listdir(fro_m):  #來源XML
    sum1 +=1
    if (os.path.splitext(fro_m + file)[-1]) == '.xml':  #判斷是否為xml檔
        sum2 += 1

        tree = ET.parse(fro_m + file)  #開啟xml檔
        root = tree.getroot()

        for name in root.iter('name'):
            new_name = name.text  #獲取內容
            if new_name == needless_name1:
                name.text = object_name1
            elif new_name == needless_name2:
                name.text = object_name2

        tree.write(t_o + file)  #目的XML
        print(file)
        sum3 +=1
        
print('輸入總數',sum1)
print('輸入xml',sum2)
print('輸出xml',sum3)


