from whaaaaat import prompt, print_json, Separator
# body2 = {1:"eyes",2:"boots",3:"clothes",4:"legs",5:"hair"}
import requests
import json
import urllib
import os
# from ipycanvas import Canvas
# from tkinter import *
# from PIL import Image, ImageGrab


questions = [
    {
        "type": "list",
        "name": "sex",
        "message": "What type of character do you want?",
        "choices": ["male", "female"],
    },
    {
        "type": "list",
        "name": "eyes",
        "message": "What color eyes do you want?",
        "choices": ["blue", "brown", "gray", "green"],
    },
    {
        "type": "list",
        "name": "shoes",
        "message": "What color shoes do you want?",
        "choices": ["boots_black1", "boots_brown1"],
    },
    {
        "type": "list",
        "name": "clothes",
        "message": "What type of clothes (top) do you want?",
        "choices": ["longsleeve_white", ],
    },
    {
        "type": "list",
        "name": "legs",
        "message": "What color pants do you want?",
        "choices": ["pants_black_L"]
    },
    {
        "type": "list",
        "name": "hair",
        "message": "What kind of hair do you want?",
        "choices": ["idol_brown"],
    },
]


a =  prompt(questions)

print_json(a)





# url = 'https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/#'





url_call = 'https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/#?sex={0}&eyes={1}&shoes={2}&clothes={3}&legs={4}&hair={5}'.format(
  a['sex'],a['eyes'],a['shoes'],a['clothes'],a['legs'],a['hair'])
r = requests.get(url_call)

# rr = json.loads(r.content)
# print(rr)


# canvas = Canvas(width=832, height=1344, sync_image_data=True)
# # Perform some drawings...
# canvas.to_file('sprite.png')
# https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/#?eyes=blue&shoes=boots_black1&clothes=longsleeve_white&legs=Pants_black_L&hair=idol_brown