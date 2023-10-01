import os
import cv2
import numpy as np
import extcolors

class ImageCleaner:
    def __init__(self, output_image_path_noBackground):
        self.output_image_path_noBackground = output_image_path_noBackground

    def remove_background_keep_text(self, input_image_path):
        for filename in os.listdir(input_image_path):
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.jpeg'):
                input_file_path = os.path.join(input_image_path, filename)
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

                print(f"Background removed for image {filename}. The image has been saved in the output_image_path_noBackground folder.")
    
    def remove_text(self, input_image_path):
        for filename in os.listdir(input_image_path):
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.jpeg'):
                input_file_path = os.path.join(input_image_path, filename)
                # Load the input image
                image = cv2.imread(input_file_path)

                # Initialize the MMOCRInferencer
                inferencer = MMOCRInferencer(det='dbnet')

                # Perform text detection using MMOCRInferencer
                result = inferencer(image, return_vis=True)

                colors_x = extcolors.extract_from_path(input_file_path, tolerance=12, limit=1)
                intermediate_data = colors_x[0][0]
                dominant_color = intermediate_data[0]

                predictions = result['predictions']

                # Create a copy of the input image to work on
                output_image = image.copy()

                for i, prediction in enumerate(predictions):
                    det_polygons = prediction['det_polygons']
                    for j, polygon in enumerate(det_polygons):
                        x1, y1, x2, y2, x3, y3, x4, y4 = polygon[:8]  # Take the first eight values
                        x1, y1, x2, y2, x3, y3, x4, y4 = int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), int(x4), int(y4)

                        # Draw a gray rectangle over the polygon region
                        output_image = cv2.rectangle(output_image, (min(x1, x2, x3, x4), min(y1, y2, y3, y4)),
                                                     (max(x1, x2, x3, x4), max(y1, y2, y3, y4)), dominant_color, -1)

                # Save the output image with removed text to the specified path
                output_file_name_image = f"extracted_text_{filename}"  # Update the filename with the image name
                output_file_path_image = os.path.join(self.output_image_path_noText, output_file_name_image)
                cv2.imwrite(output_file_path_image, output_image)

                print(f"Text removed for image {filename}. The image has been saved in the output_image_path_noText folder.")
