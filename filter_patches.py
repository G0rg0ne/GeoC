'''
This code filters all the unecessary  patches taht we created using patches.py
we only want to keep representative images to train our network on represnetative features.
we want to keep the patches where background class occupies more than 95% of the image, discard the image and mask
'''
import os 
import cv2
import numpy as np

root_directory = "data"
patch_size = 512

patches_img_dir = os.path.join(f"patches_{patch_size}", "images")
patches_img_dir = os.path.join(root_directory, patches_img_dir)
patches_mask_dir = os.path.join(f"patches_{patch_size}", "masks")
patches_mask_dir = os.path.join(root_directory, patches_mask_dir)

def discard_useless_patches(patches_img_dir, patches_mask_dir):
  for filename in os.listdir(patches_mask_dir):
    img_path = os.path.join(patches_img_dir, filename)
    mask_path = os.path.join(patches_mask_dir, filename)
    img = cv2.imread(img_path)
    mask = cv2.imread(mask_path)
    classes, count = np.unique(mask, return_counts = True)
    # If background class occupies more than 95% of the image, discard the image and mask
    if (count[0] / count.sum()) > 0.95:
      os.remove(img_path)
      os.remove(mask_path)

discard_useless_patches(patches_img_dir, patches_mask_dir)