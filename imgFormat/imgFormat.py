from PIL import Image
import os
import sys
import concurrent.futures
import shutil

valid_image_formats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

def convert_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        img.save(output_path, 'PNG', optimize=True)
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def process_image(input_dir, output_dir, img_format):
    os.makedirs(output_dir, exist_ok=True)
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for filename in os.listdir(input_dir):
            if filename.lower().endswith(img_format):
                input_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, filename)
                shutil.copy(input_path, output_path)
                print(filename)
            else:   
                new_filename = os.path.splitext(filename)[0] + img_format
                output_path = os.path.join(output_dir, new_filename)
                input_path = os.path.join(input_dir, filename)
                executor.submit(convert_image, input_path, output_path)
                print(new_filename)
        executor.shutdown(wait=True)

    print("DONE!")

if __name__ == "__main__":
    input_dir = input('Input Folder: ')
    output_dir = input('Output Folder: ')
    img_format = input("Convert images to format (.png): ").lower()

    if img_format not in valid_image_formats:
        sys.exit("Invalid image format specified.")

    process_image(input_dir, output_dir, img_format)
