from pytube import YouTube
import subprocess

# Function to play YouTube video using VLC
def play_video(video_url):
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    video_url = stream.url
    subprocess.call(["vlc", video_url])  # Opens the video in VLC player

# Example usage
video_url = "https://youtu.be/ECtLvbb7whU"  # Insert your YouTube video URL here
play_video(video_url)
