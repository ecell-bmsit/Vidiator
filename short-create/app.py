

from content_generate import get_response
from image_generate import generate_image_for_video
from  image_editing import create_video
from voice_generation import generate_voice
from caption_generate import generate_captions


def app():
    get_response("Nature Video")
    generate_image_for_video()
    generate_voice()
    create_video()
    generate_captions("final_video_with_background.mp4")

app()
