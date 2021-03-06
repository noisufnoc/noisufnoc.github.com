#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Mike'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
#PAGE_SAVE_AS = '{page_name}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
SITENAME = 'noisufnoc.com'
SITEURL = 'noisufnoc.com'
DEFAULT_CATEGORY = 'Blog'
DEFAULT_LANG = 'en'
DELETE_OUTPUT_DIRECTORY = True
THEME = 'pure-single'
GITHUB_URL = 'https://github.com/noisufnoc/'
TWITTER_USERNAME = 'noisufnoc'

TIMEZONE = 'America/New_York'

COVER_IMG_URL = 'http://i.imgur.com/AqYrKdD.jpg'
#PROFILE_IMG_URL = 'http://i.imgur.com/vKNDRoJ.jpg'
PROFILE_IMG_URL = 'http://i.imgur.com/HPAapF0.jpg'

GOOGLE_ANALYTICS = 'UA-18841921-1'

TAGLINE = '#!/usr/local/bin/python2'

#MENUITEMS = (
#    ('foo', 'http://google.com'),
#    ('bar', 'http://reddit.com'),
#    ('baz', 'http://bing.com'),
#)

# Social widget
SOCIAL = (
    ('github', 'http://github.com/noisufnoc'),
    ('twitter', 'http://twitter.com/noisufnoc'),
    ('google', 'http://plus.google.com/108169237874141810797'),
    ('facebook', 'http://facebook.com/noisufnoc'),
    ('instagram', 'http://instagram.com/noisufnoc'),
    ('beer', 'http://untappd.com/noisufnoc'),
)

DEFAULT_PAGINATION = 10
