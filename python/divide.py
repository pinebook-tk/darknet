import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

current_dir = '../data/whill'
g_colab_full_path='/cotent/darknet/data/whill'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('whill-train.txt', 'w')  
file_test = open('whill-test.txt', 'w')# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
        counter = counter + 1
