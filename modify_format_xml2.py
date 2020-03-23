import os,shutil,math
import xml.etree.ElementTree as ET
from PIL import Image


fro_m = 'D:/Insight-MVT_Annotation_Train/DETRAC-Train-Annotations-XML/'#xml來源資料夾
t_o = 'D:/Insight-MVT_Annotation_Train/DETRAC-Train-Annotations-XML_/'#xml儲存資料夾

object_name = 'bus'

sum1,sum2,sum3 = 0,0,0
for file in os.listdir(fro_m):  #xml來源
    sum1 +=1
    if (os.path.splitext(fro_m + file)[-1]) == '.xml':  #判斷是否為xml檔
        sum2 +=1
        tree = ET.parse(fro_m + file)  #開啟xml檔
        root = tree.getroot()

        #這裡建立新資料夾

        for sequence in root.iter('sequence'):
            frame_name = root.get('name')

        os.mkdir(t_o + frame_name)

        for frame in root.iter('frame'):
            num=int(frame.get('num'))

            new_xml = ET.Element("annotation")  #創建節點

            folder = ET.SubElement(new_xml,'folder')
            folder.text = 'Insight-MVT_Annotation_Train'

            filename = ET.SubElement(new_xml,'filename')
            filename.text = 'img' + "%05d"%num + '.jpg'

            path = ET.SubElement(new_xml,'path')
            path.text = t_o + frame_name + filename.text

            source = ET.SubElement(new_xml,"source")

            database = ET.SubElement(source,'database')
            database.text = 'Unknown'

            size = ET.SubElement(new_xml,"size")

            width = ET.SubElement(size,'width')
            width.text = '960'

            height = ET.SubElement(size,'height')
            height.text = '540'

            depth = ET.SubElement(size,'depth')
            depth.text = '0'

            segmented = ET.SubElement(new_xml,"segmented")
            segmented.text = '0'

            for target in frame.iter('target'):

                objects = ET.SubElement(new_xml,'object')
                name = ET.SubElement(objects,'name')

                for attribute in target.iter('attribute'):
                    vehicle_type=attribute.get('vehicle_type')
                    name.text = vehicle_type

                pose = ET.SubElement(objects,'pose')
                pose.text = 'Unspecified'

                truncated = ET.SubElement(objects,'truncated')
                truncated.text = '0'

                difficult = ET.SubElement(objects,'difficult')
                difficult.text = '0'
                
                for box in target.iter('box'):

                    bndbox = ET.SubElement(objects,'bndbox')
                    
                    left=int(float(box.get('left')))
                    top=int(float(box.get('top')))
                    x_width=math.ceil(float(box.get('width')))
                    y_height=math.ceil(float(box.get('height')))
                    
                    xmin = ET.SubElement(bndbox,'xmin')
                    xmin.text = str(left)

                    xmax = ET.SubElement(bndbox,'xmax')
                    xmax.text = str(left+x_width)

                    ymin = ET.SubElement(bndbox,'ymin')
                    ymin.text = str(top)

                    ymax = ET.SubElement(bndbox,'ymax')
                    ymax.text = str(top+y_height)

            et =ET.ElementTree(new_xml) #生成文檔對象
            et.write(t_o + frame_name + '/' + (filename.text).split('.')[0] + '.xml') #生成xml文檔並指定字符集和
            print(frame_name + '/' + (filename.text).split('.')[0] + '.xml')
            sum3 += 1


print('xml資料夾數量',sum1)
print('xml輸入數量',sum2)
print('成功生成xml數量',sum3)


