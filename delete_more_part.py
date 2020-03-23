import os,shutil,math
import xml.etree.ElementTree as ET
from PIL import Image

fro_m = 'C:/Users/KENNY_WU/Desktop/test/'#來源XML
t_o = 'C:/Users/KENNY_WU/Desktop/test3/'#目的XML

fro_m2 = 'C:/Users/KENNY_WU/Desktop/photo/'#影像來源資料夾
t_o2 = 'C:/Users/KENNY_WU/Desktop/photo/crop/'#影像目的資料夾


n = ''  #檔名前增加字串 : n + 原檔名(空白即為原檔名)
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
    sum1 += 1
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

                    ##開啟影像檔，讀取xml物件中xmin與xmax的最大最小值，並使用crop函數裁切影像
                    ##高度不便，寬度裁切為max與min +-10，並儲存影像檔
                    ##xml檔寬高做修正
                    im = Image.open(fro_m2 + file2)
                    (a,b) = im.size
                    listmax = []
                    listmin = []
                    
                    for xmax in root.iter('xmax'):
                        xmaxs = int(xmax.text)  #獲取內容
                        listmax.append(xmaxs)

                    for xmin in root.iter('xmin'):
                        xmins = int(xmin.text)  #獲取內容
                        listmin.append(xmins)

                    maxs = max(listmax)
                    mins = min(listmin)

                    im_crop = im.crop((mins-10,0,maxs+10,b))
                    
                    if (k == '1'):
                        im_crop.save(t_o2 + n + file2 , quality=qua)
                        print(file2)
                        sum3 += 1
                        
                    elif (k == '2'):
                        im_crop.save(t_o2 + n + file2.split('.')[0] + ext , quality=qua)
                        for names in root.iter('filename'):
                            filename = names.text  #獲取內容
                            new_names = n + file2.split('.')[0]  + ext  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                            names.text = new_names   #修改內容
                        for paths in root.iter('path'):
                            path = paths.text  #獲取內容
                            new_paths = t_o + n + file2.split('.')[0]  + ext  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                            paths.text = new_paths   #修改內容
                        print(file2)
                        sum3 += 1

                    (a1,b1) = im_crop.size

                    for width in root.iter('width'):
                        
                        width.text = str(a1)
                        
                    for height in root.iter('height'):
                        height.text = str(b1)

                    for xmax in root.iter('xmax'):
                        xmaxs = int(xmax.text)  #獲取內容
                        xmax.text = str(xmaxs-(mins-10))

                    for xmin in root.iter('xmin'):
                        xmins = int(xmin.text)  #獲取內容
                        xmin.text = str(xmins-(mins-10))
                    

                    tree.write(t_o + n + file)  #目的XML
                    print(file)
                    sum6 += 1

print('xml資料夾檔案總數',sum1)
print('輸入xml',sum2)
print('輸出xml',sum6)

print('影像資料夾檔案總數',sum4)
print('輸入影像',sum5)
print('輸出影像',sum3)

                    


                    

                    
                    
                    
