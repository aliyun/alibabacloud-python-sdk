# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAddonsRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        category: str = None,
        regexp: bool = None,
        search: str = None,
    ):
        self.aliyun_lang = aliyun_lang
        self.category = category
        self.regexp = regexp
        self.search = search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['aliyunLang'] = self.aliyun_lang

        if self.category is not None:
            result['category'] = self.category

        if self.regexp is not None:
            result['regexp'] = self.regexp

        if self.search is not None:
            result['search'] = self.search

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunLang') is not None:
            self.aliyun_lang = m.get('aliyunLang')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('regexp') is not None:
            self.regexp = m.get('regexp')

        if m.get('search') is not None:
            self.search = m.get('search')

        return self

