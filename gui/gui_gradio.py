import gradio as gr

from gui.content_automation_ui import GradioContentAutomationUI
from gui.ui_abstract_base import AbstractBaseUI
from gui.ui_components_html import GradioComponentsHTML
from gui.ui_tab_asset_library import AssetLibrary




class VideoUI(AbstractBaseUI):


    def __init__(self, colab=False):
        super().__init__(ui_name='gradio_video')



    def create_interface(self):

        with gr.Blocks(css="footer {visibility: hidden}", title="Vidiator") as VideoUI:
            with gr.Row(variant='compact'):
                gr.HTML(GradioComponentsHTML.get_html_header())

            self.content_automation = GradioContentAutomationUI(VideoUI).create_ui()
            self.asset_library_ui = AssetLibrary().create_ui()

        return VideoUI

    def launch(self):

        VideoUI = self.create_interface()
        VideoUI.queue(concurrency_count=5, max_size=20).launch(server_port=31415, height=1000, share=True)


if __name__ == "__main__":
    app = VideoUI()
    app.launch()
