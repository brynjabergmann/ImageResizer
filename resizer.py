from PIL import Image
from resizeimage import resizeimage
from os import listdir
from os.path import join, dirname, exists, basename


def resize(source_image, destination_image, size=[210,140]):
    ''' Resizes one image.

    Parameters
    --------------
    source_image: path to source image. 
    destination_image: path for resized image. 
    size: optional resize size (default=200x200). 
    '''
    with open(source_image, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_thumbnail(image, size) 
            cover.save(destination_image, image.format)


def resize_directory(source, destination, size=[210, 140]):
    ''' Lists all the images in the source directory, resizes them and returns the resized images to the destination directory.

    Parameters
    --------------
    source: path to source directory. 
    destination: path for destination directory. 
    size: optional resize size (default=200x200). 
    '''
    dirs = listdir(source)
    for file in dirs:    
        print (file)
        resize(join(source, file), join(destination, file), size)


if __name__ == "__main__" :
    '''Example use'''
    src = join(dirname(__file__), "images")
    dest = join(dirname(__file__), 'small_images')
    resize_directory(src, dest)