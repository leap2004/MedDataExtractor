import cv2
import pytesseract

class TextExtractor:
    def __init__(self, output_text_path, output_csv_path):
        self.output_text_path = output_text_path
        self.output_csv_path = output_csv_path

    def text_extract(self, input_image_path):
        for filename in os.listdir(input_image_path):
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.jpeg'):
                input_file_path = os.path.join(input_image_path, filename)
                image = cv2.imread(input_file_path)

                # Four quadrants
                height, width, _ = image.shape
                mid_x = width // 2
                mid_y = height // 2

                quadrants = {
                    'top_left': image[:mid_y, :mid_x],
                    'top_right': image[:mid_y, mid_x:],
                    'bottom_left': image[mid_y:, :mid_x],
                    'bottom_right': image[mid_y:, mid_x:]
                }

                extracted_text_list = []
                for quadrant, quadrant_image in quadrants.items():
                    data = pytesseract.image_to_string(quadrant_image, lang='eng', config='--psm 6')
                    data = data.replace('\u00ae', 'O')
                    extracted_text_list.append(f"Extracted Text ({quadrant}):")
                    extracted_text_list.append(data)

                    # Write the extracted text to the output file
                output_file_name_text = f"extracted_text_{filename}.txt"
                output_file_path_text = os.path.join(self.output_text_path, output_file_name_text)
                with open(output_file_path_text, 'w') as file:
                    file.write('\n\n'.join(extracted_text_list))

    def output_csv(self):
        spell = Speller()

        # Create a single CSV file for all aggregated information
        output_file_path_csv = os.path.join(self.output_csv_path, "aggregated_data.csv")
        with open(output_file_path_csv, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Add headers for dates, extract_terms, names, hospital, and Seq
            header_row = ['Name', 'Date', 'Time', 'Hospital', 'Filt', 'Seq'] + [f'{term}_Value' for term in extract_terms] + \
                         ['Mask', 'CRA', 'L Values', 'Tilt values', 'Resolution Values']
            csv_writer.writerow(header_row)

            for filename in os.listdir(self.output_text_path):
                if filename.lower().endswith('.txt'):
                    input_file_path = os.path.join(self.output_text_path, filename)

                    with open(input_file_path, 'r') as input_file:
                        extracted_text = input_file.read()
                        dates = extract_dates(extracted_text)
                        names = extract_most_likely_name(extracted_text)

                        if names is None or 'Li-' in names:
                            continue
                        correct_names = [spell(name) for name in [names]]
                        hosp_lines = extract_hosp(extracted_text)
                        correct_hosp = [spell(line) for line in hosp_lines]
                        seq_numbers = extract_seq(extracted_text)
                        filt_numbers = extract_filt(extracted_text)
                        mask_numbers = extract_mask(extracted_text)
                        CRA_numbers = extract_CRA(extracted_text)
                        L_values = extract_L(extracted_text)
                        tilt_values = extract_tilt(extracted_text)
                        time_values = extract_time(extracted_text)
                        resolution_values = extract_resolution(extracted_text)

                        for name in correct_names:
                            for date in dates:
                                for time in time_values:
                                    row_values = [name, date, time]

                                    row_values.append(' '.join(correct_hosp))
                                    row_values.append(' '.join(filt_numbers))
                                    row_values.append(' '.join(seq_numbers))

                                    for term in extract_terms:
                                        values = extract_values(extracted_text, term)
                                        row_values.append(values[0][1].strip('.').strip() if values else '')

                                    row_values.append(' '.join(mask_numbers))
                                    row_values.append(' '.join(CRA_numbers))
                                    row_values.append(' '.join(L_values))
                                    row_values.append(' '.join(tilt_values))
                                    row_values.append(' '.join(resolution_values))

                                    csv_writer.writerow(row_values)

        print("Aggregated CSV file created.")
