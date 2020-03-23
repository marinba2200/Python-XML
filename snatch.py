import os,shutil

fro_m2 = 'D:/Insight-MVT_Annotation_Train/Insight-MVT_Annotation_Train_crop/car/'#影像來源資料夾
t_o2 = "D:/Insight-MVT_Annotation_Train/Insight-MVT_Annotation_Train_crop/car'/"  #影像目的資料夾


list_set = []
for file2 in os.listdir(fro_m2):  #影像來源
    if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
        ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
        ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔

        filename = file2.split('.')[0]

        if len(list_set) >= 2:      #一組圖最後兩張移出
            if ('40171' not in (filename))|('40172' not in (filename)):
                if ((filename[0:18]) != (list_set[0][0:18])):
                    print('//////')
                    try:
                        shutil.move(fro_m2 + list_set[-2] + '.' + file2.split('.')[1] , t_o2 + list_set[-2] + '.' + file2.split('.')[1])
                    except FileNotFoundError as n:
                        pass
                    else:
                        print('3')
                        
                    try:
                        shutil.move(fro_m2 + list_set[-1] + '.' + file2.split('.')[1] , t_o2 + list_set[-1] + '.' + file2.split('.')[1])
                    except FileNotFoundError as n:
                        pass
                    else:
                        print('3')
                        list_set=[]
            

        if '40171' in (filename):   #含有40171的影像檔移出
            shutil.move(fro_m2 + file2 , t_o2 + file2)
            print('1')
        if '40172' in (filename):   #含有40172的影像檔移出
            shutil.move(fro_m2 + file2 , t_o2 + file2)
            print('1')

        if(filename[-3:] == '001')|(filename[-3:] == '002')|(filename[-3:] == '003'):   #名稱末端為001~003的影像檔移出
            try:
                shutil.move(fro_m2 + file2 , t_o2 + file2)
            except FileNotFoundError as n:
                pass
            else:
                print('2')


        list_set.append(filename)
        print(filename)
            

        
