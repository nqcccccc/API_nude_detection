from multiprocessing.sharedctypes import Value
import cv2
import numpy as np
from app.readimage import read_img_from_url

dict_class={0:'hentai',
            1:'neutral',
            2:'porn',
            3:'sexy'
            }

def nude_classify(url,model):

    image = read_img_from_url(url)
    image_resized= cv2.resize(image, (240,240))
    image=np.expand_dims(image_resized,axis=0)
    pred=model.predict(image)

    pred_index = np.argmax(pred[0])
    label = dict_class[pred_index]
    print(pred)
    if(label == 'porn'):
        if(pred[0][pred_index] > 0.7):
            return True
    elif (label == 'hentai'):
        if (pred[0][pred_index] > 0.7):
            return True
    return False
