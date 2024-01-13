import gradio as gr
from content_generate import get_response
from image_generate import generate_image_for_video
from image_editing import create_video
from voice_generation import generate_voice
from caption_generate import generate_captions

def app(nature_video_query):
    get_response(nature_video_query)
    generate_image_for_video()
    generate_voice()
    create_video()
    generate_captions("final_video_with_background.mp4")

# Create Gradio UI
iface = gr.Interface(
    fn=app,
    inputs="text",
    outputs="text",
    live=True,
    interpretation="default",
    examples=[["Nature Video"]],
    title="Video Generation App",
    description="Generate a video based on a given query."
)

iface.launch()
