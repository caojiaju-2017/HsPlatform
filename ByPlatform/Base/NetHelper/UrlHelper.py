#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
__all__ = ['UrlHelper']

class UrlHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def py2GetUrlParams(url):
        import urlparse
        query = urlparse.urlparse(url).query
        return dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items()])

    @staticmethod
    def py3GetUrlParams(url):
        from urllib import parse
        query = parse.urlparse(url).query
        return dict([(k, v[0]) for k, v in parse.parse_qs(query).items()])

    @staticmethod
    def getUrlParams(url):
        if sys.version_info[0] == 3:
            return UrlHelper.py3GetUrlParams(url)
        elif sys.version_info[0] == 2:
            return UrlHelper.py2GetUrlParams(url)
