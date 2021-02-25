from os.path import isfile, join
from os import listdir
import os
import csv
import shutil
import re
from PIL import Image

POKEMON = "./images/pokemons"
ITEM = "./images/items/sprites"
TSV_FILE ="./7th_generation.tsv"


def is_7th_generation(image_name: str):
    pokemon_tsv_file = open(TSV_FILE)
    read_tsv = csv.reader(pokemon_tsv_file, delimiter="\t")
    for line in read_tsv:
        print(line)

    return False
    #     name = line[4].lower()
    #     if re.search(rf'\w*{name}\w*', image_name):
    #         return True

def move_image(origin: str, destination: str, count: int):
    image_name = os.path.basename(origin)
    if is_7th_generation(image_name):
        shutil.copyfile(origin, f"{destination}/{image_name}")

# images = [f"{POKEMON}/{image}" for image in listdir(POKEMON) if isfile(join(POKEMON, image))]
items = [f"{ITEM}/{item}" for item in listdir(ITEM) if isfile(join(ITEM, item))]
count = 0
total_count = 0
for item in items:
    move_image(item, "./7th_generation", count)


