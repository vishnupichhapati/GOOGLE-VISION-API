import argparse
import io
from io import BytesIO
from PIL import Image
from PIL import ImageDraw
import json
import streamlit as st
from google.cloud import vision
from google.cloud.vision import types
image_file =  st.file_uploader("Upload Images (less than 1mb)", type=["png","jpg","jpeg"])
img = Image.open(image_file)
st.image(image_file,width=250,caption='Uploaded image')
byte_io = BytesIO()
img.save(byte_io, 'BYTES')#PNG
imag = byte_io.getvalue()
button=st.button('Click me',help='To give the image')
if image_file and button:
    def main(image_file):
    # Instantiates a client
        client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    
        content = Image.open(BytesIO(imag))

        image = types.Image(content=content)

    # Performs label detection on the image file
        response = client.face_detection(image=image)
        labels = response.face_annotations
        for label in labels:
            print('Joy Likelihood: {}'.format(label.joy_likelihood))

    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('-image_file', help='The image you\'d like to label.')
        args = parser.parse_args()
        st.text(main(args.image_file))
