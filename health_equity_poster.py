from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import qrcode

# Configuration
title = "Health Equity Research on Hepatitis B Care in Ghana"
width = 10800  # 36 inches at 300 DPI
height = 14400  # 48 inches at 300 DPI

# Create a blank poster image
poster = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(poster)

# Load fonts
try:
    title_font = ImageFont.truetype('arial.ttf', 120)  # Adjust size as needed
    content_font = ImageFont.truetype('arial.ttf', 80)
except IOError:
    title_font = ImageFont.load_default()
    content_font = ImageFont.load_default()

# Draw the title
text_width, text_height = draw.textsize(title, font=title_font)
draw.text(((width - text_width) / 2, 100), title, font=title_font, fill='black')

# Draw the three columns of text
content = [
    "Column 1 Content: Overview of Hepatitis B in Ghana.",
    "Column 2 Content: Current statistics and healthcare approaches.",
    "Column 3 Content: Recommendations for improving care and outreach."
]

column_width = width // 3
for i, text in enumerate(content):
    draw.text((i * column_width + 50, 300), text, font=content_font, fill='black')  # Columns start below title

# Add placeholder images
image_placeholder_size = (200, 200)
for i in range(3):
    draw.rectangle([i * column_width + 50, 700,  
                    i * column_width + 50 + image_placeholder_size[0], 
                    700 + image_placeholder_size[1]],
                    outline='black', fill='lightgray')
    draw.text((i * column_width + 50 + 60, 700 + 80), "Image Placeholder", font=content_font, fill='black')

# Generate a QR code
qr_data = "https://example.com"
qr_img = qrcode.make(qr_data)
qr_img = qr_img.resize((250, 250))  # Resize QR code

# Paste the QR code on the poster
poster.paste(qr_img, (width - 300, height - 300))

# Save as PDF and PNG
poster.save('health_equity_poster.png')
poster.save('health_equity_poster.pdf')

# Display the poster
plt.imshow(poster)
plt.axis('off')  # Hide the axis
plt.show()