# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSampleListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        current_page: int = None,
        page_size: int = None,
        reg_id: str = None,
        sample_type: str = None,
        sample_value: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Current page number.
        self.current_page = current_page
        # Page size, with a default value of 10
        self.page_size = page_size
        # Region code
        self.reg_id = reg_id
        # Sample type
        self.sample_type = sample_type
        # Sample data value.
        self.sample_value = sample_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.sample_type is not None:
            result['sampleType'] = self.sample_type

        if self.sample_value is not None:
            result['sampleValue'] = self.sample_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sampleType') is not None:
            self.sample_type = m.get('sampleType')

        if m.get('sampleValue') is not None:
            self.sample_value = m.get('sampleValue')

        return self

