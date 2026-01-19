# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTaskLogListRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        is_page: bool = None,
        lang: str = None,
        page_size: str = None,
        task_id: str = None,
        task_log_id: str = None,
        reg_id: str = None,
    ):
        # Current page.
        self.current_page = current_page
        # Whether to paginate.
        self.is_page = is_page
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Page size.
        self.page_size = page_size
        # Task ID.
        self.task_id = task_id
        # Task log ID
        self.task_log_id = task_log_id
        # Region code
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.is_page is not None:
            result['IsPage'] = self.is_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_log_id is not None:
            result['TaskLogId'] = self.task_log_id

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IsPage') is not None:
            self.is_page = m.get('IsPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskLogId') is not None:
            self.task_log_id = m.get('TaskLogId')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

