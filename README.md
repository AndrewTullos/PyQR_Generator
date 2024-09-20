# QR Code Generator

This is a simple Python script that generates a QR code from user input. The generated QR code can encode any text or URL provided and will be saved as an image file.

## Features

- User-friendly command-line interface.
- Customizable QR code with a blue background and black foreground.
- Save the generated QR code as an image file.

## Requirements

- Python 3.x
- `qrcode` module

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Navigate to the project directory:
   ```
   cd your-repo-name
   ```
3. Install the required package:
   ```
   pip install qrcode[pil]
   ```

## Usage

1. Run the script:
   ```
   bash
   Copy code
   python qr_code_generator.py
   ```
2. When prompted, enter the text or URL you want to encode in the QR code.

3. Enter the desired filename for the QR code image (e.g., my_qrcode.png).

4. The QR code will be generated and saved as an image file in the project directory.

## Example

```
Enter text or URL: https://github.com
Enter your filename: my_qrcode.png
QR code saved as my_qrcode.png
```

## Notes

- Make sure to include the file extension (.png, .jpg, etc.) when providing the filename.

- The QR code is generated with a blue background and black foreground by default. You can modify the colors in the script.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
