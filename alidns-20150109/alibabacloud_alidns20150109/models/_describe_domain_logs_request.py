# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainLogsRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        key_word: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        type: str = None,
        end_date: str = None,
    ):
        # The ID of the domain name group. If you do not specify this parameter, all groups are queried.
        self.group_id = group_id
        # The keyword for the query. A case-insensitive \\`contains\\` search is performed.
        self.key_word = key_word
        # The language of the request and response.
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        # 
        # The default value is **zh**.
        self.lang = lang
        # The number of the page to return. The value starts from **1**. The default value is **1**.
        self.page_number = page_number
        # The number of entries to return on each page. The maximum value is **100**. The default value is **20**.
        self.page_size = page_size
        # The start date. The format is **YYYY-MM-DD**.
        self.start_date = start_date
        # The type of content to query.
        # 
        # - domain: domain name
        # 
        # - slavedns: secondary DNS
        # 
        # If you do not specify this parameter, all types are queried.
        self.type = type
        # The end date. The format is **YYYY-MM-DD**.
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.type is not None:
            result['Type'] = self.type

        if self.end_date is not None:
            result['endDate'] = self.end_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        return self

