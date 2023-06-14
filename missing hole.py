import cv2
import os
import numpy as np

def_num =1
def XOR_operation(tem,test):
    
    global def_num
    test_image1=cv2.adaptiveThreshold(cv2.cvtColor(test,cv2.COLOR_BGR2GRAY),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,13,2)
    tem_image=cv2.adaptiveThreshold(cv2.cvtColor(tem,cv2.COLOR_BGR2GRAY),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,13,2)
    defect= cv2.bitwise_xor(test_image1,tem_image)
    defect=cv2.medianBlur(defect,5)
    kernel_open=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    defect=cv2.morphologyEx(defect,cv2.MORPH_OPEN,kernel_open)
    kernel_close=cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))
    defect=cv2.morphologyEx(defect,cv2.MORPH_CLOSE,kernel_close,iterations=1)
    Map=test_image.copy()
    Map[:,:,:]=0
    contours,hier=cv2.findContours(defect,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    x_c=[]
    y_c=[]
    
    for(index,contour) in  enumerate(contours):
        x, y, H, z = cv2.boundingRect(contours[index])
        Map[y-16:y+16,x-16:x+16]=255
        if(np.sum(Map[y-64:y+64,x-64:x+64:,:])==0):
          # print("i=",i,"cordinate=",y,x)
          # print("sum=",np.sum(Map[y-64:y+64,x-64:x+64]))
          filemame="C:\\Users\\User\\Desktop\\PCB_DATASET\\Defect_data\\missing_hole\\"+str(def_num)+".jpg"
          try:
               cv2.imwrite(filemame,test_image[y-128:y+128,x-128:x+128,:])
          except:
               pass
          x_c.append(x)
          y_c.append(y)
          def_num+=1
          
        #
template_path="C:\\Users\\User\\Desktop\\PCB_DATASET\\PCB_USED"
template_files=[]
template=[]
for  fileNames in os.walk(template_path):
    for name in fileNames[2]:
        template_files.append(template_path+"\\"+name)
for name in template_files:
    template.append(cv2.imread(name)) 
test_path="C:\\Users\\User\\Desktop\\PCB_DATASET\\images\\Missing_hole"

for image in os.walk(test_path):
    for names in image[2]:
        print(names[:2])
        test_image=cv2.imread(test_path+"\\"+names)
        if names[:2]=="01":
            XOR_operation(template[0],test_image)
        elif names[:2]=="04":
             XOR_operation(template[1],test_image)
        elif names[:2]=="05":
             XOR_operation(template[2],test_image)
        elif names[:2]=="06":
             XOR_operation(template[3],test_image)
        elif names[:2]=="07":
             XOR_operation(template[4],test_image)
        elif names[:2]=="08":
             XOR_operation(template[5],test_image)
        elif names[:2]=="09":
             XOR_operation(template[6],test_image)
        elif names[:2]=="10":
              XOR_operation(template[7],test_image)
        elif names[:2]=="11":
              XOR_operation(template[8],test_image)
        elif names[:2]=="12":
              XOR_operation(template[9],test_image)
            
