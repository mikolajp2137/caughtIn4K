from PIL import Image
import os

# Set the input and output folders to wherever you want your images to be stored
input_folder = "C:\\Users\\Mikolaj\\Pictures\\to_resize"
output_folder = "C:\\Users\\Mikolaj\\Pictures\\resized"

new_width = 3840
new_height = 2160

for file_name in os.listdir(input_folder):
    if file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".jpeg"):
        image = Image.open(os.path.join(input_folder, file_name))
        width, height = image.size
        proportions = width / height
        new_height = int(new_width / proportions)
        resized_image = image.resize((new_width, new_height))
        resized_image.save(os.path.join(output_folder, file_name))
        print(file_name + " done")
