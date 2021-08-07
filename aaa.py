import base64
from PIL import Image
from io import BytesIO
import io

with open("Input/img_11.jpg", "rb") as image_file:
    data = base64.b64encode(image_file.read())
print(data)
# a = '/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/wAALCAAcABwBAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/APn+vTPDHwP8TeJ9DtdXiuLCzt7kbo0uWcOU7NgKRgjkc81i+O/hvrPgW8xco1zp7ELHfIm1HYqCRjJIPUc9cHFcbSgEnABJ9BXaafH8Rrrw3NpdjBrkmjohLQLE/l7c5OOPUHgV6Fcw3um/sxXNt4hZo7qW5X7FDdLtlRfOU7QG5zgSH/dPpXhFel/Bzxj4a8H6vfzeILZy86ILe6WLzPI27i3HUZ+XkA9PQ16Pc/Hfw7pM91LaXusa20wDRxSQRQww9eAdob35DfWuNg+Ny67Dfab430SDUNLuQxjW2UK8BwcAZPPOPmyCOvPSvH6KKKK//9k='
# base64bytes = base64.b64decode(a)
# bytesObj = io.BytesIO(base64bytes)
# bytesObj.seek(0)
# b = a.encode('utf-8')
# img = Image.open(BytesIO(base64.b64decode(b)))
# im = Image.open(BytesIO(base64.b64decode(data)))
# im.save('image1.png', 'PNG')
# payload = {
#     "mime" : "image/jpg",
#     "image": encoded_image_string,
#     "some_other_data": None
# }

# response = requests.put("[http://0.0.0.0:80/predict](http://0.0.0.0:80/predict)", data=payload)

# pred = response.json