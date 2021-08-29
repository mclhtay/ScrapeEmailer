import sys
import json
import os.path
from scrape_item import ScrapeItem

def get_config_file_path(file_name):
    return os.path.dirname(__file__)+"/../configs/"+file_name

def close_file(f):
    f.close()

def get_email_config():
    try:
        f = open(get_config_file_path("email_config.json"))
        return f
    except Exception as e:
        print(e)
        sys.exit()

def get_scrape_items():
    try:
        f =  open(get_config_file_path("scrape_items.json"))
        items_json = json.load(f)
        close_file(f)
        items = []
        for item in items_json["items"]:
            items.append(
                ScrapeItem(
                    url=item['url'],
                    message=item['message'],
                    key_words=item['key_words'],
                    opp=item['opp']
                )
            )
        return items
    except Exception as e:
        print(e)
        sys.exit()
