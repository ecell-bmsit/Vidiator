from elevenlabs import generate,save
import json
from elevenlabs import set_api_key


def generate_voice():
    with open('response.json', 'r') as script_file:
        script_data = json.load(script_file)

    text = ""

    for caption in script_data['captions']:
        text += caption['text'] + " "

    print(text)

    audio = generate(
        text=text,
        voice="Sarah",
        model="eleven_multilingual_v2"
    )

    save(audio, filename="output.mp3")
