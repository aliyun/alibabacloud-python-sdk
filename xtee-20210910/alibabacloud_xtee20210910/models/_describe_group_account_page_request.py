# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGroupAccountPageRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        community_no: str = None,
        current_page: str = None,
        direction: str = None,
        field_key: str = None,
        field_val: str = None,
        is_page: bool = None,
        order: str = None,
        page_size: str = None,
        reg_id: str = None,
        task_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Community number.
        self.community_no = community_no
        # Current page number.
        self.current_page = current_page
        # Order direction.
        self.direction = direction
        # fieldKey.
        self.field_key = field_key
        # fieldVal.
        self.field_val = field_val
        # Whether to paginate.
        self.is_page = is_page
        # Sorting condition.
        self.order = order
        # Page size, default value is 10.
        self.page_size = page_size
        # Region code.
        self.reg_id = reg_id
        # Task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.community_no is not None:
            result['communityNo'] = self.community_no

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.direction is not None:
            result['direction'] = self.direction

        if self.field_key is not None:
            result['fieldKey'] = self.field_key

        if self.field_val is not None:
            result['fieldVal'] = self.field_val

        if self.is_page is not None:
            result['isPage'] = self.is_page

        if self.order is not None:
            result['order'] = self.order

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('communityNo') is not None:
            self.community_no = m.get('communityNo')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('fieldKey') is not None:
            self.field_key = m.get('fieldKey')

        if m.get('fieldVal') is not None:
            self.field_val = m.get('fieldVal')

        if m.get('isPage') is not None:
            self.is_page = m.get('isPage')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

