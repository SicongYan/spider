import tesserocr;
from PIL import Image;
from util import saveImage;
import time;
import requests;

def identify_image(imagePath):
    image = Image.open(imagePath);
    result = tesserocr.image_to_text(image);
    return result;

if __name__ == '__main__':
    url = "http://my.cnki.net/elibregister/CheckCode.aspx";
    saveImage.save_image(url, "test.jpg");
    print(identify_image("E:\\python work\\spider\\tnet\\test.jpg"));


