from PIL import Image


def get_image_resolution(image_path):
    try:
        # Open the image using Pillow
        img = Image.open(image_path)

        # Get the width and height of the image
        width, height = img.size

        return width, height
    except Exception as e:
        return None


# Provide the path to your image file
image_path = "/llm-hackathon-service/2955-1n_1.jpeg"
resolution = get_image_resolution(image_path)

print("provided image is:",image_path)
if resolution:
    print(f"Image resolution: {resolution[0]}x{resolution[1]} pixels")
else:
    print("Unable to determine the image resolution.")
