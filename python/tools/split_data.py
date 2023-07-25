import argparse
import os
import shutil
import random
import numpy as np
from loguru import logger


def split_data(args):
    input_dir = args.input_dir
    output_dir = args.output_dir
    
    if not os.path.exists(input_dir):
        raise IOError("input_dir not exists")
    
    for mode in ["train", "val", "test"]:
        folder=os.path.join(output_dir, mode)
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    random.seed(args.seed)
    np.random.seed(args.seed)

    files = np.array(os.listdir(input_dir))
    np.random.shuffle(files)
    len_ = len(files)
    sum_ = args.train + args.val + args.test

    train_len = int((args.train / sum_)  * len_)
    val_len = int((args.val / sum_) * len_)
    logger.info(f"train set length : {train_len}")
    logger.info(f"val set length : {val_len}")

    train_sets = files[:train_len]
    val_sets = files[train_len:train_len+val_len]
    test_sets = files[train_len+val_len:]

    # details
    if args.test == 0 and len(test_sets)!= 0:
       train_sets = np.append(train_sets,test_sets)
    
    for t in train_sets:
        shutil.copy(os.path.join(input_dir, t), os.path.join(output_dir, "train", prefix_name(args,t)))
    for v in val_sets:
        shutil.copy(os.path.join(input_dir, v),os.path.join(output_dir, "val",prefix_name(args,v)))
    if args.test != 0:
        for t in test_sets:
            shutil.copy(os.path.join(input_dir, t),os.path.join(output_dir, "test",prefix_name(args,t)))

        

def prefix_name(args,file_name):
    return args.prefix + "_" + file_name


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split Data')
    parser.add_argument('--input_dir', type=str, required=True)
    parser.add_argument('--output_dir', type=str, default="./output") 
    parser.add_argument('--train', type=int, default=8)
    parser.add_argument('--val', type=int, default=2)
    parser.add_argument('--test', type=int, default=0)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--prefix', type=str, default="", help="rename prefix when copying files")


    args = parser.parse_args()
    split_data(args)



   
