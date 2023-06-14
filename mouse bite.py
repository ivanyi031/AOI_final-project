import cv2
import os
import numpy as np

def_num =1
def XOR_operation(tem,test):
    global def_num
    test_image1=cv2.adaptiveThreshold(cv2.cvtColor(test,cv2.COLOR_BGR2GRAY),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,13,2)
    tem_image=cv2.adaptiveThreshold(cv2.cvtColor(tem,cv2.COLOR_BGR2GRAY),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,13,2)
    defect= cv2.bitwise_xor(test_image1,tem_image)
    defect=cv2.medianBlur(defect,11)
    kernel_open=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    defect=cv2.morphologyEx(defect,cv2.MORPH_OPEN,kernel_open,iterations=1)
    kernel_close=cv2.getStructuringElement(cv2.MORPH_RECT,(13,13))
    defect=cv2.morphologyEx(defect,cv2.MORPH_CLOSE,kernel_close)
    contours,hier=cv2.findContours(defect,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    Map=test_image.copy()
    Map[:,:,:]=0
    x_c=[]
    y_c=[]
    for(index,contour) in  enumerate(contours):
        y, x, h, z = cv2.boundingRect(contours[index])
        if(np.sum(Map[y-64:y+64,x-64:x+64,:])==0):
          x_c.append(x)
          y_c.append(y)
          filemame="C:\\Users\\User\\Desktop\\PCB_DATASET\\Defect_data\\mouse_bite\\"+str(def_num)+".jpg"
          try:
               cv2.imwrite(filemame,test_image[x-128:x+128,y-128:y+128,:])
               def_num +=1
          except:
               pass
          Map[y-16:y+16,x-16:x+16]=255
        
          
template_path="C:\\Users\\User\\Desktop\\PCB_DATASET\\PCB_USED"
template_files=[]
template=[]
for  fileNames in os.walk(template_path):
    for name in fileNames[2]:
        template_files.append(template_path+"\\"+name)
for name in template_files:
    template.append(cv2.imread(name)) 
test_path="C:\\Users\\User\\Desktop\\PCB_DATASET\\images\\Mouse_bite"
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