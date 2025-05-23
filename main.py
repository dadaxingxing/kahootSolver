from google import genai
import os
from dotenv import load_dotenv
import mss 
import mss.tools
import keyboard

load_dotenv()

API_key = os.getenv('API_KEY')
client = genai.Client(api_key=API_key)

def kahoot_bot():
        
    with mss.mss() as sct:

        # The screen part to capture
        monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
        output = "window.png"

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)



# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents="hello."
# )
# print(response.text)

keyboard.add_hotkey('ctrl+shift+s', kahoot_bot)
keyboard.wait()