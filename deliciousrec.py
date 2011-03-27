#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Paul Anderson on 2011-03-27.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os

from pydelicious import get_popular,get_userposts,get_urlposts

def initializeUserDict(tag,count=5):
	user_dict={}
	#get top count popular posts
	for p1 in get_popular(tag=tag)[0:count]:
		#find all users who posted this
		for p2 in get_urlposts(p1['href']):
			user=p2['user']
			user_dict[user]={}
	return user_dict

def main():
	pass


if __name__ == '__main__':
	main()

