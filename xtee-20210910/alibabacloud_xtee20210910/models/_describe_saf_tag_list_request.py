# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSafTagListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        tag_name: str = None,
        api_id: str = None,
        current_page: str = None,
        page_size: str = None,
        reg_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Tag name. Fuzzy search.
        self.tag_name = tag_name
        # API service ID.
        self.api_id = api_id
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10.
        self.page_size = page_size
        # Region code.
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.api_id is not None:
            result['apiId'] = self.api_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

