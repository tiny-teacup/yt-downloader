import yt_dlp
import os

def download_media(url, media_type, output_path='.'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if media_type == 'video':
        ydl_opts = {
            'format': 'best[height<=1080]/bestvideo[height<=1080]+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4'
        }
    elif media_type == 'audio':
        ydl_opts = {
            'format': 'bestaudio[ext=m4a]/bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
    else:
        print("Invalid option.")
        return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    download_location = input("Enter download folder path (or leave blank for current folder): ").strip()
    if not download_location:
        download_location = '.'

    print("Choose download type:")
    print("1. Video")
    print("2. Audio (mp3)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        download_media(video_url, 'video', download_location)
    elif choice == '2':
        download_media(video_url, 'audio', download_location)
    else:
        print("Invalid choice.")