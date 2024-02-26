from PIL import Image
# api-key = AIzaSyBmpjwN8e1VxXXZWIIospFdrSnXh2mQPvQ
def load_image(image_path):
    img = Image.open(image_path)
    return img



load_image('/Users/avyuktsoni/Desktop/6.png')