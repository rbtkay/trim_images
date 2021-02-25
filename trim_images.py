from os.path import isfile, join
from os import listdir
import os
from PIL import Image
print("trimming image...")

SOURCE_DIRECTORY = "./images/pokemons"
RESULT_DIRECTORY = "./results"
RESULT_DIRECTORY_220px = "./results/220px"
COMPARE_RESULT_DIRECTORY = "./results"

def resize_image(image_path: str, required_size_x: float, required_size_y: float):
    image = Image.open(image_path)
    image_name = os.path.basename(image_path)

    image.thumbnail((required_size_x, required_size_y))
    image.save(f"{RESULT_DIRECTORY}/{image_name}")
    print(image.size)


def trim_and_resize_image(image_path: str, required_size: float = -1, folder: str = RESULT_DIRECTORY):
    image = Image.open(image_path)
    image_name = os.path.basename(image_path)

    print(image_path)

    image_trimmed = image.crop(image.getbbox())

    if required_size > -1 and (image.size[0] > required_size or image.size[1] > required_size):
        image_trimmed.thumbnail((required_size, required_size))
    
    image_trimmed.save(f"{folder}/{image_name}")


SIZE_TO_COMPARE = 455

def is_image_small(image_path: str):
    image = Image.open(image_path)
    if image.size[0] < SIZE_TO_COMPARE and image.size[1] < SIZE_TO_COMPARE:
        image.save(f"{COMPARE_RESULT_DIRECTORY}/{os.path.basename(image_path)}")
        return 1
    return 0


images = [f"{SOURCE_DIRECTORY}/{image}" for image in listdir(
    SOURCE_DIRECTORY) if isfile(join(SOURCE_DIRECTORY, image))]

print("number of images", len(images))

print("processing to 220px")
[trim_and_resize_image(image, 220, RESULT_DIRECTORY_220px) for image in images]
print("processing to 455px")
[trim_and_resize_image(image, 455) for image in images]
print("done successfully")