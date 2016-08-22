import argparse
from scraper import Scraper

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--subreddit", help="specify subreddit to scrape", default="wallpapers")
parser.add_argument("-l", "--limit", help="set amount of posts to sift through (default 25)", default=25, type=int)
parser.add_argument("--log", help="save a log of wallpapers downloaded/skipped/failed",
                    action="store_true", default=False)
args = parser.parse_args()

scraper = Scraper(args)
scraper.run()
