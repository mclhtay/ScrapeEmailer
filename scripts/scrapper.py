from bs4 import BeautifulSoup
import urllib.request
import re
import time
import utils
import sys
from mail_client import MailClient

WAIT_TIME = 7200

def scrape(item):
    web_url = urllib.request.urlopen(item.url)

    soup = BeautifulSoup(web_url, 'html.parser')

    for key_word in item.key_words:
        exist = soup.body.findAll(text=re.compile(key_word))
        if len(exist) != 0 and not item.opp:
            return True
        if len(exist) == 0 and item.opp:
            return True
    return False


def start_scrapper(stop_when_found):
    mail_config = utils.get_email_config()
    mail_client = MailClient(mail_config)
    mail_client.start_mail_client()
    utils.close_file(mail_config)
    scrape_items = utils.get_scrape_items()

    while True:
        print("Scrapper running")
        for scrape_item in scrape_items:
            found = scrape(scrape_item)
            if found:
                print("Found 1 item")
                mail_client.send_email(scrape_item.message)
                if stop_when_found:
                    break
        time.sleep(WAIT_TIME)

if __name__ == '__main__':
    stop_when_found = True
    if len(sys.argv) > 1:
        stop_when_found = False if sys.argv[1] == "--no-stop" else True
    start_scrapper(stop_when_found)