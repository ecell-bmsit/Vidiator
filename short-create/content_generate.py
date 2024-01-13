import openai
import json




def get_response(topic):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": f'''Act as a video creator you are a video script witer and flim maker I will give you the topic write a video script  for the duration of 1 minute and {topic}  and you should also generate script for the video with 
            duration and also timstamps for each script your response should be like this keywordsearch for video in google and also give me the prompt for image to generate from DALL E and text this example note this in text give me only script of the video text with timestamps don't give other words like intro music
            finally format in json file as per give prompt example json:

            captions:
                 start:
                 end:
                 text:
                 keyword:
                 prompt:


            '''

             }
        ]
    )
    final_response = response.choices[0].message.content

    print(final_response)

    # Save the response to a JSON file
    response_data = json.loads(final_response)

    # Save the response as a JSON file
    with open('response.json', 'w') as json_file:
        json.dump(response_data, json_file, indent=4)

    print(final_response)


