import argparse
import os.path

from PIL import Image


def image_manipulation(args):
    for file in args.input:
        name, ext = os.path.splitext(file)
        with Image.open(file) as image:
            width, height = image.size
            
            if args.square:
                square_dim = max(width, height)
                canvas = Image.new('RGBA', (square_dim, square_dim), (255, 255, 255, 0))
                canvas.paste(image, (square_dim // 2 - width // 2, square_dim // 2 - height // 2))
                image = canvas

            if args.dims:
                image = image.resize((args.dims[0], args.dims[1]))
            image.save(name + "." + args.format, format=args.format, dpi=(args.dpi, args.dpi))


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            description='Provides basic image manipulation suitable for scripting.')
        parser.add_argument('-i', '--input', type=str, nargs='+', dest="input",
                            required=True, help="The list of filenames that we want to convert.")
        parser.add_argument('-s', '--square', action='store_true',
                            help="Squares up the image canvas based on maximum dimension.")
        parser.add_argument('-d', '--dims', type=int, nargs=2,
                            help="The width and height of the output image.")
        parser.add_argument('--dpi', type=int, default=150,
                            help="The desired DPI for the output image.")
        parser.add_argument('-f', '--format', dest='format', choices=['png', 'jpeg'],
                            help="The output format to use", default="png")

        image_manipulation(parser.parse_args())
    except KeyboardInterrupt:
        print("Received keyboard interrupt. Stopping execution.")
    except Exception as e:
        print(e)
