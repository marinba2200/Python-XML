import os
import xml.etree.ElementTree as ET
from PIL import Image

fro_m = 'D:/labing/kau/ch3/xml/'#來源XML
t_o = 'D:/labing/kau/ch3/test/xml/'#目的XML

fro_m2 = 'D:/labing/kau/ch3/'#影像來源資料夾
t_o2 = 'D:/labing/kau/ch3/test/photo/'#影像目的資料夾


n = 'f'  #檔名前增加字串 : n + 原檔名
ext = '.jpg'  #影像檔格式
qua = 100  #quality

while True:
    print('1.影像檔格式不變更')
    print('2.影像檔格式改為自行設定之格式')
    k = input('請輸入需執行:')
    if (k == '1')|(k == '2'):
        break
                
    else:
        print('輸入錯誤，請重新輸入。')

sum1,sum2,sum3,sum6 = 0,0,0,0
for file in os.listdir(fro_m):  #來源XML
    sum1 =+ 1
    if (os.path.splitext(fro_m + file)[-1]) == '.xml':  #判斷是否為xml檔
        sum2 += 1
        tree = ET.parse(fro_m + file)  #開啟xml檔
        root = tree.getroot()
        sum4,sum5 = 0,0
        for file2 in os.listdir(fro_m2):  #影像來源
            sum4 += 1
            if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
                sum5 += 1
                if (file.split('.')[0]) == (file2.split('.')[0]):
                    im = Image.open(fro_m2 + file2)
                    flip = im.transpose(Image.FLIP_LEFT_RIGHT)
                    if (k == '1'):
                        flip.save(t_o2 + n + file2.split('.')[0] + '.' + file2.split('.')[1] , quality=qua)
                                
                        for names in root.iter('filename'):
                            filename = names.text  #獲取內容
                            new_names = n + file.split('.')[0]+ '.' + file2.split('.')[1]  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                            names.text = new_names   #修改內容
                        for paths in root.iter('path'):
                            path = paths.text  #獲取內容
                            new_paths = t_o + n + file.split('.')[0] + '.' + file2.split('.')[1]  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                            paths.text = new_paths   #修改內容
                        print(file2)
                        sum6 += 1

                    if (k == '2'):
                        flip.save(t_o2 + n + file2.split('.')[0] + ext , quality=qua)

                        for names in root.iter('filename'):
                            filename = names.text  #獲取內容
                            new_names = n + file.split('.')[0]  + ext  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                            names.text = new_names   #修改內容
                        for paths in root.iter('path'):
                            path = paths.text  #獲取內容
                            new_paths = t_o + n + file.split('.')[0]  + ext  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                            paths.text = new_paths   #修改內容
                        print(file2)
                        sum6 += 1

                    for sizes in root.iter('width'):
                        width = int(sizes.text)  #獲取內容
                            
                    for node in root.findall('object'):
                        for bndbox in node.findall('bndbox'):#繼續找到bndbox的標籤
                            for x_min in bndbox.findall('xmin'):
                                xmin = int(x_min.text)
                            for x_max in bndbox.findall('xmax'):
                                xmax = int(x_max.text)
                                
                            new_xmin = width - xmax
                            new_xmax = width - xmin

                            if (new_xmax > width):
                                new_xmax = width
                            if (new_xmin < 0):
                                new_xmin = 0


                            
                            x_min.text = str(new_xmin)
                            x_max.text = str(new_xmax)
                            
                    tree.write(t_o + n + file.split('.')[0]  + '.' + file.split('.')[1])  #目的XML
                    print(file)
                    sum3 += 1

               
print('xml資料夾檔案總數',sum1)
print('輸入xml',sum2)
print('輸出xml',sum3)

print('影像資料夾檔案總數',sum4)
print('輸入影像',sum5)
print('輸出影像',sum6)
