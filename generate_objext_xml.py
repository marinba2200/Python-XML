import os,shutil
import xml.etree.ElementTree as ET
from PIL import Image


fro_m = 'D:/Insight-MVT_Annotation_Train/Insight-MVT_Annotation_Train_crop/car/'#影像來源資料夾
t_o = 'D:/Insight-MVT_Annotation_Train/Insight-MVT_Annotation_Train_crop/car_xml/'#xml儲存資料夾

object_name = 'car' #物件名稱

sum1,sum2,sum3 = 0,0,0
for file in os.listdir(fro_m):  #影像來源
    sum1 += 1
    if ((os.path.splitext(fro_m + file)[-1]) == '.png')|\
        ((os.path.splitext(fro_m + file)[-1]) == '.jpg')|\
        ((os.path.splitext(fro_m + file)[-1]) == '.jpeg'):  #判斷是否為影像檔
        sum2 += 1
        #新建一個xml檔
        #內容(讀取影像大小、來源資料夾+檔名[附檔名為xml]、物件名稱)
        #儲存xml檔
        im = Image.open(fro_m + file)
        (a,b) = im.size
        
        new_xml = ET.Element("annotation")  #創建節點

        folder = ET.SubElement(new_xml,'folder')
        folder.text = 'Insight-MVT_Annotation_Train'  ############################需要改

        filename = ET.SubElement(new_xml,'filename')
        filename.text = file

        path = ET.SubElement(new_xml,'path')
        path.text = fro_m + file


        source = ET.SubElement(new_xml,"source")

        database = ET.SubElement(source,'database')
        database.text = 'Unknown'


        size = ET.SubElement(new_xml,"size")

        width = ET.SubElement(size,'width')
        width.text = str(a)

        height = ET.SubElement(size,'height')
        height.text = str(b)

        depth = ET.SubElement(size,'depth')
        depth.text = '3'

    
        segmented = ET.SubElement(new_xml,"segmented")
        segmented.text = '0'


        objects = ET.SubElement(new_xml,"object")

        name = ET.SubElement(objects,'name')
        name.text = object_name

        pose = ET.SubElement(objects,'pose')
        pose.text = 'Unspecified'

        truncated = ET.SubElement(objects,'truncated')
        truncated.text = '0'

        difficult = ET.SubElement(objects,'difficult')
        difficult.text = '0'
        

        bndbox = ET.SubElement(objects,'bndbox')

        xmin = ET.SubElement(bndbox,'xmin')
        xmin.text = '0'

        ymin = ET.SubElement(bndbox,'ymin')
        ymin.text = '0'

        xmax = ET.SubElement(bndbox,'xmax')
        xmax.text = str(a)

        ymax = ET.SubElement(bndbox,'ymax')
        ymax.text = str(b)

        
        et =ET.ElementTree(new_xml) #生成文檔對象
        et.write(t_o + file.split('.')[0] + '.xml') #生成xml文檔並指定字符集和
        print(file)
        sum3 += 1


print('影像資料夾數量',sum1)
print('影像輸入數量',sum2)
print('成功生成xml數量',sum3)

