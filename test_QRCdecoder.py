# Import Library
import streamlit as st
import cv2


filename = "C:\\Users\\aforr\\Thonny\\MM\\image_folder\\generate_image_20240629-113327.png"

# read the QRCODE image
image = cv2.imread(filename)

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# detect and decode
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

# if there is a QR code
# print the data
if vertices_array is not None:
  st.write("QRCode data:")
  st.write(data)
else:
  st.write("There was some error")
