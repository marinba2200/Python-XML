import os,shutil
import xml.etree.ElementTree as ET



fro_m1 = 'C:/Users/KENNY_WU/Desktop/test/'  #xml來源資料夾
t_o1 = 'C:/Users/KENNY_WU/Desktop/test3/'#xml目的資料夾


fro_m2 = 'C:/Users/KENNY_WU/Desktop/photo/'#影像來源資料夾
t_o2 = 'C:/Users/KENNY_WU/Desktop/photo/123/'#影像目的資料夾


change = '_'  #檔名新增字串
old = ''  #檔名中不要的字串 S.replace(old, new, [count])
new = ''  #要替換的字串

sum1,sum2,sum3,sum4,sum5,sum6 = 0,0,0,0,0,0

for file1 in os.listdir(fro_m1):  #xml來源
    sum1 +=1
    if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔
        tree = ET.parse(fro_m1 + file1)  #開啟xml檔
        root = tree.getroot()
        sum2 +=1
        jud1=0
        for file2 in os.listdir(fro_m2):  #影像來源
            
            if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較

                if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                   ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                   ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
                    jud1 += 1
                    if (os.path.isfile(t_o1 + change + file1.replace(old, new,1))):

                        while True:                            
                            print('有重複檔名:',change + file1.replace(old, new,1))
                            i = input('是否覆蓋Y/N:')
                            if (i == 'Y')|(i == 'y')|(i == 'N')|(i == 'n'):
                                break
                            else:
                                print('輸入錯誤，請重新輸入。')

                        if (i == 'Y')|(i == 'y'):
                            for names in root.iter('filename'):
                                filename = names.text  #獲取內容
                                new_names = change + file2.replace(old, new,1)  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                                names.text = new_names   #修改內容
                            sum3 +=1

                    else:
                        for names in root.iter('filename'):
                            filename = names.text  #獲取內容
                            new_names = change + file2.replace(old, new,1)  #調整大小:節點資列為字串，先轉換成整數型態做修改後再轉換回字串
                            names.text = new_names   #修改內容
                        sum3 +=1
                    if (os.path.isfile(t_o2 + change + file2.replace(old, new,1))):
                        print('有重複檔名:',change + file2.replace(old, new,1))
                        i = input('是否覆蓋Y/N:')

                        if (i == 'Y')|(i == 'y'):
                            shutil.copyfile(fro_m2 +file2,t_o2 +change+file2.replace(old, new,1))  #替換次數預設1
                            sum6 +=1

                    else:
                        shutil.copyfile(fro_m2 +file2,t_o2 +change+file2.replace(old, new,1))  #替換次數預設1
                        sum6 +=1
                    tree.write(t_o1 + change + file1.replace(old, new,1))  #目的XML
                    print(sum3)  ###顯示處理中的數量
        if jud1 != 1:
            print(file1,'的影像檔 no found')


for file2 in os.listdir(fro_m2):  #影像來源
    sum4 +=1
    if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
       ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
       ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
        sum5 +=1
        jud2=0
        for file1 in os.listdir(fro_m1):  #xml來源

            if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較

                if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔
                    jud2 += 1
                    

        if jud2 != 1:
            print(file2,'的xml檔 no found')


print('xml資料夾檔案總數',sum1)
print('xml檔案數量',sum2)
print('xml成功改名檔案',sum3)

print('影像資料夾檔案總數',sum4)
print('影像檔案數量',sum5)
print('影像成功改名檔案',sum6)
