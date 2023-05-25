
from PIL import Image

from PIL import Image, ImageDraw, ImageFont





def text_to_braille(text):
    braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵', ' ': '⠀', '.': '⠲', ',': '⠂',
    '?': '⠦', '!': '⠖', "'": '⠄', '-': '⠤', '(': '⠐⠣', ')': '⠐⠜'
    }
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
    font_size = 40
    cell_width = 40
    cell_height = 80
    
    # Create an image
    image = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(image)
    
    # Define the braille font
    braille_font = ImageFont.truetype('C:/Users/kash/Downloads/cash/thesis/freemono/FreeMono.ttf', font_size)

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


def translate_to_braille(text):
    # Define a dictionary to map Chinese characters to Braille patterns
    braille_dict = {
        '一': '⠁', '丁': '⠃', '七': '⠛', '三': '⠌', '上': '⠉', '下': '⠩', '不': '⠯', '中': '⠤', '九': '⠔', '了': '⠝',
        '二': '⠆', '十': '⠴', '人': '⠘', '入': '⠙', '八': '⠦', '六': '⠖', '冊': '⠜', '刀': '⠂', '力': '⠇', '口': '⠡',
        '匕': '⠢', '十': '⠴', '卜': '⠛', '卩': '⠶', '又': '⠽', '口': '⠡', '土': '⠭', '士': '⠱', '夂': '⠳', '大': '⠣',
        '女': '⠪', '子': '⠫', '寸': '⠩', '小': '⠹', '山': '⠵', '川': '⠲', '工': '⠐', '己': '⠔', '已': '⠻', '巾': '⠞',
        '幺': '⠯', '广': '⠪', '廴': '⠙', '弓': '⠳', '彑': '⠱', '彳': '⠫', '心': '⠥', '戈': '⠛', '手': '⠷', '支': '⠮',
        '攵': '⠢', '文': '⠫', '斗': '⠣', '斤': '⠊', '方': '⠷', '无': '⠰', '日': '⠈', '曰': '⠉', '月': '⠶', '木': '⠂',
        '欠': '⠲', '止': '⠾', '歹': '⠹', '殳': '⠱', '毋': '⠣', '比': '⠒', '毛': '⠤', '氏': '⠪', '气': '⠧', '水': '⠩',
        '火': '⠪', '爪': '⠻', '父': '⠜', '爻': '⠖', '片': '⠠', '牛': '⠣', '犬': '⠍', '王': '⠺', '元': '⠕', '井': '⠏',
        '玻': '⠃⠕⠃', '璃': '⠇⠊⠥', '電': '⠙⠑⠝⠋', '腦': '⠝⠁⠕⠕', '教': '⠚⠊⠕', '室': '⠑⠞⠓', '內': '⠝⠑⠑', '規': '⠛⠊⠊⠑', '定': '⠙⠊⠝⠭',
        '器': '⠟⠊⠗⠗', '此': '⠉⠎⠓', '飲': '⠟⠊⠝', '食': '⠟⠊⠅⠅', '錄': '⠟⠕⠇⠍', '影': '⠽⠑⠍⠑', '監': '⠑⠝⠁⠝', '視': '⠛⠊⠑⠊', '君': '⠚⠥⠍⠝',
        '子': '⠵⠎⠎', '自': '⠵⠊⠎', '重': '⠉⠗⠕', '男': '⠝⠃', '洗': '⠭⠅', '手': '⠰⠕', '間': '⠚⠁⠝',
       
    }

    # Convert each character in the text to its Braille equivalent
    braille = ""
    for char in text:
        if char in braille_dict:
            braille += braille_dict[char]
        else:
            braille += char
    return braille

