# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:35:15 2021

@author: MathiyalaganN
"""

def dimensions(filename):
    """Determine the dimensions in pixels of a BMP image.


    Args:
        filename: The filename of a BMP file.


    Returns:
        A tuple containing two integers with the width
        and height in pixels.


    Raises:
        ValueError: If the file was not a BMP file.
        OSError: If there was a problem reading the file.
    """


    with open(filename, 'rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError("{} is not a BMP file".format(filename))


        f.seek(18)
        width_bytes = f.read(4)
        height_bytes = f.read(4)


        return (_bytes_to_int32(width_bytes),
                _bytes_to_int32(height_bytes))




def _bytes_to_int32(b):
    "Convert a bytes object containing four bytes into an integer."
    return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)

print(dimensions('/Users/MathiyalaganN/Downloads/sample1.bmp'))







