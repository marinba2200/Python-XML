import os,shutil
import xml.etree.ElementTree as ET
import math
from PIL import Image

fro_m1 = 'C:/Users/KENNY_WU/Desktop/copy/copy/selectedXML_/'#來源XML
fro_m2 = 'C:/Users/KENNY_WU/Desktop/copy/copy/selectedJPG/'#影像來源資料夾
t_o = 'C:/Users/KENNY_WU/Desktop/copy/copy/crop/'  #影像目的資料夾

error_move = 'C:/Users/KENNY_WU/Desktop/copy/copy/error/'  #發現錯誤檔案時存放的資料夾

#### 錯誤檔案清單將存error.txt檔在error_move的資料夾中，若資料夾中已有error.txt則會清空並重新寫入 ####

ext = '.jpg'  #影像檔格式
qua = 100  #quality

sum1,sum2,sum4,sum5,sum6 = 0,0,0,0,0
error = []
error_count = 0
for file2 in os.listdir(fro_m2):  #影像來源
    sum4 += 1
for file1 in os.listdir(fro_m1):  #xml來源
    sum1 += 1
    if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔
        sum2 += 1
        tree = ET.parse(fro_m1 + file1)  #開啟xml檔
        root = tree.getroot()
        
        for file2 in os.listdir(fro_m2):  #影像來源
            if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較
                
                if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                   ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                   ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
                    sum5 += 1
                    img = Image.open(fro_m2 + file2)
                    name_count = 0
                    (a,b) = img.size
                    count = 0
                    print('正在處理',file1)
                    for node in root.findall('object'):
                        if (count == 0):
                            object_name = node.find('name').text#繼續找到name的標籤
                                
                            
                            name_count += 1 
                            for bndbox in node.findall('bndbox'):#繼續找到bndbox的標籤
                                xmin = int(bndbox.find('xmin').text)#繼續找到xmin的標籤
                                xmax = int(bndbox.find('xmax').text)#繼續找到xmin的標籤
                                ymin = int(bndbox.find('ymin').text)#繼續找到xmin的標籤
                                ymax = int(bndbox.find('ymax').text)#繼續找到xmin的標籤
                                

                                if os.path.isdir(t_o + object_name)!=True:
                                    os.mkdir(t_o + object_name)

                                if (xmin > xmax)or(ymin > ymax):#用or
                                    error.append(object_name + '/' + file1.split('.')[0] + '_' + str("%03d"%name_count) + ext + ' min 大於 max !')
                                    try:
                                        img2 = img.crop((min(xmin,xmax),min(ymin,ymax),max(xmin,xmax),max(ymin,ymax)))
                                    except EOFError as n:
                                        print(object_name,'/',file2,"EOFError")
                                        error.append(object_name + '/' + file2 + ':' + 'EOFError')
                                    else:
                                        img2.save(t_o + object_name + '/' + file2.split('.')[0] + '_' + str("%03d"%name_count) + ext , quality=qua)
                                        sum6 += 1
                                        print(object_name + '/' + file1.split('.')[0] + '_' + str("%03d"%name_count) + ext + ' min 大於 max !')
                                        img.close()
                                        shutil.move(fro_m1 + file1,error_move+file1)
                                        shutil.move(fro_m2 + file2,error_move+file2)
                                        count += 1
                                        error_count +=1
                                    

                                elif (xmin == xmax)or(ymin == ymax):#用or
                                    error.append(object_name + '/' + file1.split('.')[0] + '_' + str("%03d"%name_count) + ext + ' min 與 max 相等 !')
                                    img.close()
                                    shutil.move(fro_m1 + file1,error_move+file1)
                                    shutil.move(fro_m2 + file2,error_move+file2)
                                    print(object_name + '/' + file1.split('.')[0] + '_' + str("%03d"%name_count) + ext + ' min 與 max 相等 !')
                                    count += 1
                                    error_count +=1
                                  
                                else:
                                    try:
                                        img2 = img.crop((min(xmin,xmax),min(ymin,ymax),max(xmin,xmax),max(ymin,ymax)))       
                                    except EOFError as n:
                                        print(object_name,'/',file2,"EOFError")
                                        error.append(object_name + '/' + file2 + ':' + 'EOFError')
                                    else:
                                        img2.save(t_o + object_name + '/' + file2.split('.')[0] + '_' + str("%03d"%name_count) + ext , quality=qua)
                                        print(object_name + '/' + file2.split('.')[0] + '_' + str("%03d"%name_count) + ext)
                                        sum6 += 1      

                        else:
                            break
                        
                    #跳到最外圈迴圈，才能離開xml，再用continue

print('')
print('xml資料夾檔案總數',sum1)
print('xml檔案數量',sum2)
print('')
print('影像資料夾檔案總數',sum4)
print('影像檔案數量',sum5)
print('影像切割總數',sum6)
print('')
print('錯誤檔案共',error_count,'筆')
fp = open(error_move + 'ERROR.txt','w')

for tt in error:
    fp.write(tt)
    print(tt)

fp.write('\n')
fp.close()


fp2 = open(error_move + 'ERROR.txt','r')
tt2 = fp2.readline()


print('')
print('正在移動EOFError的影像檔與xml檔.......')
y = 0
for file1 in os.listdir(fro_m1):
    if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔
        for file2 in os.listdir(fro_m2):  #影像來源
            if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較
                
                if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                   ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                   ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
                    while tt2:
                        if 'EOFError' in tt2:
                            cut = tt2.index('.')
                            if file1.split('.')[0] == tt2[2:cut-4]:
                                print(file1.split('.')[0])
                                shutil.move(fro_m1 + file1,error_move+file1)
                                shutil.move(fro_m2 + file1.split('.')[0] + '.'  + file2.split('.')[1], error_move + file1.split('.')[0] + '.'  + file2.split('.')[1])
                        tt2 = fp2.readline()
                        y +=1
fp2.close()
print('移除完畢，請至error_move資料夾確認！')



