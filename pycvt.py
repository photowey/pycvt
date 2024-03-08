import argparse
from PIL import Image


def resize_image(input_path, output_path, factor):
    image = Image.open(input_path)
    width, height = image.size
    new_width = int(width * factor) if factor > 0 else int(width / factor)
    new_height = int(height * factor) if factor > 0 else int(height / factor)

    resized_image = image.resize((abs(new_width), abs(new_height)))
    resized_image.save(output_path)
    print(f"Image resized successfully and saved to {output_path}")


if __name__ == "__main__":
    # $ pyinstaller --onefile pycvt.py

    parser = argparse.ArgumentParser(description="Image resize tool")
    parser.add_argument("-i", "--input", type=str, required=True, help="Input image path")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output image path")
    parser.add_argument("-f", "--factor", type=float, required=True, help="Factor by which to resize the image")
    args = parser.parse_args()

    resize_image(args.input, args.output, args.factor)
