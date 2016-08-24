# PrawWallpaperDownloader (Python3)
[![Build Status](https://travis-ci.org/nikolajlauridsen/PrawWallpaperDownloader.svg?branch=master)](https://travis-ci.org/nikolajlauridsen/PrawWallpaperDownloader)

Download a bunch of wallpapers from the hot sections of r/wallpapers

Inspirations is drawn from [Daily-Reddit-Wallpaper](https://github.com/ssimunic/Daily-Reddit-Wallpaper)

## Install process
1. Download and install python from https://www.python.org/ (If you're unsure download version 3.5 and chose default install)
2. Clone or download/extract the repository
3. Install requirements with 
```
py -m pip install -r requirements.txt
```
(You might have to use python or python3 instead of py depending on your system/install)

#### Requirements
* praw
* requests

## Usage
The script can be run by double clicking wallpaper_downloader.py or via the commandline with the latter being the best option since the script accepts a variety of optional arguments

#### Examples
Basic use: search through the first 25 posts of /r/wallpapers
```
py wallpaper_downloader.py
```
"Advanced" use: Search the first 100 posts of /r/MinimalWallpaper and save a log
```
py wallpaper_downloader.py -s MinimalWallpaper -l 100 --log
```

### Optional arguments
* --subreddit \<subreddit> or -s \<subreddit> specify which subreddit to download images from, omit the /r/ (default is wallpapers)
* --limit \<number> or -l \<number> specify how many posts to search as a whole number (default is 25)
* --re or -r will try to re download every post previously downloaded
* --log save a log of posts skipped
* --verbose or -v print skipped posts to console
