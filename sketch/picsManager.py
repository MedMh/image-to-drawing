import cv2
import secrets
import os
from PIL import Image


def save_picture(form_picture, app):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    #i.thumbnail(output_size)
    i.save(picture_path)
    return random_hex, picture_path, picture_fn

def image_to_sketch(filename, filepath, app):
    im = cv2.imread(filepath)
    grey_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_image)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_image, inverted_blur, scale=256.0)
    file_result = filename + '_result.jpg'
    picture_path = os.path.join(app.root_path, 'static/pics', file_result)
    cv2.imwrite(picture_path, sketch)
    return file_result