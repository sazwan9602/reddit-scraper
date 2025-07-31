from src import scraper
from src import fn
from typing import List
import time
from glom import glom

RAW_PATH = "src/raw/{}.json"
FINAL_PATH = "src/final/{}.json"


def run(subreddit_name: str) -> None:
    raw_data = scrape(subreddit_name)
    fn.write_json(RAW_PATH.format(subreddit_name), raw_data)

    processed_data = preprocess_data(raw_data)
    fn.write_json(FINAL_PATH.format(subreddit_name), processed_data)


def scrape(subreddit_name: str) -> List[dict]:
    print(f"scraping {subreddit_name}")

    base_url: str = f"https://www.reddit.com/r/{subreddit_name}/.json?limit=25"  # default limit of page is 25 posts
    page_start: int = 0
    next_cursor: str = None
    results: List = []
    while page_start < 10:
        page_start += 1
        if next_cursor:
            url = base_url + f"&after={next_cursor}"
        else:
            url = base_url
        print(f"Page {page_start}: Get {url}")

        listing: dict = scraper.get(url)
        if listing:
            children = glom(listing, "data.children", default=None)
            results += children
            next_cursor = glom(listing, "data.after", default=None)
            if not next_cursor:
                print("Next cursor not found")
                break
            print("sleep 2 seconds")
            time.sleep(2)
        else:
            break
    return results


def preprocess_data(raw_data: List[dict]) -> List[dict]:
    print("preprocess posts")
    results = []
    for raw in raw_data:
        post_title = glom(raw, "data.title", default=None)
        post_thumbnail: str = glom(
            raw, "data.preview.images.0.source.url", default=None
        )
        if post_thumbnail:
            if "&amp;" in post_thumbnail:
                post_thumbnail = post_thumbnail.replace("&amp;", "&")
            data = {"title": post_title, "thumbnail": post_thumbnail}
            results.append(data)
    return results
