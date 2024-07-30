import os
import shutil

''' Assuming we already have the images folder with instances in 7 subfolders 
named ['left_only', 'left_right', 'left_right_through', 'left_through', 'right_only', 'right_through', 'through'].
We will need to manually do the step of copying the images in the combined arrow folders over to a new folder called 'other',
and delete those original conbined arrow folders (as it's quite messy to try to incorporate this in the code below)
This code will create a directory structure that looks like this:
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
Because we are working with cropped arrow images, 
the content of the text file for each image will be [class_name] 0.5 0.5 1 1, 
where class_name follows the class mapping for the 4-class model detailed in the code.
'''


# Path to the dataset directory
dataset_path = 'dataset'

os.makedirs(os.path.join(dataset_path, 'labels'), exist_ok=False)
import os

# Paths to the main image and label directories
image_dir = 'dataset/images'
label_dir = 'dataset/labels'

# Define class mapping
class_mapping = {
    'left_only': 0,
    'right_only': 1,
    'through': 2,
    'other': 3
}

# Create the labels directory if it does not exist
os.makedirs(label_dir, exist_ok=True)

# Loop over each subfolder (class) in the image directory
for subfolder in os.listdir(image_dir):
    subfolder_path = os.path.join(image_dir, subfolder)
    
    if not os.path.isdir(subfolder_path):
        continue
    
    # Determine class name based on subfolder name
    class_name = class_mapping[subfolder]
    
    # Create corresponding label subfolder
    label_subfolder_path = os.path.join(label_dir, subfolder)
    os.makedirs(label_subfolder_path, exist_ok=True)
    
    # Loop over each image file in the subfolder
    for image_file in os.listdir(subfolder_path):
        if image_file.endswith(('.jpg', '.jpeg', '.png')):
            # Create the content for the corresponding text file
            content = f"{class_name} 0.5 0.5 1 1"
            
            # Create the label file path
            label_file = os.path.join(label_subfolder_path, image_file.replace(image_file.split('.')[-1], 'txt'))
            
            # Write the content to the label file
            with open(label_file, 'w') as f:
                f.write(content)
