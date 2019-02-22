from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np


# Creating model with architecture VGG16
model = VGG16(weights='imagenet')

# Downloading picture and transform it into arrayy
img_path = path\zeship2.jpg'

# Lets starting recognizing picture
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)


preds = model.predict(x)

# Print 3 classes with the biggest chance of coincidence
#print('', decode_predictions(preds, top=3)[0])
print('Result of recognizing:', decode_predictions(preds,top=3)[0])
