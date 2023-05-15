import numpy as np
import cv2
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
#     print(args.file)
    mask = cv2.imread("/workspace/DDNM/exp/inp_masks_raindrop/mask_th05_all/"+args.file)
#     print(mask)
    print(mask.shape)
    mask = mask[:, :, 0]
    mask = (mask == 255) * 1
    print(mask.shape)
    np.save("/workspace/DDNM/exp/inp_masks_raindrop/mask.npy", mask)


