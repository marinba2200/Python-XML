import os,shutil


fro_m1 = 'D:/Insight-MVT_Annotation_Train/Insight-MVT_Annotation_Train_/DETRAC-Train-Annotations-XML/DETRAC-Train-Annotations-XML/'#xml來源資料夾
t_o1 = "D:/Insight-MVT_Annotation_Train/Insight-MVT_Annotation_Train_crop/car_bigxml/"#xml目的資料夾


fro_m2 = "D:/Insight-MVT_Annotation_Train/Insight-MVT_Annotation_Train_crop/car_bigphoto/" #影像來源資料夾



sum1,sum2,sum3,sum4,sum5,sum6 = 0,0,0,0,0,0
while True:
    print('1.移動xml檔')
    print('2.複製的xml檔')
    m = input('請輸入需執行:')
    if (m == '1')|(m == '2'):
        while True:
            print('1.取出有配對的xml檔')
            print('2.取出無配對的xml檔')
            k = input('請輸入需執行:')
            if (k == '1')|(k == '2'):
                break
                        
            else:
                print('輸入錯誤，請重新輸入。')
        break
                
    else:
        print('輸入錯誤，請重新輸入。')
    
if (m == '1'):
    print(' ')
    if (k == '1'):
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
                            shutil.move(fro_m1 + file1 , t_o1 + file1)        #移动文件或重命名
                            jud2 += 1
                            sum3 +=1
                            print('.')
                if jud2 != 1:
                    print('與',file2,'配對的xml檔 no found')

    if (k == '2'):
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
                            print('.')

                if jud2 != 1:
                    print('與',file2,'配對的xml檔 no found')
                    shutil.move(fro_m1 + file1 , t_o1 + file1)
                    sum3 +=1
if (m == '2'):
    print(' ')
    if (k == '1'):
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
                            shutil.copy(fro_m1 + file1 , t_o1 + file1)        #移动文件或重命名
                            jud2 += 1
                            sum3 +=1
                            print('.')
                if jud2 != 1:
                    print('與',file2,'配對的xml檔 no found')

    if (k == '2'):
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
                            print('.')

                if jud2 != 1:
                    print('與',file2,'配對的xml檔 no found')
                    shutil.copy(fro_m1 + file1 , t_o1 + file1)
                    sum3 +=1


print(' ')
print('xml資料夾檔案總數',sum1)
print('xml檔案總數',sum2)
print('xml處理總數',sum3)

print(' ')
print('影像資料夾檔案總數',sum4)
print('影像檔案總數',sum5)
