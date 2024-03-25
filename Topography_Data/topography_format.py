import numpy as np

from pprint import pprint

def create_topography_array_wrong():
    # Specify the file path
    file_path = "binary_image.txt"
    # Read data from the file
    with open(file_path, "r") as file:
        data = [list(map(int, line.strip())) for line in file]

    # Convert the list of lists to a NumPy array
    array_2d = np.array(data)

    array_2d[array_2d == 1] = 25

    # Display the resulting array
    print(array_2d)

    # Specify the file path
    output_file_path = "topography_output.txt"

    # Save the array to the text file
    np.savetxt(output_file_path, array_2d, fmt='%d', delimiter=' ')

    return array_2d

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def parse_text_to_array(text_content):
    rows = text_content.strip().split('\n')

    # Padding rows with zeros
    rows_padded = [list(map(int, row.split())) + [0] * (100 - len(row.split())) for row in rows]

    # Transpose the matrix to work on columns
    cols_padded = list(map(list, zip(*rows_padded)))

    # Padding columns with zeros
    cols_padded = [col + [0] * (100 - len(col)) for col in cols_padded]

    # Transpose the matrix back to the original orientation
    result_array = list(map(list, zip(*cols_padded)))

    return result_array

def create_topography_array():
# Example usage
    file_path = 'topography_output.txt'
    text_content = read_text_file(file_path)
    result_array = parse_text_to_array(text_content)

    pprint(result_array)

    # Now, result_array contains the 2D array with the specified conditions

    output_file_path = "topography_array_output.csv"

    # Save the array to the text file
    np.savetxt(output_file_path, result_array, fmt='%d', delimiter=' ')

    return result_array

# FORMAT CSV TOPOGRAPHY FILE
with open('topography_array_output.csv', 'r') as file:
    lines = file.readlines()

with open('topography_array_output_with_commas.csv', 'w') as new_file:
    for line in lines:
        # Remove leading and trailing whitespaces
        line = line.strip()
        # Split values by space
        values = line.split(' ')
        # Join values with commas
        new_line = ','.join(values)
        # Write the new line to the new file
        new_file.write(new_line + '\n')