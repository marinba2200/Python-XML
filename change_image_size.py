import os
from PIL import Image

fro_m2 = 'C:/Users/KENNY_WU/Desktop/photo/'#影像來源資料夾
t_o2 = 'C:/Users/KENNY_WU/Desktop/photo/123/'#影像目的資料夾

sizes2 = 300  #縮小程度pixel

sum2_1,sum2_2,sum2_3 = 0,0,0

for file2 in os.listdir(fro_m2):
    sum2_1 += 1
    
    if ((os.path.splitext(fro_m2 + file2)[-1]) == '.png')|\
        ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpg')|\
        ((os.path.splitext(fro_m2 + file2)[-1]) == '.jpeg'):  #判斷是否為影像檔
        sum2_2 += 1
        im = Image.open(fro_m2 + file2)
        (a,b) = im.size
        
        if (a < sizes2)|(b < sizes2):
            
            while True:
                print(file2,'影像檔',a,'x',b,'小於',sizes2)
                i = input('是否覆蓋Y/N:')
                if (i == 'Y')|(i == 'y')|(i == 'N')|(i == 'n'):
                    break
                
                else:
                    print('輸入錯誤，請重新輸入。')
                    
            if (i == 'Y')|(i == 'y'):        
                im_ = im.resize( (sizes2,sizes2), Image.BILINEAR )
                im_.save(t_o2 + file2)
                print(file2,'縮放成功')
                sum2_3 += 1

            else:
                im_.save(t_o2 + file2)
                    
        else:
            im_ = im.resize( (sizes2,sizes2), Image.BILINEAR )
            im_.save(t_o2 + file2)
            print(file2,'縮放成功')
            sum2_3 += 1

print('資料夾檔案總數',sum2_1)
print('影像檔案總數',sum2_2)
print('完成縮小總數',sum2_3)
