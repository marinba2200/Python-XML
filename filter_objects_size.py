import os
import xml.etree.ElementTree as ET
import math

fro_m = 'C:/Users/KENNY_WU/Desktop/test3/err/'#來源XML
t_o = 'C:/Users/KENNY_WU/Desktop/test2/'#目的XML

xmin_=10  #xml最小物件
ymin_=10

sum1 = 0
sum2 = 0
sum3 = 0
for file in os.listdir(fro_m):  
    sum1 +=1
    if (os.path.splitext(fro_m + file)[-1]) == '.xml':  
        sum2 += 1

        tree = ET.parse(fro_m + file) 
        root = tree.getroot()
                
            
        for node in root.findall('object'):
            for bndbox in node.findall('bndbox'):
                xmin = float(bndbox.find('xmin').text)
                xmax = float(bndbox.find('xmax').text)
                ymin = float(bndbox.find('ymin').text)
                ymax = float(bndbox.find('ymax').text)
                if ((float(xmax)-float(xmin))< xmin_) | ((float(ymax)-float(ymin)) < ymin_):  # | = or ; & = and ;
                    root.remove(node)
                    
        tree.write(t_o + file)  
        print(file)
        sum3 +=1
        
print('輸入總數',sum1)
print('輸入xml',sum2)
print('輸出xml',sum3)
