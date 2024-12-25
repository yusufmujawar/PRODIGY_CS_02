# Python code for Image Encryption & Decryption Pixel Manipulation Technique
from PIL import Image
import os

print()
print('***** Welcome to Image Pixel Manipulation Encryption Technique *****')
print('                 *** Build By Mohamed Yusuf Mujawar ***               ')
print()

# Take path of image as input so user can choose image file
path = r'D:\Internship\Prodigy Infotech_Internship_Report\PD_CS_02\Encrypt & Decrypt Technique_Prodigy Infotech_Image Test.png'
print()

# Take encryption key as input so user can enter key
try:
    key = int(input("Enter the key for encryption: "))
except ValueError:
    print("Invalid Key Entered. Please Enter a Numeric Key.")
    exit()

# Print path of image file and encryption key so user can see the path and key
print("Path of the image file: ", path)
print()
print("Key for encryption is: ", key)

# Open image file in read mode
with open(path, 'rb') as fin:
    # Storing image data in image variable
    image = fin.read()
    fin.close()

# Convert image data in byte array
# Perform bitwise XOR operation on each value of byte array with encryption key
image = bytearray(image)

for index, values in enumerate(image):
    image[index] = values ^ key

# Open image file in write mode
with open(path, 'wb') as fout:
    # Write encrypted data in image file
    fout.write(image)
    fout.close()
print()
print("Encryption Done...Task Completed...")
print()
