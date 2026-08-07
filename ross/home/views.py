from django.shortcuts import render
from pyfiglet import FigletFont

from .t2a import textoa, code, COLORS
from .img2a import imgtoa 

def index(request):

    fonts = FigletFont.getFonts()
    colors = list(COLORS.keys())

    text_result = ""
    code_result = ""
    image_result = ""
    selected_color = "black"   # default

    if request.method == "POST":

        action = request.POST.get("action")

        if action == "text":

            text = request.POST.get("text")
            font = request.POST.get("font")
            selected_color = request.POST.get("color")

            text_result = textoa(text, font, selected_color)
            code_result = code(text, font, selected_color)

        elif action == "image":
            image = request.FILES.get("image")
            mode = request.POST.get("mode")

            if image:
                image_result = imgtoa(image, mode)
                
    return render(request, "home/index.html", {
        "fonts": fonts,
        "colors": colors,
        "text_result": text_result,
        "code_result": code_result,
        "image_result": image_result,
        "selected_color": selected_color,
    })