#Identifying text in the image
def text_detector(file_name):
    from PIL import Image
    import pytesseract
    im=Image.open(file_name)
    text=pytesseract.image_to_string(im, lang='eng')
    return text