#!/usr/bin/env python

from html.parser import HTMLparser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        pass

    def error(self, message):
        pass
