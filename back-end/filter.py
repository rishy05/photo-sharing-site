from PIL import Image, ImageDraw

# Open an image file
image_path = r"D:\photo_sharing\back-end\people\sai.jpg"
image = Image.open(image_path)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define the coordinates of the points you want to keep
point_coordinates = [(71.83786, 882.4004), (206.26532, 834.6223)]

# Set the color and size for the points
point_color = (255, 0, 0)  # Red color
point_size = 5

# Draw points on the image
for point in point_coordinates:
    draw.ellipse(
        [
            point[0] - point_size,
            point[1] - point_size,
            point[0] + point_size,
            point[1] + point_size,
        ],
        fill=point_color,
        outline=point_color,
    )

# Save or display the modified image
image.show()


left_eye = (206.26532, 834.6223)
right_eye = (71.83786, 882.4004)
