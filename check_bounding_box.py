import os
import xml.etree.ElementTree as ET
from PIL import Image


fro_m = 'C:/Users/KENNY_WU/Desktop/test2/'#來源XML

max_ = 300  #立即修改標籤的最大值
min_ = 0  #立即修改標籤的最小值

sum1,sum2,sum3,sum4 = 0,0,0,0

for file in os.listdir(fro_m):  #xml來源
    sum1 +=1
    if (os.path.splitext(fro_m + file)[-1]) == '.xml':  #判斷是否為xml檔
        sum2 +=1
        tree = ET.parse(fro_m + file)  #開啟xml檔
        root = tree.getroot()

        size = ('xmin','xmax','ymin','ymax')
        for clas in size:
        
            for node in root.iter(clas):
                xmin = node.text
                lenght =int(xmin)
                if (lenght > max_):
                    sum3 +=1
                                
                    while True:
                        print(file,'的',clas,'大於',max_)
                        i = input('是否立即修改Y/N:')
                        
                        if (i == 'Y')|(i == 'y')|(i == 'N')|(i == 'n'):
                            break
                                    
                        else:
                            print('輸入錯誤，請重新輸入。')
                                    
                    if (i == 'Y')|(i == 'y'):
                        node.text = str(max_)
                        sum4 +=1
                                    
                if (lenght < min_):
                    sum3 +=1
                                
                    while True:
                        print(file,'的',clas,'小於',min_)
                        i = input('是否立即修改Y/N:')
                        
                        if (i == 'Y')|(i == 'y')|(i == 'N')|(i == 'n'):
                            break
                                    
                        else:
                            print('輸入錯誤，請重新輸入。')
                                    
                    if (i == 'Y')|(i == 'y'):
                        node.text = str(min_)
                        sum4 +=1
                        
        tree.write(fro_m + file)  #目的XML          
                    
print('xml資料夾檔案總數',sum1)
print('xml檔案數量',sum2)
print('發現問題的標籤數量',sum3)
print('更改的標籤數量',sum4)

                    
