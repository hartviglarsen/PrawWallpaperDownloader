"""
Functions related to downloading wallpapers
"""
import requests
import time
import os


# Get image link of most upvoted wallpaper of the day
def get_top_image(subreddit):
    dl_urls = []
    for submission in subreddit.get_top(limit=25):
        url = submission.url
        if url.endswith(".jpg"):
            context = {"url": url, "title": submission.title, "date": time.strftime("%d-%m-%Y %H:%M")}
            dl_urls.append(context)
        # Imgur support
        elif ("imgur.com" in url) and ("/a/" not in url):
            if url.endswith("/new"):
                url = url.rsplit("/", 1)[0]
            id = url.rsplit("/", 1)[1].rsplit(".", 1)[0]
            link = "http://imgur.com/" + id + ".jpg"
            context = {"url": link, "title": submission.title, "date": time.strftime("%d-%m-%Y %H:%M")}
            dl_urls.append(context)
    return dl_urls


# Save a list of image links to disk
def download_images(submissions):
    image_n = 0
    total_images = len(submissions)

    for submission in submissions:
        print("Downloading image " + str(image_n+1) + "/" + str(total_images))
        # Send request
        response = requests.get(submission["url"])

        # Save image to disk
        if response.status_code == 200:
            # TODO: Sanitize post title and mkdir
            file_path = os.path.join('images', submission["title"] + ".jpg")
            with open(file_path, 'wb') as fo:
                for chunk in response.iter_content(4096):
                    fo.write(chunk)
                fo.close()
        image_n += 1
