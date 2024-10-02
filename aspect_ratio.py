import cv2
import os

# To resize image to a given aspect ratio
def aspect_ratio_testing(image_path, aspect_ratio=(16, 9)):
    original_image = cv2.imread(image_path)
    height, width = original_image.shape[:2]

    # Calculate new dimensions
    new_width = width
    new_height = int(new_width * aspect_ratio[1] / aspect_ratio[0])
    resized_image = cv2.resize(original_image, (new_width, new_height))

    output_path = f"aspect_ratio_images/{os.path.basename(image_path)}"
    cv2.imwrite(output_path, resized_image)
    print(f"Aspect ratio changed image saved at: {output_path}")


os.makedirs('aspect_ratio_images', exist_ok=True)


image_path = "D:/New folder/avataar_assignment/2_nocrop.png"
#aspect_ratio_testing(image_path, aspect_ratio=(1, 1)) (output saved as 2_nocrop copy for 1:1 ratio)

aspect_ratio_testing(image_path, aspect_ratio=(16, 9))


