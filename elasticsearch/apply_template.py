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

import httplib
import os.path
import sys
import json


def read_json(tpath):
    try:
        with open(tpath) as template:
            tjson = json.load(template)
            return tjson
    except:
        print "no such file: {}".format(tpath)
        sys.exit()


def get_template_name(tpath):
    basename = os.path.basename(tpath)
    return os.path.splitext(basename)[0]


def put_template(data, tname):
    conn = httplib.HTTPConnection("127.0.0.1", 9200, timeout=10)
    conn.request("PUT", "/_template/{0}".format(tname), json.dumps(data))
    res = conn.getresponse()
    return res.status, res.reason

if __name__ == "__main__":
    tpath = os.path.abspath(sys.argv[1])
    tname = get_template_name(tpath)
    print put_template(read_json(tpath), tname)
