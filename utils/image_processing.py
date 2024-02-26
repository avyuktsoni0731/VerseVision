from PIL import Image
def load_image(image_path):
    img = Image.open(image_path)
    return img
