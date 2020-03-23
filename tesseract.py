from PIL import Image
import os



origin_path = 'C:/Users/KENNY_WU/Desktop/1234/H/'
new_path = 'C:/Users/KENNY_WU/Desktop/1234/H_/'   #用来存放处理好的图片

#从100张图片中提取出字符样本
for image in os.listdir(origin_path): 
    im = Image.open(origin_path+image)    
    width, height = im.size
    
    #获取图片中的颜色，返回列表[(counts, color)...]
    color_info = im.getcolors(width*height)
    #按照计数从大到小排列颜色，那么颜色计数最多的应该是背景，接下来排名2到6的则对应5个字符。
    sort_color = sorted(color_info, key=lambda x: x[0], reverse=True)    

    #根据颜色，提取出每一个字符，重新放置到一个新建的白色背景image对象上。每个image只放一个字符。
    char_dict = {}
    range1= range(50)
    im2 = Image.new('RGB', im.size, (255, 255, 255))
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if (im.getpixel((x, y)) == sort_color[1][1])|\
               (im.getpixel((x, y)) == sort_color[2][1])|\
               (im.getpixel((x, y)) == sort_color[3][1])|\
               (im.getpixel((x, y)) == sort_color[4][1])|\
               (im.getpixel((x, y)) == sort_color[5][1])|\
               (im.getpixel((x, y)) == sort_color[6][1])|\
               (im.getpixel((x, y)) == sort_color[7][1])|\
               (im.getpixel((x, y)) == sort_color[8][1])|\
               (im.getpixel((x, y)) == sort_color[9][1])|\
               (im.getpixel((x, y)) == sort_color[10][1])|\
               (im.getpixel((x, y)) == sort_color[11][1])|\
               (im.getpixel((x, y)) == sort_color[12][1])|\
               (im.getpixel((x, y)) == sort_color[13][1])|\
               (im.getpixel((x, y)) == sort_color[0][1])|\
               (im.getpixel((x, y)) == sort_color[15][1])|\
               (im.getpixel((x, y)) == sort_color[16][1])|\
               (im.getpixel((x, y)) == sort_color[17][1])|\
               (im.getpixel((x, y)) == sort_color[19][1])|\
               (im.getpixel((x, y)) == sort_color[18][1])|\
               (im.getpixel((x, y)) == sort_color[20][1])|\
               (im.getpixel((x, y)) == sort_color[21][1])|\
               (im.getpixel((x, y)) == sort_color[22][1])|\
               (im.getpixel((x, y)) == sort_color[23][1])|\
               (im.getpixel((x, y)) == sort_color[24][1])|\
               (im.getpixel((x, y)) == sort_color[25][1])|\
               (im.getpixel((x, y)) == sort_color[26][1])|\
               (im.getpixel((x, y)) == sort_color[27][1])|\
               (im.getpixel((x, y)) == sort_color[28][1])|\
               (im.getpixel((x, y)) == sort_color[29][1])|\
               (im.getpixel((x, y)) == sort_color[30][1])|\
               (im.getpixel((x, y)) == sort_color[31][1])|\
               (im.getpixel((x, y)) == sort_color[32][1])|\
               (im.getpixel((x, y)) == sort_color[61][1])|\
               (im.getpixel((x, y)) == sort_color[62][1])|\
               (im.getpixel((x, y)) == sort_color[63][1])|\
               (im.getpixel((x, y)) == sort_color[54][1])|\
               (im.getpixel((x, y)) == sort_color[64][1])|\
               (im.getpixel((x, y)) == sort_color[56][1])|\
               (im.getpixel((x, y)) == sort_color[57][1])|\
               (im.getpixel((x, y)) == sort_color[58][1])|\
               (im.getpixel((x, y)) == sort_color[59][1])|\
               (im.getpixel((x, y)) == sort_color[60][1])|\
               (im.getpixel((x, y)) == sort_color[51][1])|\
               (im.getpixel((x, y)) == sort_color[52][1])|\
               (im.getpixel((x, y)) == sort_color[53][1])|\
               (im.getpixel((x, y)) == sort_color[50][1])|\
               (im.getpixel((x, y)) == sort_color[55][1])|\
               (im.getpixel((x, y)) == sort_color[46][1])|\
               (im.getpixel((x, y)) == sort_color[47][1])|\
               (im.getpixel((x, y)) == sort_color[49][1])|\
               (im.getpixel((x, y)) == sort_color[48][1])|\
               (im.getpixel((x, y)) == sort_color[40][1])|\
               (im.getpixel((x, y)) == sort_color[41][1])|\
               (im.getpixel((x, y)) == sort_color[42][1])|\
               (im.getpixel((x, y)) == sort_color[43][1])|\
               (im.getpixel((x, y)) == sort_color[44][1])|\
               (im.getpixel((x, y)) == sort_color[45][1])|\
               (im.getpixel((x, y)) == sort_color[39][1])|\
               (im.getpixel((x, y)) == sort_color[37][1])|\
               (im.getpixel((x, y)) == sort_color[38][1])|\
               (im.getpixel((x, y)) == sort_color[36][1])|\
               (im.getpixel((x, y)) == sort_color[35][1])|\
               (im.getpixel((x, y)) == sort_color[34][1])|\
               (im.getpixel((x, y)) == sort_color[33][1])|\
               (im.getpixel((x, y)) == sort_color[21][1]):
                im2.putpixel((x, y), (255,255,255))
            else:
                im2.putpixel((x, y), (0,0,0))
    im2.save(new_path +'-'+ image.replace('jpg','tif'))  
    print('成功处理图片{}'.format(image))    


