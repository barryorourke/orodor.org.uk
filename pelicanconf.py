#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Barry O'Rourke"
SITEURL = 'http://localhost:8000'
SITENAME = 'orodor.org.uk'
SITETITLE = AUTHOR
SITESUBTITLE ='fat dad, sysadmin and developer with mild hemiplegia.'
SITELOGO = 'images/avatar.png'
FAVICO =  SITEURL + 'images/favico.ico'

ROBOTS = 'index, follow'
COPYRIGHT_YEAR = '2016'

OG_LOCALE = 'en_GB'
TIMEZONE = 'Europe/London'

DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'en'

THEME = '../Flex'
SUMMARY_MAX_LENGTH = None

# social links
SOCIAL = (
    ('envelope-o', 'mailto://barry@orodor.org.uk'),
    ('rss', 'https://orodor.org.uk/feed/atom.xml'),
    ('twitter', 'https://www.twitter.com/barryorourke'),
    ('github', 'https://www.github.com/barryorourke'),
)

# feed settings
FEED_ATOM = "feed/atom.xml"

# pagination
DEFAULT_PAGINATION = 5
