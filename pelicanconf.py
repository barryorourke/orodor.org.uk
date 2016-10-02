#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Barry O'Rourke"
SITEURL = 'http://localhost:8000'
SITENAME = 'orodor.org.uk'
SITETITLE = AUTHOR
SITESUBTITLE ='fat dad, sysadmin and developer with mild hemiplegia.'
EMAIL = 'barry@orodor.org.uk'
SITELOGO = '/images/avatar.png'
FAVICO =  SITEURL + 'images/favico.ico'

ROBOTS = 'index, follow'
COPYRIGHT_YEAR = '2016'

OG_LOCALE = 'en_GB'
TIMEZONE = 'Europe/London'

DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

THEME = '../Flex'
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = None
STATIC_PATHS = ['images', 'css']
EXTRA_PATH_METADATA = {'css/orodor.css': {'path': 'css/orodor.css'}}
CUSTOM_CSS = 'css/orodor.css'

# social links
SOCIAL = (
    ('envelope-o', 'mailto://barry@orodor.org.uk'),
    ('rss', 'https://orodor.org.uk/feed/atom.xml'),
    ('twitter', 'https://www.twitter.com/barryorourke'),
    ('github', 'https://www.github.com/barryorourke'),
)

# feed settings
FEED_ATOM = "feed/atom.xml"

# do not generate                                                                                                                                                                              
ARCHIVES_SAVE_AS      = None
AUTHORS_SAVE_AS       = None
CATEGORIES_SAVE_AS    = None
TAGS_SAVE_AS          = None
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None

# article urls
ARTICLE_URL     = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# page urls
PAGE_URL        = '{slug}/'
PAGE_SAVE_AS    = '{slug}/index.html'

# tag urls
TAG_URL         = 'tag/{slug}/'
TAG_SAVE_AS     = 'tag/{slug}/index.html'

# pagination
DEFAULT_PAGINATION = 5

# set the url pattern for paginated pages
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap']

# sitemap configuration
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
