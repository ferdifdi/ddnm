import numpy as np
import cv2

mask = cv2.imread("./mask.png")
print(mask.shape)
mask = mask[:, :, 0]
mask = (mask == 255) * 1
print(mask.shape)
np.save("mask.npy", mask)

mask = cv2.imread("./mask_mouth.png")
print(mask.shape)
mask = mask[:, :, 0]
mask = (mask == 255) * 1
print(mask.shape)
np.save("mask_mouth.npy", mask)


