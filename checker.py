import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('images/clear.jpg', detail=0)
print(result)
