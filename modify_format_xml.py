import os,shutil,math
import xml.etree.ElementTree as ET
from PIL import Image

fro_m = 'C:/Users/KENNY_WU/Desktop/Casablanca/Annotations/'#xml來源資料夾
t_o = 'C:/Users/KENNY_WU/Desktop/Casablanca/Casablanca_/Annotations_/'#xml儲存資料夾

fro_m2 = 'C:/Users/KENNY_WU/Desktop/Casablanca/JPEGImages/'#影像來源資料夾

#add: path pose truncated difficult
#transform float into int or math.ceil
#check photo size

sum1,sum2,sum3 = 0,0,0

for file in os.listdir(fro_m):  #xml來源
    sum1 +=1
    if (os.path.splitext(fro_m + file)[-1]) == '.xml':  #判斷是否為xml檔
        sum2 +=1
        tree = ET.parse(fro_m + file)  #開啟xml檔
        root = tree.getroot()

        for file2 in os.listdir(fro_m2):  #影像來源

            if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔

                if (file.split('.')[0]) == (file2.split('.')[0]):
                    
                    im = Image.open(fro_m2 + file2)
                    (a,b) = im.size
                    
                    for width_ in root.iter('width'):
                        width = float(width_.text)
                        width_.text = str(a)

                    for height_ in root.iter('height'):
                        height = float(height_.text)
                        height_.text = str(b)

                    number = 0

                    for xmin in root.iter('xmin'):
                        number +=1      ###判斷是否為空檔案
                        xmin.text = str(int(float(xmin.text)*(a/width)-((a-width)/2)))
                        if float(xmin.text)<0:
                            xmin.text = '0'
               
                    for ymin in root.iter('ymin'):  
                        ymin.text = str(int(float(ymin.text)*(b/height)-((b-height)/2))) 
                        if float(ymin.text)<0:
                            ymin.text = '0'
                            
                    for xmax in root.iter('xmax'):  
                        xmax.text = str(math.ceil(float(xmax.text)*(a/width)+(a-width))) 
                        if float(xmax.text)>a:
                            xmax.text = str(a)
                            
                    for ymax in root.iter('ymax'):  
                        ymax.text = str(math.ceil(float(ymax.text)*(b/height)+(b-height)))
                        if float(ymax.text)>b:
                            ymax.text = str(b)

                    path = ET.SubElement(root,'path')
                    path.text = fro_m2 + file2

                    for objects in root.iter('object'):
                        
                        pose = ET.SubElement(objects,'pose')
                        pose.text = 'Unspecified'

                        truncated = ET.SubElement(objects,'truncated')
                        truncated.text = '0'

                        difficult = ET.SubElement(objects,'difficult')
                        difficult.text = '0'
                        
                    if number !=0 :
                        tree.write(t_o + file) #生成xml文檔並指定字符集和
                        print(file)
                        sum3 += 1



print('xml資料夾數量',sum1)
print('xml輸入數量',sum2)
print('xml輸出數量',sum3)

