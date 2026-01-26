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
        region_id: str = None,
        search: str = None,
    ):
        # Language,the default language is Chinese.
        self.aliyun_lang = aliyun_lang
        # Category filter.
        self.category = category
        # Whether to enable regular matching.
        self.regexp = regexp
        # The region ID.
        self.region_id = region_id
        # A query field can be queried by name or description.
        self.search = search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.category is not None:
            result['Category'] = self.category

        if self.regexp is not None:
            result['Regexp'] = self.regexp

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search is not None:
            result['Search'] = self.search

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Regexp') is not None:
            self.regexp = m.get('Regexp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Search') is not None:
            self.search = m.get('Search')

        return self

