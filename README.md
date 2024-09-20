## QR Code Generator Script

This Python script generates a QR code for the provided URL and saves it as "some_file.png".

### Requirements

- Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
- qrcode library (installation instructions below)

### Installation

1. **Install Python 3:**
   Download and install Python 3 from the official website if you haven't already.

2. **Install the qrcode library:**
   Open a terminal or command prompt and run the following command:

   ```bash
   pip3 install qrcode
   ```

   - Detailed outline provided here https://pypi.org/project/qrcode/

3. **Swap out the**
   Swap out line 2 URL for your weblink you desire

   ```
   img = qrcode.make('https://main.d3vianaxlv4x9d.amplifyapp.com/')
   ```

4. **Run your code**

   ```
   python3 qr.py
   ```

   You should now see a png file generated in your documents folder "QRCODE_GENERATOR".

5. Share with friends and enjoy the results

_Resources: https://pypi.org/project/qrcode/_
