import os
import xml.etree.ElementTree as ET
from PIL import Image


fro_m1 = 'C:/Users/KENNY_WU/Desktop/test2/'#xml來源資料夾
fro_m2 = 'C:/Users/KENNY_WU/Desktop/photo/'#影像來源資料夾


sum1,sum2,sum3,sum6 = 0,0,0,0
sum4,sum5 = 0,0

for file1 in os.listdir(fro_m1):  #xml來源
    sum1 +=1
    if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔
        sum2 +=1
        
        tree = ET.parse(fro_m1 + file1)  #開啟xml檔
        root = tree.getroot()
        for file2 in os.listdir(fro_m2):  #影像來源
            sum4 +=1
            if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
                sum5 +=1
                if (file1.split('.')[0]) == (file2.split('.')[0]):

                    im = Image.open(fro_m2 + file2)
                    (a,b) = im.size
                        
                    for sizes in root.iter('width'):
                        width = int(sizes.text)  #獲取內容

                    for sizes in root.iter('height'):
                        height = int(sizes.text)  #獲取內容

                    if (a < width)|(b < height):
                        print(file2,'影像檔小於xml檔的設定:')
                        sum3 +=1

                    if (a > width)|(b > height):
                        print(file2,'影像檔大於xml檔的設定:')
                        sum6 +=1

print('xml資料夾檔案總數',sum1)
print('xml檔案數量',sum2)

print('影像資料夾檔案總數',sum4)
print('影像檔案數量',sum5)

print('影像檔小於xml檔設定數量',sum3)
print('影像檔大於xml檔設定數量',sum6)

                        

                    
                        





                    
