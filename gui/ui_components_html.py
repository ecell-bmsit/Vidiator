class GradioComponentsHTML:

    @staticmethod
    def get_html_header() -> str:

        return '''
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 5px;">
            <h1 style="margin-left: 0px; font-size: 35px;">Vidiator.AI</h1>
            
            </div>
        '''

    @staticmethod
    def get_html_error_template() -> str:
        return '''
        <div style='text-align: center; background: #f2dede; color: #a94442; padding: 20px; border-radius: 5px; margin: 10px;'>
          <h2 style='margin: 0;'>ERROR : {error_message}</h2>

        </div>
        '''

    @staticmethod
    def get_html_video_template(file_url_path, file_name, width="auto", height="auto"):

        html = f'''
            <div style="display: flex; flex-direction: column; align-items: center;">
                <video width="{width}" height="{height}" style="max-height: 100%;" controls>
                    <source src="{file_url_path}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <a href="{file_url_path}" download="{file_name}" style="margin-top: 10px;">
                    <button style="font-size: 1em; padding: 10px; border: none; cursor: pointer; color: white; background: #007bff;">Download Video</button>
                </a>
            </div>
        '''
        return html
