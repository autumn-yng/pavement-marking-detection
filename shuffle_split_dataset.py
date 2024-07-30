import os  # For file and directory operations
import shutil  # For copying files
import random  # For shuffling the data

'''
Inpput directory structure:
dataset/
├── images/
│   ├── left_only/
│   │   ├── image1.png
│   │   ├── image2.png
│   │   └── ...
│   ├── right_only/
│   │   ├── image1.png
│   │   ├── image2.png
│   │   └── ...
│   ├── through/
│   │   ├── image1.png
│   │   ├── image2.png
│   │   └── ...
│   └── other/
│       ├── image1.png
│       ├── image2.png
│       └── ...
└── labels/
    ├── left_only/
    │   ├── image1.txt
    │   ├── image2.txt
    │   └── ...
    ├── right_only/
    │   ├── image1.txt
    │   ├── image2.txt
    │   └── ...
    ├── through/
    │   ├── image1.txt
    │   ├── image2.txt
    │   └── ...
    └── other/
        ├── image1.txt
        ├── image2.txt
        └── ...

Output directory structure:
dataset/
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/

'''
# Paths to the main image and label directories
image_dir = 'dataset/images'
label_dir = 'dataset/labels'

# Create directories for training, validation, and testing datasets
os.makedirs('dataset/train/images', exist_ok=True)
os.makedirs('dataset/train/labels', exist_ok=True)
os.makedirs('dataset/val/images', exist_ok=True)
os.makedirs('dataset/val/labels', exist_ok=True)
os.makedirs('dataset/test/images', exist_ok=True)
os.makedirs('dataset/test/labels', exist_ok=True)

# Define split ratios for training, validation, and testing sets
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# Get the list of all classes (subdirectories in the image directory)
classes = os.listdir(image_dir)

# Loop over each class directory
for cls in classes:
    # List all image files in the current class directory
    image_files = os.listdir(os.path.join(image_dir, cls))
    # Shuffle the image files to ensure random splitting
    random.shuffle(image_files)
    
    # Calculate the number of files for each split
    total_files = len(image_files)
    train_end = int(total_files * train_ratio)  # Index marking end of training set
    val_end = train_end + int(total_files * val_ratio)  # Index marking end of validation set
    
    # Loop over each file and distribute it into train, val, or test set
    for i, file in enumerate(image_files):
        # Construct the full paths for the image and its corresponding label
        img_src = os.path.join(image_dir, cls, file)
        label_src = os.path.join(label_dir, cls, file.replace('.png', '.txt'))
        
        # Determine the destination directory based on the current index
        if i < train_end:
            # Training set
            img_dst = os.path.join('dataset/train/images', f'{cls}_{file}')
            label_dst = os.path.join('dataset/train/labels', f'{cls}_{file.replace(".png", ".txt")}')
        elif i < val_end:
            # Validation set
            img_dst = os.path.join('dataset/val/images', f'{cls}_{file}')
            label_dst = os.path.join('dataset/val/labels', f'{cls}_{file.replace(".png", ".txt")}')
        else:
            # Testing set
            img_dst = os.path.join('dataset/test/images', f'{cls}_{file}')
            label_dst = os.path.join('dataset/test/labels', f'{cls}_{file.replace(".png", ".txt")}')
        
        # Copy the image and label files to their respective destination directories
        shutil.copyfile(img_src, img_dst)
        shutil.copyfile(label_src, label_dst)
