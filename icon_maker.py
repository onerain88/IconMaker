#!/usr/bin/python
#coding=utf-8
import os
import json
from PIL import Image, ImageDraw

def gen_mipmaps(src_path, mipmaps, icon_name):
    im = Image.open(src_path)
    for mipmap in mipmaps:
        name = mipmap['name']
        size = mipmap['size']
        icon_file = os.path.join('android', name, icon_name)
        icon = im.resize((size, size), Image.ANTIALIAS)
        if not os.path.exists(os.path.dirname(icon_file)):
            os.makedirs(os.path.dirname(icon_file))
        icon.save(icon_file, quality = 100)
        print('gen %s done' % name)

def gen_round_corners(src_path, dist_path, percent):
    im = Image.open(src_path)
    w, h = im.size
    rad = int(w * percent)
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill = 255)
    alpha = Image.new('L', im.size, 255)
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    im.save(dist_path)
    print('gen round icon done.')

def get_config(json_file):
    with open(json_file,'r') as load_f:
        json_dict = json.load(load_f)
        return json_dict

if __name__ == '__main__':
    config = get_config("./android.json")
    print('get config done.')
    src_path = config['icon']
    if config['round']:
        round_image = 'round_icon.png'
        gen_round_corners(src_path, round_image, config['percent'])
        src_path = round_image
    gen_mipmaps(src_path, config['mipmaps'], config['icon_name'])
    print('done')