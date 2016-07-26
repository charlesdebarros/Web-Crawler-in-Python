#!/usr/bin/env python3

import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://thenewboston.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Each queue link is a new job
def create_jobs:
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Checks if there are items in the queue, if so, crawl them.
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue.')
        create_jobs()
