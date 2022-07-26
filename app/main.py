from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

import cv2
import tensorflow as tf

from app.image_classify import nude_classify

model_nude = tf.keras.models.load_model('./app/model/nudenetResnet50.h5')

class Item(BaseModel):
    img_urls: list[str] = []

app = FastAPI()

@app.post('/nude-detect')
async def nude_detect(item: Item):
    nude_arr = []
    if(len(item.img_urls) > 0):
        for i in item.img_urls:
            print(i)
            if(nude_classify(i,model_nude)):
                tmp_name = ((i.split('/')[-1]))
                nude_arr.append(tmp_name)
    return {'result':bool(len(nude_arr)),'nude_arr':nude_arr}