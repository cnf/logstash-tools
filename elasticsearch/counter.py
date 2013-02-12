#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2013, Frank Rosquin <frank@rosquin.net>

ISC license

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
"""

from datetime import datetime, timedelta
import urllib
import urllib2

from urllib2 import HTTPError

import json
import sys

min_count = 1000
if len(sys.argv) >= 2:
    minutes = int(sys.argv[1])
else:
    minutes = 15

now = datetime.now()
today = "{year}.{month:02d}.{day:02d}".format(year=now.year,
                                              month=now.month,
                                              day=now.day)
ago = timedelta(minutes=minutes)
offset = (now - ago).isoformat()

query = urllib.urlencode({'q': "@timestamp:[{offset}+01 TO *]".format(
    offset=offset)})
url = "http://127.0.0.1:9200/logstash-{today}/_count?".format(today=today)

try:
    result = urllib2.urlopen(url + query).read()
    arr = json.loads(result)
except HTTPError as e:
    arr = { 'count': 0 }



print arr['count']
