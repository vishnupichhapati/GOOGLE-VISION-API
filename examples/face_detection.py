import argparse
import io
import streamlit
from google.cloud import vision
from google.cloud.vision import types
image_file = st.file_uploader("Choose an imamge file")
def main(image_file):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    
    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.face_detection(image=image)
    labels = response.face_annotations
    for label in labels:
        print('Joy Likelihood: {}'.format(label.joy_likelihood))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    st.image(main(args.image_file))
