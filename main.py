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
    response = openai.ChatCompletion.create(
        model='gpt-4o',
        messages=[
            {
            'role': 'user',
            'content': [
                {
                    'type': 'text', 
                    'text': "You are a helpful assistant specialized in answering multiple-choice questions who only responds with the button number corresponding to the most likely answer do not respond with words only a integer. You'll do this even if the question involves content you can't analyze, such as videos or images. If you cannot answer the question, you'll respond with an educated guess. Remember only respond with an integer between 1 and 4 that corresponds to the answer."
                },
                {
                    'type': 'image_url', 
                    'image_url': {'url': question}
                }
            ]
            }
        ]
    )

    return response['choices'][0]['message']['content']

def click_button(ans, locations):
    width, height = pyautogui.size()
    x1, y1, x2, y2 = locations[ans]

    x, y = int((x2 - x1)/2 * width), int((y2 - y1) / 2 * height)
    pyautogui.click(x, y)

def kahoot_bot():

    question_and_answers = {
        0: (0.0, 0.072, 1.0, 0.2),
        1: (0.042, 0.69, 0.458, 0.77),
        2: (0.54, 0.70, .94, 0.79),
        3: (0.042, 0.82, 0.458, 0.92),
        4: (0.54, 0.82, .94, 0.92),
    }

    width, height = pyautogui.size()
    # full screen monitor
    monitor = {"left": 0, "top": 0, "width": width, "height": height}
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        base64_img = base64.b64encode(buffer.getvalue()).decode('utf-8')

        img_url = f'data:image/png;base64,{base64_img}'
    

    ans = gpt_ans(img_url)
    click_button(ans, question_and_answers)

    # res = ''
    # with mss.mss() as sct:
        
    #     for key, value in question_and_answers.items():
            
    #         x1, y1, x2, y2 = int(value[0] * width), int(value[1] * height), int(value[2] * width), int(value[3] * height)
            

    #         # The screen part to capture
    #         monitor = {"top": y1, "left": x1, "width": x2 - x1, "height": y2 - y1}
    #         sct_img = sct.grab(monitor)

    #         # img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
    #         # Save to the picture file

keyboard.add_hotkey('alt+shift+t', kahoot_bot)
keyboard.wait()