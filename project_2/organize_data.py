import glob
import os.path
import shutil
        
num_img_folders = 0    # Number of folders that contain images
dir_img_folders = 'data/photos/'   # Directory where all the folders of the images are contained
directory = 'data/' # Directory where the test, train, and validation folders are contained
              # Make sure for this directory that the folders are already created

# Set the percentage that each folder will contain (for the number of images)
test_perc = 0.20
train_perc = 0.70
valid_perc = 0.10

# Will contain the string directories of the pictures which will be moved to their corresponding folders
test = {}
train = {}
validation = {}

# Detects the number of folders within the "photos" folder
num_img_folders = len(os.listdir(dir_img_folders))

# Organizes all the pictures into a dictionary type variable
photos = {}
photo_dir = os.listdir(dir_img_folders)

for name in photo_dir:
        if name not in test.keys():
            test[name] = []
            train[name] = []
            validation[name] = []

        photos["" + name] = glob.glob(dir_img_folders + name + "/*.jpg")

# Assigns all the picures to their corresponding folders (test, train, validation)
for photo_folder, test_data_folder, train_data_folder, valid_data_folder in zip(photos, test, train, validation):
    length = len(photos[photo_folder])

    test_portion = int(length * test_perc)
    train_portion = int(length * train_perc)

    first_index = test_portion + 1
    second_index = test_portion + train_portion + 1
    
    for i in range(0, first_index):
        test[test_data_folder].append(photos[photo_folder][i])

    for j in range(first_index, second_index):
        train[train_data_folder].append(photos[photo_folder][j])

    for k in range(second_index, length):
        validation[valid_data_folder].append(photos[photo_folder][k])
        


# For the next three loops, the photos are copied into the test, train, and validation folders
for folder in test:
    try:
        os.mkdir(directory + "/test/" + folder)
    except OSError:
        print ("Creation of the directory %s failed" % folder)
    else:
        print ("Successfully created the directory %s " % folder)

    for src in test[folder]:
        shutil.copy(src, directory + "test/" + folder + "/")


for folder in train:
    try:
        os.mkdir(directory + "/train/" + folder)
    except OSError:
        print ("Creation of the directory %s failed" % folder)
    else:
        print ("Successfully created the directory %s " % folder)

    for src in train[folder]:
        shutil.copy(src, directory + "train/" + folder + "/")

for folder in validation:
    try:
        os.mkdir(directory + "/validation/" + folder)
    except OSError:
        print ("Creation of the directory %s failed" % folder)
    else:
        print ("Successfully created the directory %s " % folder)

    for src in validation[folder]:
        shutil.copy(src, directory + "validation/" + folder + "/")
