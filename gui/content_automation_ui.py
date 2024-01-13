import gradio as gr


from gui.ui_tab_video_automation import VideoAutomationUI



class GradioContentAutomationUI:
    def __init__(self, VideoUI):
        self.VideoUI =VideoUI
        self.content_automation_ui = None

    def create_ui(self):

        with gr.Tab("Content Automation") as self.content_automation_ui:
            gr.Markdown("# 🏆 Create Video 🚀")
            gr.Markdown("## Choose your desired automation task.")
            choice = gr.Radio(['🎬 Automate the creation of shorts', '🎞️ Automate a video with stock assets', ], label="Choose an option")
            video_automation_ui = VideoAutomationUI(self.VideoUI).create_ui()
            # short_automation_ui = ShortAutomationUI(self.shortGPTUI).create_ui()

            choice.change(lambda x: (gr.update(visible=x == choice.choices[1])), [choice], [video_automation_ui])
        return self.content_automation_ui
