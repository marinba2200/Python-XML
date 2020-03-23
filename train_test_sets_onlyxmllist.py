import os,shutil

#############會在目的資料夾中新增train與test資料夾

fro_m1 = 'C:/Users/KENNY_WU/Desktop/test2/'#xml來源資料夾
t_o1 = 'C:/Users/KENNY_WU/Desktop/12345/'#xml目的資料夾


i = 5   ##每五個檔即取四個進訓練集，一個進測試集




test = []
train = []

sum1,sum2,sum3,count = 0,0,0,0
for file1 in os.listdir(fro_m1):  #xml來源

    if (os.path.splitext(fro_m1 + file1)[-1]) == '.xml':  #判斷是否為xml檔
        sum1 += 1
        count += 1
        #################if count mod 5 == 0則將影像檔取出,並搜尋xml的相同名稱的檔案後取出，讓兩個都可以改名，並新建train與test資料夾,塞進去
        ###########在建立清單(通常train跟test 7:3)，move 跟copy方法都要
        if (count%i == 0):
            print('test-',file1.split('.')[0])
            test.append(file1.split('.')[0])
            sum2 += 1 
                            
        else:
            print('train-',file1.split('.')[0])
            train.append(file1.split('.')[0])
            sum3 += 1


fp3 = open(t_o1 + 'xml_train.txt','w')
print('正在寫入xml訓練集清單......')
for t3 in train:
    fp3.write(t3)
    fp3.write('\n')
fp3.close()


fp1 = open(t_o1 + 'xml_test.txt','w')
print('正在寫入xml測試集清單......')
for t1 in test:
    fp1.write(t1)
    fp1.write('\n')
fp1.close()



print('輸入xml總數:',sum1)
print('訓練集總數:',sum3)
print('測試集總數:',sum2)

