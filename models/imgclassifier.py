import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image

class ImageClassifier:
    def __init__(self, model_path='models/finetuned.h5'):
        self.model=load_model(model_path)
        self.class_names=[
            'airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck'
        ]

    def preprocess_image(self, image_path):
        img=Image.open(image_path).convert('RGB') 
        img=img.resize((224,224))
        img_array=np.array(img)
        img_array = preprocess_input(img_array)
        return np.expand_dims(img_array,axis=0)
    
    def predict(self,img_path):
        img_tensor=self.preprocess_image(img_path) #tiền xử lý ảnh
        prediction=self.model.predict(img_tensor)
        index=np.argmax(prediction) #lấy chỉ số có xác suất cao nhất
        class_name=self.class_names[index]
        confiden=f"{np.max(prediction)*100:.2f}%"
        return class_name,confiden