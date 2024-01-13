import os
from moviepy.editor import *
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout


def create_video():
    # Directory containing images
    image_directory = "images"

    # List image files in the directory
    image_files = [f for f in os.listdir(image_directory) if f.endswith(".png")]
    image_files.sort()  # Sort the image files

    # Initialize a list to store image clips
    image_clips = []

    # Calculate the duration for each image based on audio duration and the number of images
    audio_duration = AudioFileClip("output.mp3").duration
    image_count = len(image_files)
    image_duration = audio_duration / image_count

    # Desired video dimensions
    width, height = 1080, 1980  # Adjusted for the desired frame size
    fade_duration = 1

    # Function to slide the image from left to right
    def slide_from_left_to_right(image_clip, frame_index):
        t = frame_index / image_clip.fps  # Calculate time based on frame index and frame rate
        x_position = -1024 + (1920 * t / image_duration)  # Adjust for your desired movement and scaling
        scaled_clip = image_clip.resize((1080, 1980))  # Scale the image to the desired frame size
        return scaled_clip.set_position((x_position, 'center')).set_duration(1 / image_clip.fps)

    # Load and process each image
    for image_file in image_files:
        image_path = os.path.join(image_directory, image_file)
        image_clip = ImageSequenceClip([image_path], fps=1 / image_duration)

        # Apply the fade-in and fade-out transitions to each image clip
        fadein_clip = fadein(image_clip, fade_duration)
        fadeout_clip = fadeout(image_clip, fade_duration)

        # Create a sliding effect by applying the position adjustment
        sliding_image_clips = [slide_from_left_to_right(fadein_clip, i) for i in range(int(fadein_clip.fps))]
        sliding_image_clips.append(fadeout_clip)

        image_clips.extend(sliding_image_clips)

    # Concatenate the image clips into a video
    final_video = concatenate_videoclips(image_clips, method="compose")

    # Resize the final video to the desired dimensions
    final_video = final_video.resize((1080, 1980))

    # Load the audio file
    audio = AudioFileClip("output.mp3")

    # Set the audio of the final video
    final_video = final_video.set_audio(audio)

    # Load the background music
    background_audio = AudioFileClip("background-music.mp3")

    # Trim the background music to match the video's duration
    if background_audio.duration > final_video.duration:
        background_audio = background_audio.subclip(0, final_video.duration)

    final_audio = CompositeAudioClip([audio.volumex(1.0), background_audio.volumex(0.2)])

    # Set the audio of the final video to include background music
    final_video = final_video.set_audio(final_audio)

    # Set the audio of the final video to include the trimmed background music

    # Export the final video
    final_video.write_videofile("final_video_with_background.mp4", codec="libx264", fps=30)


