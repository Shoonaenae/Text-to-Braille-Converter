
from PIL import Image

from PIL import Image, ImageDraw, ImageFont





braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵', ' ': '⠀', '.': '⠲', ',': '⠂',
    '?': '⠦', '!': '⠖', "'": '⠄', '-': '⠤', '(': '⠐⠣', ')': '⠐⠜'
}

def text_to_braille(text):
    braille = ""
    for char in text:
        if char.lower() in braille_dict:
            braille += braille_dict[char.lower()]
        else:
            braille += char
    return braille

def braille_to_image(braille):
    # Define braille image properties
    width = 1000
    height = 1000
    background_color = (255, 255, 255)
    text_color = (0, 0, 0)
    font_size = 60
    cell_width = 40
    cell_height = 80
    
    # Create an image
    image = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(image)
    
    # Define the braille font
    braille_font = ImageFont.truetype('C:/Users/kash/Downloads/freemono/FreeMono.ttf', font_size)

    # Draw the braille text on the image
    x = 10
    y = 10
    for char in braille:
        if char == '⠀':  # Space character
            x += cell_width
        else:
            draw.text((x, y), char, font=braille_font, fill=text_color)
            x += cell_width
        if x >= width - cell_width:  # Move to the next line
            x = 10
            y += cell_height
    
    # Save the image
    image.save('C:/Users/kash/Documents/GitHub/Text-to-Braille-Converter/thesis/static/images/braille_image.png', 'PNG', encoding='utf-8')
