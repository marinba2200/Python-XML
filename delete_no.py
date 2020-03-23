import os
import xml.etree.ElementTree as ET

fro_m = 'C:/Users/KENNY_WU/Desktop/test/'#來源XML
fro_m2 = 'C:/Users/KENNY_WU/Desktop/photo/'#影像來源資料夾
t_o = 'C:/Users/KENNY_WU/Desktop/test2/'#目的XML

has = ['car','moto','bus']  #要的類別(兩個以上):('moto','bus')or('car','moto','bus')


sum2,sum3,sum4 = 0,0,0
for file in os.listdir(fro_m):  #來源XML
    if (os.path.splitext(fro_m + file)[-1]) == '.xml':  #判斷是否為xml檔
        sum2 += 1
        jud,jud2 = 0,0
        tree = ET.parse(fro_m + file)  #開啟xml檔
        root = tree.getroot()
        sum5 = 0
        for file2 in os.listdir(fro_m2):  #影像來源
            if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
                sum5 +=1
                if (file.split('.')[0]) == (file2.split('.')[0]):
                    jud2 =+ 1
                    for node in root.findall('object'):
                        name = node.find('name').text

                        if name not in has:
                            root.remove(node)  #移除這個標籤
                            jud =+ 1
                            sum3 +=1
        if jud2 !=1:
            print(file,'缺少影像檔')

        elif jud != 0:
            sum4 +=1
            print('含被移除的標籤',file)

        else:
            tree.write(t_o + file)  #目的XML
        
print ('xml輸入數量',sum2)
print ('影像檔輸入數量',sum5)

print ('被移除標籤數',sum3)
print ('含被移除標籤之xml檔數',sum4)
