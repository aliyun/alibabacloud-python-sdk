# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVariableSceneListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        biz_type: str = None,
        config_key: str = None,
        current_page: str = None,
        page_size: str = None,
        paging: bool = None,
        reg_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Business type.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # Configuration key.
        self.config_key = config_key
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10.
        self.page_size = page_size
        # Paging flag, default is true.
        # 
        # This parameter is required.
        self.paging = paging
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

        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.config_key is not None:
            result['configKey'] = self.config_key

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.paging is not None:
            result['paging'] = self.paging

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('configKey') is not None:
            self.config_key = m.get('configKey')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('paging') is not None:
            self.paging = m.get('paging')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

