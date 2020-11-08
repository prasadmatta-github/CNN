import cv2
import numpy as np

img = 'test_case1.jpg'

vertical_kernal = [[1,0,-1],[1,0,-1],[1,0,-1]]
horizontal_kernal = [[1,1,1],[0,0,0],[-1,-1,-1]]

class EDGE:

    def __init__(self,img,kernal):
        self.img = cv2.imread(img,0)
        self.height,self.width = self.img.shape
        self.kernal = kernal
        
    def vertical(self):
        
        self.gen_img = []
        for ht in range(self.height-2):
            row =[]
            for wdt in range(self.width-2):
                n_img = self.img[ht:ht+3,wdt:wdt+3] * self.kernal
                row.append(sum(list(map(lambda x :sum(x),n_img))))
            self.gen_img.append(row)
        self.gen_img = np.array(self.gen_img,dtype=np.uint8)
        return self.gen_img

    def horizontal(self):
        
        self.gen_img = []
        for ht in range(self.height-2):
            row =[]
            for wdt in range(self.width-2):
                n_img = self.img[ht:ht+3,wdt:wdt+3] * self.kernal
                row.append(sum(list(map(lambda x :sum(x),n_img))))
            self.gen_img.append(row)
        self.gen_img = np.array(self.gen_img,dtype=np.uint8)
        return self.gen_img

edge_vertical = EDGE(img,vertical_kernal)
vertical_img = edge_vertical.vertical()

edge_horizontal = EDGE(img,horizontal_kernal)
horizontal_img = edge_horizontal.vertical()
for out_img in [vertical_img,horizontal_img]: 
    cv2.imshow('out_img',out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()