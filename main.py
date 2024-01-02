from pytube import YouTube
from flask import Flask, request, render_template
import ssl
import os
app = Flask(__name__)

def download_video(url):
    try:
        # Отключение проверки сертификата SSL для pytube
        ssl._create_default_https_context = ssl._create_unverified_context

        # Скачивание видео с YouTube
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=os.path.expanduser('~/Downloads'))

        print("Video downloaded successfully")
    except Exception as e:
        print("Error: ", str(e))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download_video', methods=['POST'])
def download_video_route():
    video_url = request.form['video_url']
    download_video(video_url)
    return 'Video is being downloaded'

if __name__ == '__main__':
    app.run(debug=True)