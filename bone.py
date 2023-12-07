import cv2
from PIL import Image

def process_image(image_path):
    # Indlæs billedet
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Anvend Canny-kantdetektion
    edges = cv2.Canny(image, 100, 200)

    # Gem det bearbejdede billede
    processed_image_path = 'processed_image.png'
    cv2.imwrite(processed_image_path, edges)

    # Vis det oprindelige og det bearbejdede billede
    original = Image.open(image_path)
    processed = Image.open(processed_image_path)

    original.show(title="Original Image")
    processed.show(title="Processed Image")

# Brug funktionen med stien til dit røntgenbillede
process_image('hand-x-ray.jpg')
