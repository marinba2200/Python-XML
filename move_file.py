import os,shutil


fro_m1 = 'C:/Users/KENNY_WU/Desktop/test/'#xml來源資料夾
t_o1 = 'C:/Users/KENNY_WU/Desktop/test2/'#xml目的資料夾


fro_m2 = 'C:/Users/KENNY_WU/Desktop/photo/'#影像來源資料夾
t_o2 = 'C:/Users/KENNY_WU/Desktop/photo/123/'#影像目的資料夾



sum1,sum2,sum3,sum4,sum5,sum6 = 0,0,0,0,0,0
while True:
    print('1.取出有配對的xml與影像檔')
    print('2.取出無配對的xml與影像檔')
    k = input('請輸入需執行:')
    if (k == '1')|(k == '2'):
        break
                
    else:
        print('輸入錯誤，請重新輸入。')

print(' ')
if (k == '1'):

    for file1 in os.listdir(fro_m1):  #xml來源
        sum1 +=1
        if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔
            jud1=0
            sum2 +=1
            for file2 in os.listdir(fro_m2):  #影像來源
                
                if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較

                    if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                       ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                       ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
                        jud1 += 1
                        shutil.move(fro_m1 + file1 , t_o1 + file1)        #移动文件或重命名
                        shutil.move(fro_m2 + file2 , t_o2 + file2) 
                        
                        sum3 +=1
            if jud1 != 1:
                print('與',file1,'配對的影像檔 no found')
    print(' ')

    for file2 in os.listdir(fro_m2):  #影像來源
        sum4 +=1
        if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
           ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
           ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
            jud2=0
            sum5 +=1
            for file1 in os.listdir(fro_m1):  #xml來源

                if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較

                    if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔
                        jud2 += 1
                        sum6 +=1
            if jud2 != 1:
                print('與',file2,'配對的xml檔 no found')

if (k == '2'):

    for file1 in os.listdir(fro_m1):  #xml來源
        sum1 +=1
        if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔
            jud1=0
            sum2 +=1
            for file2 in os.listdir(fro_m2):  #影像來源
                
                if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較

                    if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
                       ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
                       ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
                        jud1 += 1

            if jud1 != 1:
                print('與',file1,'配對的影像檔 no found')
                shutil.move(fro_m1 + file1 , t_o1 + file1)
                sum3 +=1
    print(' ')

    for file2 in os.listdir(fro_m2):  #影像來源
        sum4 +=1
        if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
           ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
           ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
            jud2=0
            sum5 +=1
            for file1 in os.listdir(fro_m1):  #xml來源

                if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較

                    if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔
                        jud2 += 1

            if jud2 != 1:
                print('與',file2,'配對的xml檔 no found')
                shutil.move(fro_m2 + file2 , t_o2 + file2)
                sum6 +=1

print(' ')
print('xml資料夾檔案總數',sum1)
print('xml檔案總數',sum2)
print('xml移動總數',sum3)

print(' ')
print('影像資料夾檔案總數',sum4)
print('影像檔案總數',sum5)
print('影像移動總數',sum6)
