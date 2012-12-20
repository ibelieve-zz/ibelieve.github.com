#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Robin (Bing) Lu'


SITENAME = u'Compile My Dream'
SITEURL = 'http://ibelieve.github.com'

TIMEZONE = 'America/Toronto'




DEFAULT_LANG = u'en'

#FEED_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('github', 'http://github.com/ibelieve'),)

DEFAULT_PAGINATION = 10

GITHUB_URL = 'http://github.com/ibelieve'
#NEWEST_FIRST_ARCHIVES (True)
#DEFAULT_CATEGORY ('blog')
#TYPOGRIFY (True)
#SUMMARY_MAX_LENGTH (50)
