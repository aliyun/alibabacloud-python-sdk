# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataSourcePageListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        reg_id: str = None,
        type: str = None,
    ):
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip
        # The current page number.
        self.current_page = current_page
        # The variable name.
        self.name = name
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region ID.
        self.reg_id = reg_id
        # The type.
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

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.name is not None:
            result['name'] = self.name

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

