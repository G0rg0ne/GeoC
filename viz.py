# Visualizing the dataset
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Image and Mask filename: M-33-20-D-c-4-2.tif")
print()
temp_img = cv2.imread("data/images/M-33-20-D-c-4-2.tif", 1) # 3 channels / spectral bands
temp_img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB)
print("Image shape:", temp_img.shape)
print()

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(temp_img[:,:,2])
plt.title("One channel of image")
plt.subplot(122)
plt.imshow(temp_img)
plt.title("All channels of image")
plt.show()
print()

temp_mask = cv2.imread("data/masks/M-33-20-D-c-4-2.tif") # 3 channels but all same. Can also read with cv2.imread(path, 0) to get only one channel.
print("Mask shape:", temp_mask[:,:,0].shape)
print()
classes, count = np.unique(temp_mask[:,:,0], return_counts=True) # Visualize only one channel. All chanels are identical.
print("Classes are: ", classes, " and the counts are: ", count)
print()

plt.figure(figsize=(6, 4))
plt.imshow(temp_mask[:,:,0])
plt.title("Mask")
plt.show()
print()