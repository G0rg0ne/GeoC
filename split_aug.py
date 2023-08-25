import splitfolders  # or import split_folders
import os


patch_size = 512

root_directory = "data"
patches_img_dir = os.path.join(f"patches_{patch_size}", "images")
patches_img_dir = os.path.join(root_directory, patches_img_dir)
input_folder = patches_img_dir.strip("images")
print(input_folder)
output_folder = os.path.join(root_directory, "train_val_test")
print(output_folder)

os.makedirs(output_folder, exist_ok=True)

# Split with a ratio.
# To split into training, validation, and testing set, set a tuple to `ratio`, i.e, `(.8, .1, .1)`.
splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(.8, .2), group_prefix=None, move=False) # splitting in training and validation only

train_dir = os.path.join(output_folder, "train")
val_dir = os.path.join(output_folder, "val")
# test_dir = os.path.join(output_folder, "test")