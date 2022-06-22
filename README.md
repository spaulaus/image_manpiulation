# Image Manipulator
Image manipulator using python and pillow. Focused on squaring up images and resizing them. 

## Usage
```
usage: image_manipulation.py [-h] -i INPUT [INPUT ...] [-s] [-d DIMS DIMS]
                             [--dpi DPI] [-f {png,jpeg}]

Provides basic image manipulation suitable for scripting.

options:
  -h, --help            show this help message and exit
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        The list of filenames that we want to convert.
  -s, --square          Squares up the image canvas based on maximum
                        dimension.
  -d DIMS DIMS, --dims DIMS DIMS
                        The width and height of the output image.
  --dpi DPI             The desired DPI for the output image.
  -f {png,jpeg}, --format {png,jpeg}
                        The output format to use
```
