# youtube-convrt
Downloads Youtube playlist as mp3 files to the target directory.

## Usage

`python3 main.py playlist_url target_directory`

### Parameters

`playlist_url` is the URL to the youtube playlist (youtube.com/playlist...).

`target_directory` is the directory where you want to save the mp3 files. It can be absolute or relative path. If the directory doesn't exist it will be created when running the script.

## Dependencies

The script is using these 2 packages:

1. https://pypi.org/project/pytube/
This one downloads the youtube videos as mp4 files.

2. https://pypi.org/project/moviepy/
This one converts mp4 files to the mp3 files.
