# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVersionPageListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        current_page: int = None,
        object_code: str = None,
        object_id: int = None,
        page_size: int = None,
        paging: bool = None,
        reg_id: str = None,
        type: str = None,
    ):
        # Sets the language type for the request and response messages, with a default value of **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Maximum number of results to be read in this call, with a default value of 10.
        self.max_results = max_results
        # Used to mark the starting position for reading. An empty value indicates starting from the beginning.
        self.next_token = next_token
        # Current page number.
        self.current_page = current_page
        # Name of the variable.
        self.object_code = object_code
        # Primary key ID of the variable.
        self.object_id = object_id
        # Number of items per page, with a default value of 10.
        self.page_size = page_size
        # Pagination flag, with a default value of true.
        self.paging = paging
        # Region code.
        self.reg_id = reg_id
        # Type.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.object_code is not None:
            result['objectCode'] = self.object_code

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.paging is not None:
            result['paging'] = self.paging

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('objectCode') is not None:
            self.object_code = m.get('objectCode')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('paging') is not None:
            self.paging = m.get('paging')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

