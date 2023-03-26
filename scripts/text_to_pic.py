from PIL import Image, ImageDraw, ImageFont

# Set up the dimensions of the image and the background color
width = 640
height = 427
background_color = (255, 255, 255)  # white

# Create a new image with the given dimensions and background color
image = Image.new('RGB', (width, height), background_color)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Set the font and size of the text
font_size = 50
font = ImageFont.truetype('../assets/rozha_one.ttf', font_size)

# Set the text to be displayed
text = input("Enter quote for image: ")
if not text:
    text = 'Hello, world!'

# Get the size of the text box or the length of the text
text_box = draw.textbbox((0, 0), text, font=font)
text_length = draw.textlength(text, font=font)

# Determine the position of the text on the image
x = (width - text_box[2]) // 2
y = (height - text_box[3]) // 2

# Draw the text on the image
draw.text((x, y), text, font=font, fill=(180, 180, 180))  # black

# Save the image as a JPEG file
image.save('../testData/text_image.jpg', 'JPEG')

