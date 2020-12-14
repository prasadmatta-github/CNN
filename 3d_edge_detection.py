import cv2
import numpy as np


b_img = np.zeros((200,200,3),dtype='uint8')
w_img = np.ones((200,200,3),dtype='uint8')
w_img = w_img * 255
u_img = cv2.hconcat([b_img,w_img])
l_img = cv2.hconcat([w_img,b_img])

img = cv2.vconcat([u_img,l_img])

img = cv2.imread('/home/prasadmatta/Desktop/CNN/2.jpg')

print('input image',img.shape)
                   
vertical_kernal = [[[1,0,-1],[1,0,-1],[1,0,-1]],
                   [[1,0,-1],[1,0,-1],[1,0,-1]],
                   [[1,0,-1],[1,0,-1],[1,0,-1]]]

horizontal_kernal = [[[1,1,1],[0,0,0],[-1,-1,-1]],
                     [[1,1,1],[0,0,0],[-1,-1,-1]],
                     [[1,1,1],[0,0,0],[-1,-1,-1]]]

p_val = 1
for i in range(4):
    img = np.rot90(img)
    pad_val = np.zeros((p_val,img.shape[1],3),dtype=np.uint8)
    img = cv2.vconcat([img,pad_val])

class EDGE:

    def __init__(self,img,kernal,strides):

        self.img = img
        self.height,self.width,self.channel = self.img.shape
        self.kernal = np.array(kernal)
        self.strides = strides

    def vertical(self):
        
        self.gen_img = []
        for ht in range(0,self.height-2):
            row =[]
            for wdt in range(0,self.width-2):
                n_img = self.img[ht:ht+3,wdt:wdt+3] * self.kernal
                row.append(sum(list(map(lambda x :sum(x),n_img))))
            self.gen_img.append(row)
        self.gen_img = np.array(self.gen_img,dtype='uint8')
        return self.gen_img

for i in ['vertical_kernal','horizontal_kernal']:
    edge_vertical = EDGE(img,eval(i),2)
    vertical_img = edge_vertical.vertical()
    print('output',img.shape,vertical_img.shape)
    cv2.imshow('{0}'.format(str(i)),vertical_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

