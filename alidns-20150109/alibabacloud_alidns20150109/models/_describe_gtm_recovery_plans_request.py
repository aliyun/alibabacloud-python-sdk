# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGtmRecoveryPlansRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The keyword for the query. Fuzzy match is supported by disaster recovery plan name.
        self.keyword = keyword
        # The language in which you want the values of some response parameters to be returned. These response parameters support multiple languages.
        self.lang = lang
        # The page number to return. The page number starts from **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return per page. Maximum value: **100**. Default value: **20**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

