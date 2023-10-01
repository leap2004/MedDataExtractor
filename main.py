from text_extractor import TextExtractor
from image_cleaner import ImageCleaner

def get_user_input():
    input_image_path = input("Please insert the path for inputted images: ")
    output_image_path_noBackground = input("Please insert the path for output images with no background: ")
    output_image_path_noText = input("Please insert the path for output images with no text: ")
    output_text_path = input("Please insert path for outputted text file: ")
    output_csv_path = input("Please insert path for outputted csv file: ")

    return input_image_path, output_image_path_noBackground, output_image_path_noText, output_text_path, output_csv_path

def process_images(input_image_path, output_image_path_noBackground, output_text_path, output_csv_path):
    text_extractor = TextExtractor(output_text_path, output_csv_path)
    image_cleaner = ImageCleaner(output_image_path_noBackground, output_image_path_noText)

    # Perform image processing
    image_cleaner.remove_background_keep_text(input_image_path)

    # Extract text from processed images
    text_extractor.text_extract(output_image_path_noBackground)

    # Remove text from the original input images
    image_cleaner.remove_text(input_image_path)

    # Generate the CSV with extracted information
    text_extractor.output_csv()

if __name__ == "__main__":
    input_image_path, output_image_path_noBackground, output_image_path_noText, output_text_path, output_csv_path = get_user_input()

    process_images(input_image_path, output_image_path_noBackground, output_text_path, output_csv_path)
