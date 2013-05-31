#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mike"
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
SITENAME = u"noisufnoc.com"
SITEURL = ''
DEFAULT_CATEGORY = 'Blog'
DEFAULT_LANG = 'en'
DELETE_OUTPUT_DIRECTORY = True
THEME = 'pelican-chunk'
GITHUB_URL = 'https://github.com/noisufnoc/noisufnoc.github.com'
TWITTER_USERNAME = 'noisufnoc'

TIMEZONE = 'America/Los_Angeles'


# Blogroll
LINKS = (
    ('github', 'http://github.com/noisufnoc'),
    ('google+', 'http://plus.google.com/108169237874141810797'),
    ('twitter', 'http://twitter.com/noisufnoc'),
    ('instagram', 'http://instagram.com/therealnoisufnoc'),
    ('facebook', 'http://facebook.com/noisufnoc'),
)

# Social widget
SOCIAL = (
    ('twitter', 'http://twitter.com/noisufnoc'),
    ('facebook', 'http://facebook.com/noisufnoc'),
    ('instagram', 'http://instagram.com/therealnoisufnoc'),
)

DEFAULT_PAGINATION = 10


#SOCIAL = (
#    ('aclark4life', 'http://twitter.com/aclark4life'),
#    ('ACLARKNET', 'http://twitter.com/ACLARKNET'),
#    ('GitHub', 'http://github.com/aclark4life'),
#    ('Gittip', 'https://www.gittip.com/aclark4life'),
#    ('PythonPackages', 'https://pythonpackages.com/user/aclark4life'),
#    ('atom feed (Django)', 'http://blog.aclark.net/feeds/Django.atom.xml'),
#    ('atom feed (Mozilla)', 'http://blog.aclark.net/feeds/Mozilla.atom.xml'),
#    ('atom feed (Plone)', 'http://blog.aclark.net/feeds/Plone.atom.xml'),
#    ('atom feed (Python)', 'http://blog.aclark.net/feeds/Python.atom.xml'),
#)
