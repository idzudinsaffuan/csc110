"""CSC110 Fall 2026 Assignment 1, Part 3: Working with Image Data

Instructions (READ THIS FIRST!)
===============================

Please follow the instructions in the assignment handout to complete this file.

You are required to add doctest examples for crop_image, but not other functions.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team
"""

import a1_part2
import a1_helpers

# This constant represents a 4-by-4 pixel grid. We have provided it to help
# with testing your work for this part.
EXAMPLE_PIXEL_GRID = [
    [[128, 128, 128], [35, 50, 65], [210, 32, 68], [32, 208, 43]],
    [[130, 20, 42], [43, 44, 45], [17, 243, 82], [61, 85, 92]],
    [[201, 23, 23], [23, 23, 23], [42, 180, 19], [16, 58, 29]],
    [[1, 52, 128], [26, 123, 128], [71, 234, 82], [23, 108, 34]],
]


###################################################################################################
# 0. Warmup
###################################################################################################
def warmup2() -> list:
    """Read an image file and return a list of colour rows (lists of RGB lists).

    This illustrates the use of the helper function load_image_pixels that we have provided you.
    """
    # This refers to a file called 'spiderman.png' inside the 'images' folder.
    example_image_data = a1_helpers.load_image_pixels('assignments/a1/images/spiderman.png')

    # Display the pixels as squares in a pygame window
    a1_helpers.show_colour_rows_pygame(example_image_data)

    # Return the data (helpful for testing in this part of the assignment)
    return example_image_data


###################################################################################################
# 1. EXAMPLE CODE: Transforming multiple colour rows (Examples only, not for credit)
# The following functions have all been completed for you. Do NOT modify any of the functions in this
# section. They rely on the functions you wrote in a1_part2 and will only work correctly if you
# have completed those functions.
###################################################################################################


def remove_red_in_image(image_data: list) -> list:
    """Return new image data with the same pixels as image_data, except each colour has its "red" value changed to 0.

    You may ASSUME that:
    - image_data is a list of valid colour rows of the same length (possibly empty)
    """
    return [a1_part2.remove_red_in_row(colour_row) for colour_row in image_data]


def greyscale_image(image_data: list) -> list:
    """Return new image data with the same pixels as image_data, except each colour
    is replaced with its greyscale version.

    You may ASSUME that:
    - image_data is a list of valid colour rows of the same length (possibly empty)
    """
    return [a1_part2.greyscale(colour_row) for colour_row in image_data]


def pixelate_rows_in_image(image_data: list, block_size: int) -> list:
    """Return new image data where each row has been pixelated in the same
    process described in a1_part2.pixelate_row.

    You may ASSUME that:
    - image_data is a list of valid colour rows of the same length (possibly empty)
    - block_size > 0
    - the length of every row of image_data can be divided evenly by block_size
    """
    return [a1_part2.pixelate_row(colour_row, block_size) for colour_row in image_data]


def crop_rows_in_image(image_data: list, start: int, num_colours: int) -> list:
    """Return new image data where each colour row has been cropped in the same way as described
    in a1_part2.crop_row.

    Notes:
    1. start is the index of the first colour to take from each colour row.
    2. num_colours specifies the number of colours to take from each colour row.

    You may ASSUME that:
    - image_data is a list of valid colour rows of the same length (possibly empty)
    - start >= 0
    - num_colours >= 0
    - image_data == [] or start + num_colours <= len(image_data[0])
    """
    return [a1_part2.crop_row(colour_row, start, num_colours) for colour_row in image_data]


###################################################################################################
# 2. Cropping
###################################################################################################


def crop_image(
    image_data: list, start_row: int, start_col: int, crop_height: int, crop_width: int
) -> list:
    """Return a cropped version of image_data.

    Notes:
    1. start_row is the index of the first colour row to take from image_data
    2. crop_height is the number of rows to take from image_data
    3. start_col is the index of the first colour to take from each colour row
    4. crop_width is the number of colours to take from each colour row
    5. If crop_height is 0, return []. If crop_width is 0, return crop_height empty rows.

    You may ASSUME that:
    - image_data is non-empty
    - every element of image_data is a valid colour row with the same length
    - start_row >= 0
    - start_col >= 0
    - crop_height >= 0
    - crop_width >= 0
    - start_row + crop_height <= len(image_data)
    - start_col + crop_width <= len(image_data[0])

    >>> EXAMPLE_PIXEL_GRID = [
    ... [[128, 128, 128], [35, 50, 65], [210, 32, 68], [32, 208, 43]],
    ... [[130, 20, 42], [43, 44, 45], [17, 243, 82], [61, 85, 92]],
    ... [[201, 23, 23], [23, 23, 23], [42, 180, 19], [16, 58, 29]],
    ... [[1, 52, 128], [26, 123, 128], [71, 234, 82], [23, 108, 34]]
    ... ]
    >>> crop_image(EXAMPLE_PIXEL_GRID, 1, 1, 2, 2)
    [[[43, 44, 45], [17, 243, 82]], [[23, 23, 23], [42, 180, 19]]]
    >>> crop_image(EXAMPLE_PIXEL_GRID, 1, 1, 0, 2)
    []
    >>> crop_image(EXAMPLE_PIXEL_GRID, 1, 1, 2, 0)
    [[], []]


    """

    cropped_rows = [image_data[x] for x in range(start_row, start_row + crop_height)]
    if crop_width > 0:
        ungrouped = [row[x] for row in cropped_rows
                     for x in range(start_col, start_col + crop_width)]
        grouped = [[ungrouped[x] for x in range(n * crop_width, (n + 1) * crop_width)]
                   for n in range(0, len(ungrouped) // crop_width)]
        return grouped
    else:
        return [[] for i in range(crop_height)]

###################################################################################################
# EXAMPLE: Image transformation (exploration only, not for credit)
###################################################################################################


def transform_image(input_file_path: str, output_file_path: str) -> None:
    """Perform a series of transformations on the given input file image and save the result to the output_file_path.

    We have provided some sample function calls using the functions from this file. Feel free to try these out
    by uncommenting them and adding your own.

    Here is an example call for this function:

        transform_image('assignments/a1/images/sadias_zoo.jpg', 'assignments/a1/images/new_sadias_zoo_modified.jpg')
    """
    original_image_data = a1_helpers.load_image_pixels(input_file_path)

    # The sample arguments below are for sadias_zoo.jpg. For other images, choose
    # a block size that divides the image width and crop bounds within the image.
    # Keep at least one row and one column when saving an image.
    # You can comment out this line and switch it with one of the lines below
    # new_image_data = original_image_data
    # new_image_data = remove_red_in_image(original_image_data)
    # new_image_data = greyscale_image(original_image_data)
    # new_image_data = pixelate_rows_in_image(original_image_data, 16)
    # new_image_data = crop_rows_in_image(original_image_data, 30, 10)
    new_image_data = crop_image(original_image_data, 565, 500, 250, 200)

    a1_helpers.save_image(output_file_path, new_image_data)


###################################################################################################
# "Main block" (we'll discuss what this means in lecture)
###################################################################################################
if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['a1_part2', 'a1_helpers'],
        'max-line-length': 120,
        'disallowed-python-syntax': ['For', 'While', 'Slice']
    })

    transform_image('assignments/a1/images/sadias_zoo.jpg', 'assignments/a1/images/new_sadias_zoo_modified.jpg')

# warmup2()
