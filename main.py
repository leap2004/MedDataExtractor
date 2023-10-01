from image_processor import ImageProcessor
from text_extractor import TextExtractor
from image_cleaner import ImageCleaner

def process_images(input_image_path, output_image_path_noBackground, output_text_path, output_csv_path):
    # Declaring input/output path directories
    input_image_path=input("Please insert the path for inputted images: ")
    output_image_path_noBackground=input("Please insert the path for output images with no background: ")
    output_image_path_noText=input("Please insert the path for output images with no text: ")
    output_text_path=input("Please insert path for outputted text file: ")
    output_csv_path=input("Please insert path for outputted csv file: ")
  
    image_processor = ImageProcessor(input_image_path, output_image_path_noBackground, output_text_path)
    text_extractor = TextExtractor(output_text_path, output_csv_path)
    image_cleaner = ImageCleaner(input_image_path, output_image_path_noText)

    # Perform image processing
    image_cleaner.remove_background_keep_text()

    # Extract text from processed images
    text_extractor.text_extract(output_image_path_noBackground)

    # Remove text from the original input images
    image_cleaner.remove_text()

    # Generate the CSV with extracted information
    text_extractor.output_csv()

    process_images(input_image_path, output_image_path_noBackground, output_text_path, output_csv_path)
