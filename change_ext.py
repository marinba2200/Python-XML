import os,shutil
import xml.etree.ElementTree as ET


fro_m = 'D:/Insight-MVT_Annotation_Train/Insight-MVT_Annotation_Train_/DETRAC-Train-Annotations-XML/' #來源XML
t_o = 'D:/Insight-MVT_Annotation_Train/Insight-MVT_Annotation_Train_/DETRAC-Train-Annotations-XML/DETRAC-Train-Annotations-XML/' #目的XML
ext = '.jpg'

sum1 = 0
sum2 = 0
sum3 = 0
for file in os.listdir(fro_m):  #來源XML
    sum1 +=1
    if (os.path.splitext(fro_m + file)[-1]) == '.xml':  #判斷是否為xml檔
        sum2 += 1

        tree = ET.parse(fro_m + file)  #開啟xml檔
        root = tree.getroot()

        
        for name in root.iter('filename'):
            filename = name.text
            if filename.find('.') == (-1):
                name.text = filename + ext
            else:
                name.text = filename.split('.')[0]+ ext
            

        tree.write(t_o + file)  #目的XML
        print(file)
        sum3 +=1
        
print('輸入總數',sum1)
print('輸入xml',sum2)
print('輸出xml',sum3)




