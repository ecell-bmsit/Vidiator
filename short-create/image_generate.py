import json
import os
import requests
import openai
import base64
import time



with open('response.json', 'r') as script_file:
  script_data = json.load(script_file)





def generate_image_for_video():
    prompt_list = []

    for caption in script_data['captions']:
        if len(caption['prompt']) > 0:
            prompt_list.append(caption['prompt'])

    for i, prompt in enumerate(prompt_list):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size='1024x1024',
            api_key=api_key,
        )

        # Loop through the image URLs in the response and download/save them
        for j, image_data in enumerate(response["data"]):
            img_url = image_data["url"]
            img_filename = f"images/generated_image_{i}_{j}.png"  # Include prompt index

            image_response = requests.get(img_url)
            if image_response.status_code == 200:
                with open(img_filename, "wb") as f:
                    f.write(image_response.content)
                print(f"Image {i}_{j} saved to '{img_filename}'")
            else:
                print(f"Failed to download Image {i}_{j}.")


