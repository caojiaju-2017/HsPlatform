#!/usr/bin/python
# -*- coding:utf-8 -*-

from CodernityDB.database import Database
from CodernityDB.hash_index import HashIndex


class WithXIndex(HashIndex):
    def __init__(self, *args, **kwargs):
        # self.indexCode = kwargs[]
        kwargs['key_format'] = '32s'
        super(WithXIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        a_val = data.get("ucode")
        if a_val is not None:
            return a_val, None
        return None

    def make_key(self, key):
        return key