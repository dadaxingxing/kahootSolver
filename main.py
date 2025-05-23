import os
from dotenv import load_dotenv
import mss 
import mss.tools
import keyboard
import pyautogui
from PIL import Image
import openai
from PIL import Image
from io import BytesIO
import base64


load_dotenv()

API_key = os.getenv('API_KEY')
openai.api_key = API_key

def gpt_ans(question):
    pass

def click_button(ans):
    pass

def kahoot_bot():

    question_and_answers = {
        0: (0.0, 0.072, 1.0, 0.2),
        1: (0.042, 0.69, 0.458, 0.77),
        2: (0.54, 0.70, .94, 0.79),
        3: (0.042, 0.82, 0.458, 0.92),
        4: (0.54, 0.82, .94, 0.92),
    }



    # res = ''
    # with mss.mss() as sct:
        
    #     for key, value in question_and_answers.items():
            
    #         x1, y1, x2, y2 = int(value[0] * width), int(value[1] * height), int(value[2] * width), int(value[3] * height)
            

    #         # The screen part to capture
    #         monitor = {"top": y1, "left": x1, "width": x2 - x1, "height": y2 - y1}
    #         sct_img = sct.grab(monitor)

    #         # img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)



    #         # Save to the picture file

    width, height = pyautogui.size()
    # full screen monitor
    monitor = {"left": 0, "top": 0, "width": width, "height": height}
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        base64_img = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        # output = f"window_full.png"
        # mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)


keyboard.add_hotkey('alt+shift+t', kahoot_bot)
keyboard.wait()