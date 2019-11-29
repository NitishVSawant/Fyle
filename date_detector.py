#Extract date from image
def data_detector(text):
    import re
    pattern1=re.compile(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s?\d{2}.\s?\d{2,4}')
    pattern2=re.compile(r'\d{1,2}.(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s?.\s?\d{2,4}')
    pattern3=re.compile(r'\d{1,4}\s?(-|/|\.)\s?\d{1,2}\s?(-|/|\.)\s?\d{2,4}')
    pattern4=re.compile(r'\d{1,4}\s?(-|/|\.)\s?\w{1,3}\s?(-|/|\.)\s?\d{2,4}')
    pattern5=re.compile(r'[0-3]?\d\s?(-|/)\s?[0-3]?\d\s?')
    patterns=[pattern1,pattern2,pattern3,pattern4,pattern5]
    match=None
    print('Dates found in the image:')
    for i in patterns:
        for match in re.finditer(i,text):
            print('\t'+match.group())
        if match is None:
            continue
        else:
            break
    if match is None:
        print('\tNo dates found in image')