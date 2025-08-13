# This script allows users to download a playlist of youtube songs from a text document in a specified folder

import yt_dlp
import os

def download_audio(url, output_path='.'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    path = input("Enter youtube link collection file path: ").strip()
    download_location = input("Enter playlist folder path (or leave blank for current folder): ").strip()
    if not download_location:
        download_location = '.'

    with open(path) as f:
        for x in f:
            download_audio(x, download_location)