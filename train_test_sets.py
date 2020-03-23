import os,shutil

#############會在目的資料夾中新增train與test資料夾

fro_m1 = 'C:/Users/KENNY_WU/Desktop/test2/'#xml來源資料夾
t_o1 = 'C:/Users/KENNY_WU/Desktop/12345/xml/'#xml目的資料夾

fro_m2 = 'C:/Users/KENNY_WU/Desktop/kau_taichung/'#影像來源資料夾
t_o2 = 'C:/Users/KENNY_WU/Desktop/12345/photo/'#影像目的資料夾

i = 5   ##每五個檔即取四個進訓練集，一個進測試集





while True:
    print('1.僅產生xml與影像清單')
    print('2.複製xml與影像檔案')
    print('3.移動xml與影像檔案')
    k = input('請輸入需執行:')
    if (k == '1')|(k == '2')|(k == '3'):
        break
                
    else:
        print('輸入錯誤，請重新輸入。')
test1 = []
test2 = []
train1 = []
train2 = []

if (k == '1'):
    count = 0
    sum1,sum2,sum3 = 0,0,0
    for file2 in os.listdir(fro_m2):  #影像來源

        if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
            ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
            ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
            sum1 += 1
            for file1 in os.listdir(fro_m1):  #xml來源
                
                if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較

                    if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔

                        count += 1
                        #################if count mod 5 == 0則將影像檔取出,並搜尋xml的相同名稱的檔案後取出，讓兩個都可以改名，並新建train與test資料夾,塞進去
                        ###########在建立清單(通常train跟test 7:3)，move 跟copy方法都要
                        if (count%i == 0):
                            print('test-',file1)
                            test1.append(file1)
                            print('test-',file2)
                            test2.append(file2)
                            sum2 += 1 
                            
                        else:
                            print('train-',file1)
                            train1.append(file1)
                            print('train-',file2)
                            train2.append(file2)
                            sum3 += 1

if (k == '2')|(k == '3'):
                        
    if os.path.isdir(t_o1 + 'train')!=True:
        os.mkdir(t_o1 + 'train')
    if os.path.isdir(t_o1 + 'test')!=True:
        os.mkdir(t_o1 + 'test')
    if os.path.isdir(t_o2 + 'train')!=True:
        os.mkdir(t_o2 + 'train')
    if os.path.isdir(t_o2 + 'test')!=True:
        os.mkdir(t_o2 + 'test')
    count = 0
    sum1,sum2,sum3 = 0,0,0
    for file2 in os.listdir(fro_m2):  #影像來源

        if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
            ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
            ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
            sum1 += 1
            for file1 in os.listdir(fro_m1):  #xml來源
                
                if (file1.split('.')[0]) == (file2.split('.')[0]):   #分割檔名與副檔名並比較

                    if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔

                        count += 1
                        #################if count mod 5 == 0則將影像檔取出,並搜尋xml的相同名稱的檔案後取出，讓兩個都可以改名，並新建train與test資料夾,塞進去
                        ###########在建立清單(通常train跟test 7:3)，move 跟copy方法都要
                        if (count%i == 0):
                            if (k == '2'):
                                shutil.copy(fro_m1 + file1 , t_o1 + 'test/' + file1)  #移动文件或重命名
                                print('test-',file1)
                                test1.append(file1)
                                shutil.copy(fro_m2 + file2 , t_o2 + 'test/' + file2)  #移动文件或重命名
                                print('test-',file2)
                                test2.append(file2)
                                sum2 += 1
                            if (k == '3'):
                                shutil.move(fro_m1 + file1 , t_o1 + 'test/' + file1)  #移动文件或重命名
                                print('test-',file1)
                                test1.append(file1)
                                shutil.move(fro_m2 + file2 , t_o2 + 'test/' + file2)  #移动文件或重命名
                                print('test-',file2)
                                test2.append(file2)
                                sum2 += 1
                            
                        else:
                            if (k == '2'):
                                shutil.copy(fro_m1 + file1 , t_o1 + 'train/' + file1)  #移动文件或重命名
                                print('train-',file1)
                                train1.append(file1)
                                shutil.copy(fro_m2 + file2 , t_o2 + 'train/' + file2)  #移动文件或重命名
                                print('train-',file2)
                                train2.append(file2)
                                sum3 += 1
                            if (k == '3'):
                                shutil.move(fro_m1 + file1 , t_o1 + 'train/' + file1)  #移动文件或重命名
                                print('train-',file1)
                                train1.append(file1)
                                shutil.move(fro_m2 + file2 , t_o2 + 'train/' + file2)  #移动文件或重命名
                                print('train-',file2)
                                train2.append(file2)
                                sum3 += 1

fp3 = open(t_o1 + 'xml_train.txt','w')
print('正在寫入xml訓練集清單......')
for t3 in train1:
    fp3.write(t3)
    fp3.write('\n')
fp3.close()

fp4 = open(t_o2 + 'photo_train.txt','w')
print('正在寫入影像訓練集清單......')
for t4 in train2:
    fp4.write(t4)
    fp4.write('\n')
fp4.close()

fp1 = open(t_o1 + 'xml_test.txt','w')
print('正在寫入xml測試集清單......')
for t1 in test1:
    fp1.write(t1)
    fp1.write('\n')
fp1.close()

fp2 = open(t_o2 + 'photo_test.txt','w')
print('正在寫入影像測試集清單......')
for t2 in test2:
    fp2.write(t2)
    fp2.write('\n')
fp2.close()



print('輸入影像總數:',sum1)
print('輸入xml總數:',sum2 + sum3)
print('訓練集總數:',sum3)
print('測試集總數:',sum2)



