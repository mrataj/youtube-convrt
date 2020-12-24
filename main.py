from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description='Downloads Youtube playlist to the target directory.')
parser.add_argument('playlist_url', type=str, help='URL of the Youtube playlist.')
parser.add_argument('target_directory', type=str, help='Target directory where to put mp3 files.')
args = parser.parse_args()

playlist = Playlist(args.playlist_url)

print(str(len(playlist.video_urls)) + " videos found, downloading in progress ...")

# Download all tracks as mp4 files
for video in playlist.videos:
    audioStream = video.streams.get_by_itag('140')
    audioStream.download(output_path=args.target_directory)

print("Download successful, converting files from mp4 to mp3 ...")

# Convert mp4 files to mp3
for file in os.listdir(args.target_directory):
  if re.search('mp4', file):
    print("Converting " + file + " to mp3 ...")
    mp4_path = os.path.join(args.target_directory,file)
    mp3_path = os.path.join(args.target_directory,os.path.splitext(file)[0]+'.mp3')
    new_file = mp.AudioFileClip(mp4_path)
    new_file.write_audiofile(mp3_path)
    os.remove(mp4_path)

print("Conversion successful, files are now ready!")
