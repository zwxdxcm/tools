import argparse
import os
from utils.img import * 
from utils.io import create_dirs
import cv2 as cv
import tqdm


def img_process(args):
    input_dir = args.input_dir
    output_dir = args.output_dir
    
    if not os.path.exists(input_dir):
        raise IOError("input_dir not exists")
    
    create_dirs(output_dir,clear=True)

    files = os.listdir(input_dir)
    for f in tqdm.tqdm(files):
        img = cv.imread(os.path.join(input_dir, f))
        ret = crop(img)
        cv.imwrite(os.path.join(output_dir, f), ret)
    

def crop(img):
    ## process
    h,w,_=img.shape
    cut = int(w*0.1)
    ret = img[:,cut:,:]
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split Data')
    parser.add_argument('--input_dir', type=str, required=True)
    parser.add_argument('--output_dir', type=str, default="./output") 
    args = parser.parse_args()
    img_process(args)
