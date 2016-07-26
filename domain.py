#!/usr/bin/env python 3.3.0

from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_subdomain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get subdomain name (name.example.com)
def get_subdomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
