import os

fro_m = 'C:/Users/KENNY_WU/Desktop/photo/'  #檔案來源資料夾

sum1,sum2 = 0,0
f = open(fro_m + 'filename.txt','w')
for file in os.listdir(fro_m):
    sum1 += 1
    name = file.split('.')[0]
    f.write(name + '\n')
    print(name)
    sum2+=1

f.close()

print('資料夾檔案總數',sum1)
print('成功處理檔案總數',sum2)
