# Simple PDF Converter

Tired of having to convert images to PDFs using web services and not knowing what happend to your files, if their really deleting after X time or something else like that? Why don't you try to do it on your localhost?

Already supports: 'JPEG', 'PNG', 'GIF', 'BMP', 'TIFF' formats.

## Dependencies

* [Python 3.6+](https://www.python.org/downloads/)

## Instalation

Unix Based Systems:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows:
```bash
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
```bash
python converter.py [-h] [-image IMAGE] [-output OUTPUT]

Convert an image to a pdf file.

optional arguments:
  -h, --help      show this help message and exit
  -image IMAGE    The image to be converted.
  -output OUTPUT  The output file name.
```
