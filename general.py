#!/usr/bin/env python

# Each website crawled has its own project folder

import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

create_project_dir('testdirectory')
