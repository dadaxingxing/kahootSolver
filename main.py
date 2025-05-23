from google import genai
import os
from dotenv import load_dotenv
import mss 
import mss.tools
import keyboard
import pyautogui


load_dotenv()

API_key = os.getenv('API_KEY')
client = genai.Client(api_key=API_key)

def kahoot_bot():

    question_and_answers = {
        0: (0.0, 0.072, 1.0, 0.2),
        1: (0.042, 0.667, 0.458, 0.742),
        2: (0.542, 0.667, 1.0, 0.742),
        3: (0.042, 0.8, 0.458, 0.875),
        4: (0.542, 0.8, 1.0, 0.875),
    }
    
    width, height = pyautogui.size()
    with mss.mss() as sct:
        
        for key, value in question_and_answers.items():
            
            x1, y1, x2, y2 = int(value[0] * width), int(value[1] * height), int(value[2] * width), int(value[3] * height)
            

            # The screen part to capture
            monitor = {"top": y1, "left": x1, "width": y2 - y1, "height": x2 - x1}
            output = f"window{key}.png"

            # Grab the 
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            print(output)



# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents="hello."
# )
# print(response.text)

keyboard.add_hotkey('alt+shift+t', kahoot_bot)
keyboard.wait()