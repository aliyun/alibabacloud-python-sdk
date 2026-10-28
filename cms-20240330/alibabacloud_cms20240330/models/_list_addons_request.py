# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAddonsRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        api_version: str = None,
        category: str = None,
        regexp: bool = None,
        search: str = None,
    ):
        # The language environment. Valid values: zh and en. Default value: zh.
        self.aliyun_lang = aliyun_lang
        # The add-on catalog version. Valid values: v1 and v2. Default value: v2. If you specify v1, the add-ons in the v1 catalog are listed.
        self.api_version = api_version
        # The category filter.
        self.category = category
        # Specifies whether to use regular expression matching for the query field. Default value: false.
        self.regexp = regexp
        # The search keyword. You can search by add-on name, description, or keyword.
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

        if self.api_version is not None:
            result['apiVersion'] = self.api_version

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

        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('regexp') is not None:
            self.regexp = m.get('regexp')

        if m.get('search') is not None:
            self.search = m.get('search')

        return self

