import cv2
import numpy as np


b_img = np.zeros((200,200),dtype='uint8')
w_img = np.ones((200,200),dtype='uint8')
w_img = w_img * 255
u_img = cv2.hconcat([b_img,w_img])
l_img = cv2.hconcat([w_img,b_img])

img = cv2.vconcat([u_img,l_img])

img = cv2.imread('/home/prasadmatta/Desktop/CNN/2.jpg',0)
print(img.shape)
vertical_kernal = [[1,0,-1],[1,0,-1],[1,0,-1]]
horizontal_kernal = [[1,1,1],[0,0,0],[-1,-1,-1]]
sobel_filter = [[1,0,-1],[2,0,-2],[1,0,-1]]

p_val = 1
for i in range(4):
    img = np.rot90(img)
    pad_val = np.zeros((p_val,img.shape[1]),dtype=np.uint8)
    img = cv2.vconcat([img,pad_val])

class EDGE:

    def __init__(self,img,kernal):

        self.img = img
        self.height,self.width = self.img.shape
        self.kernal = np.array(kernal)
        
    def vertical(self):
        
        self.gen_img = []
        for ht in range(self.height-2):
            row =[]
            for wdt in range(self.width-2):
                n_img = self.img[ht:ht+3,wdt:wdt+3] * self.kernal
                row.append(sum(list(map(lambda x :sum(x),n_img))))
            self.gen_img.append(row)
        self.gen_img = np.array(self.gen_img,dtype='uint8')
        return self.gen_img

for i in ['vertical_kernal','horizontal_kernal']:
    k = eval(i)
    edge_vertical = EDGE(img,k)
    vertical_img = edge_vertical.vertical()
    print(img.shape,vertical_img.shape)
    cv2.imshow('{0}'.format(str(i)),vertical_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

