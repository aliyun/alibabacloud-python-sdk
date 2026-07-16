# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFieldPageRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        classify: str = None,
        condition: str = None,
        current_page: str = None,
        name: str = None,
        page_size: str = None,
        reg_id: str = None,
        source: str = None,
        status: str = None,
        title: str = None,
        type: str = None,
    ):
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The field classification.
        self.classify = classify
        # The query parameter: name or title.
        self.condition = condition
        # The current page number.
        self.current_page = current_page
        # The field name.
        self.name = name
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region code.
        self.reg_id = reg_id
        # The field source.
        self.source = source
        # The status.
        self.status = status
        # The title.
        self.title = title
        # The field type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.classify is not None:
            result['classify'] = self.classify

        if self.condition is not None:
            result['condition'] = self.condition

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.name is not None:
            result['name'] = self.name

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.source is not None:
            result['source'] = self.source

        if self.status is not None:
            result['status'] = self.status

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('classify') is not None:
            self.classify = m.get('classify')

        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

