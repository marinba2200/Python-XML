import os
import xml.etree.ElementTree as ET
import logging
from PIL import Image

fro_m = 'C:/Users/KENNY_WU/Desktop/test/'#來源XML
fro_m2 = 'C:/Users/KENNY_WU/Desktop/photo/'#來源影像

t_o = 'C:/Users/KENNY_WU/Desktop/test2/'#目的XML

#### 錯誤檔案清單將存error.txt檔在XML的目的資料夾中，若資料夾中已有error.txt則會清空並重新寫入 ####
error = []

sum1,sum2,sum3,sum4 = 0,0,0,0

for file in os.listdir(fro_m):  #xml來源

        
        sum1 +=1
        if (os.path.splitext(fro_m + file)[-1]) == '.xml':  #判斷是否為xml檔
            sum2 +=1
            for file2 in os.listdir(fro_m2):  #影像來源   ##########################################################
            
                    if (file.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較

                        if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                           ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                           ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔

                            img = Image.open(fro_m2 + file2)
                            (a,b) = img.size
                            
                            tree = ET.parse(fro_m + file)  #開啟xml檔
                            root = tree.getroot()
                            for sizes1 in root.iter('width'):
                                max_1 = int(float(sizes1.text))  #獲取內容

                            for sizes2 in root.iter('height'):
                                max_2 = int(float(sizes2.text))  #獲取內容

                            if (a != max_1)|(b != max_2):
                                error.append(file)
                                max_1 = a
                                max_2 = b
                                size1.text = str(a)
                                size2.text = str(b)
                                sum3 += 1        #########################################################1/23新增

                            min_ = 0

                            for node in root.iter('xmax'):
                                xmax = node.text
                                lenght = int(float(xmax))
                                if (lenght >= max_1):
                                        error.append(file)
                                        sum3 += 1
                                        node.text = str(max_1-1)
                                        sum4 +=1
                                
                            for node in root.iter('ymax'):
                                ymax = node.text
                                lenght = int(float(ymax))
                                if (lenght >= max_2):
                                        error.append(file)
                                        sum3 +=1
                                        node.text = str(max_2-1)
                                        sum4 +=1

                    
                            size = ('xmin','ymin')
                            for clas in size:
                                for node in root.iter(clas):
                                    xmin = node.text
                                    lenght = float(xmin)
                                                        
                                    if (lenght <= min_):
                                        error.append(file)
                                        sum3 +=1
                                        node.text = str(min_ +1 )
                                        sum4 += 1

                            print(file,'已處理完畢')    
                            tree.write(t_o + file)  #目的XML

                    
print('xml資料夾檔案總數',sum1)
print('xml檔案數量',sum2)
print('發現問題的標籤數量',sum3)
print('更改的標籤數量',sum4)

fp = open(t_o  + 'error.txt','w')
for tt in error:
    fp.write(tt)
    print(tt)
    fp.write('\n')
fp.close()


fp2 = open(t_o  + 'error.txt','r')
tt2 = fp2.readline()
fp2.close()
