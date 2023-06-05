import numpy as np 
import cv2
img=cv2.imread('mypic.png',0)
temp=cv2.imread('halfpic.png',0)
#limitation: - both image and template should have same dimensions


h,w=temp.shape #template.shape() return height, weight
#img is 2d array as it is grey scale

'''Different algorithms or methods are there to do template matching'''
methods=[cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
for method in methods:
    img2=img.copy()
    result=cv2.matchTemplate(img2,temp,method)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
    # (W-w+1,H-h+1) times we have to compare( can be the possible solution)

    print(min_loc,max_loc)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        loc=min_loc
    else:
        loc=max_loc
    bottom_right=(loc[0]+w,loc[1]+ h)
    cv2.rectangle(img2,loc,bottom_right,255,5)
    cv2.imshow('Match',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

