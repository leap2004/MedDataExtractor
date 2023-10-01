import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, input_image_path, output_image_path_noBackground, output_text_path):
        self.input_image_path = input_image_path
        self.output_image_path_noBackground = output_image_path_noBackground
        self.output_text_path = output_text_path

    def remove_background_keep_text(self):
        for filename in os.listdir(self.input_image_path):
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.jpeg'):
                input_file_path = os.path.join(self.input_image_path, filename)
                # Read the image as grayscale
                image = cv2.imread(input_file_path, cv2.IMREAD_GRAYSCALE)

                # Image Segmentation: Thresholding to create a binary mask
                _, binary_mask = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

                # Find the contours in the binary mask
                contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Create a blank mask to draw the contours
                blank_mask = np.zeros_like(binary_mask)

                # Draw the text contours on the blank mask
                cv2.drawContours(blank_mask, contours, -1, 255, thickness=cv2.FILLED)

                # Invert the binary mask to keep the text region and remove the background
                result_image = cv2.bitwise_and(image, image, mask=blank_mask)

                # Save the result
                output_file_name_image_text = f"image_extracted_text_{filename}"  # Update the filename with the image name
                output_file_path_image_text = os.path.join(self.output_image_path_noBackground, output_file_name_image_text)
                cv2.imwrite(output_file_path_image_text, result_image)

                print(f"Background removed for image {filename}. The image has been saved in the {self.output_image_path_noBackground} folder.")
