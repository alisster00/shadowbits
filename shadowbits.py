import argparse
from PIL import Image

def text_to_bin(text):
    return ''.join(format(ord(c), '08b') for c in text) + '00000000'

def bin_to_text(binary):
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if byte == '00000000':
            break
        text += chr(int(byte, 2))
    return text

def hide_message(input_image, output_image, message):
    img = Image.open(input_image).convert("RGB")
    pixels = list(img.get_flattened_data())

    binary = text_to_bin(message)
    if len(binary) > len(pixels) * 3:
        raise ValueError("The message is too large for this image")

    idx = 0 
    mod_pixels = []

    for r, g, b in pixels:
        if idx < len(binary):
            r = (r & ~1) | int(binary[idx]); idx += 1
        
        if idx < len(binary):
            g = (g & ~1) | int(binary[idx]); idx += 1

        if idx < len(binary):
            b = (b & ~1) | int(binary[idx]); idx += 1

        mod_pixels.append((r, g, b))

    img.putdata(mod_pixels)
    img.save(output_image)

def extract_message(image):
    img = Image.open(image).convert("RGB")
    pixels = list(img.get_flattened_data())

    binary_msg = ""
    for r, g, b in pixels:
            binary_msg += str(r & 1)
            binary_msg += str(g & 1)
            binary_msg += str(b & 1)

    return bin_to_text(binary_msg)

def main():
    parser = argparse.ArgumentParser(
            description="LSB Steganography in PNG images"
            )
    subparsers = parser.add_subparsers(dest="mode", required=True)

    hide = subparsers.add_parser("H", help="Hide text in an image")
    hide.add_argument("-i", "--input", required=True, help="Input image (PNG)")
    hide.add_argument("-o", "--output", required=True, help="Output image")
    hide.add_argument("-m", "--message", required=True, help="Message to hide")

    extract = subparsers.add_parser("E", help="Extraer hidden text")
    extract.add_argument("-i", "--input", required=True, help="Image with hidden message")

    args = parser.parse_args()

    if args.mode == "H":
        hide_message(args.input, args.output, args.message)
        print(f"Menssage hidden successfully")

    elif args.mode == "E":
        message = extract_message(args.input)
        print("Extracted message:")
        print(message)

if __name__ == "__main__":
    main()
