Angiography Scan Analysis using OpenCV and Natural Language Processing


## Overview

This project utilizes the power of OpenCV (Open Source Computer Vision Library) and natural language processing (NLP) techniques to analyze angiography scans, extract relevant information, redact confidential patient information, and perform various functions on the scans. The goal is to automate the process of extracting and redacting critical data from angiography scans, allowing for the aggregation of data for further analysis.

## Features

- **Background Removal**: Utilize image segmentation to remove the background and retain only the text and relevant regions within angiography scans.

- **Text Extraction**: Implement Optical Character Recognition (OCR) using Tesseract to extract text from different sections of the angiography scans.
  
- **Text Redaction**: Redact patient data, proecting patient privacy and ensuring anonymity regarding medical scans.

- **Information Aggregation**: Collect extracted information, including patient names, dates, times, hospital details, filter values, sequence numbers, and more.

- **Data Correction**: Utilize autocorrection techniques to enhance the accuracy of extracted data, including spelling corrections for names and other textual information.

- **CSV Generation**: Create a comprehensive CSV file that aggregates the extracted information, making it easy to analyze and visualize the data.


## Installation

To run this project, you'll need to have Python installed on your system. You can follow the steps below to set up and run the project:

1. Clone the repository to your local machine:
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Install the required Python libraries and dependencies using `pip`:
    pip install -r requirements.txt

   This will install the necessary packages specified in the `requirements.txt` file.

4. Download the spaCy language model by running:

   python -m spacy download en_core_web_sm

## Usage

To process images and extract information using this tool, follow these steps:

1. Place your input images in the `input_images` directory.

2. Run the main processing script:
   python process_images.py

   This script performs the following steps:
   
   - Removes the background and keeps only text from the images.
   - Extracts text from the processed images.
   - Removes text from the original input images.
   - Aggregates extracted information into a CSV file.

3. After running the script, you'll find the results in the following directories:
   - Processed images with removed text: `output_images_noText`
   - Extracted text files: `output_text`
   - Preprocessed images with removed background: `output_images_noBackground`
   - Aggregated CSV file: `output_csv/aggregated_data.csv`

## Example
A sample image has been provided for users to see how MedDataExtractor works
![Angiography Scan Analysis](images/angiography sample.jpg)


## Acknowledgments

This project uses the following libraries and tools:
- spaCy for named entity recognition
- OpenCV for image processing
- pytesseract for text extraction from images
- mmocr for text detection
- extcolors for color extraction
- autocorrect for text spell checking
