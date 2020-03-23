import os

fro_m1 = 'D:/labing/ch1_12/'  #影像來源資料夾
fro_m2= 'D:/labing/ch1_12/xml/'  #xml來源資料夾

sum1,sum2,sum3,sum4,sum5,sum6 = 0,0,0,0,0,0

for file1 in os.listdir(fro_m1):  #影像來源
    sum1 += 1
    if ((os.path.splitext(fro_m1 + file1)[-1]) == '.png')|\
       ((os.path.splitext(fro_m1 + file1)[-1]) == '.jpg')|\
       ((os.path.splitext(fro_m1 + file1)[-1]) == '.jpeg'):  #判斷是否為png檔
        jud1=0
        sum2 += 1
        
        for file2 in os.listdir(fro_m2):  #xml來源

            if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較

                if (os.path.splitext(fro_m2 + file2)[-1]) == '.xml':  #判斷是否為xml檔
                    jud1 += 1
                    break

        if jud1 != 1:
            print(file1,'的xml檔 no found')
        else:
            sum3 += 1
            
print ('影像資料夾總數',sum1)
print ('影像檔案數量',sum2)
print ('影像成功配對數',sum3)


for file2 in os.listdir(fro_m2):  #xml來源
    sum4 += 1
    if (os.path.splitext(fro_m2 + file2)[-1]) == '.xml':  #判斷是否為xml檔
        jud2=0
        sum5 += 1
        for file1 in os.listdir(fro_m1):  #影像來源
            
            if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較

                if ((os.path.splitext(fro_m1 + file1)[-1]) == '.png')|\
                   ((os.path.splitext(fro_m1 + file1)[-1]) == '.jpg')|\
                   ((os.path.splitext(fro_m1 + file1)[-1]) == '.jpeg'):  #判斷是否為png檔
                    jud2 += 1
                    break

        if jud2 != 1:
            print(file2,'的影像檔 no found')
        else:
            sum6 += 1

print ('xml資料夾總數',sum4)
print ('xml檔案數量',sum5)
print ('xml成功配對數',sum6)
