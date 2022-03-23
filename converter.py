import argparse
import os

from PIL import Image


def get_desktop_path():
    if os.name == 'nt':
        return 'C:\\Users\\' + os.getlogin() + '\\Desktop\\'
    else:
        return '/home/' + os.getlogin() + '/Desktop/'


def main():

    parser = argparse.ArgumentParser(
        description='Convert an image to a pdf file.')
    parser.add_argument('-image', help='The image to be converted.')
    parser.add_argument('-output', help='The output file name.')

    args = parser.parse_args()

    if not args.image and not args.output:
        parser.print_help()
        exit()

    if args.output:
        output = args.output
    else:
        output = get_desktop_path()

    try:
        image = Image.open(args.image)
        filename = image.filename.replace(
            image.format.lower(), 'pdf').split('\\')[-1]

        if not os.path.isfile(image.filename):
            print('[!] Error: Image not found.')
            exit()

        if not os.path.isdir(os.path.dirname(output)):
            print('[!] Error: Output directory not found.')
            exit()

        if os.path.isfile(output+filename):
            print('[!] Error: Output file already exists.')
            exit()

        if image.format == 'JPEG' or image.format == 'PNG' or image.format == 'GIF' or image.format == 'BMP' or image.format == 'TIFF':
            image.save(output + filename, resolution=100.0)
    except Exception as e:
        print('[!] Error: ' + str(e))
        exit()


if __name__ == '__main__':
    main()