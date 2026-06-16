# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeListPocRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        reg_id: str = None,
        task_name: str = None,
        task_status: str = None,
        type: str = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The number of entries per page.
        self.page_size = page_size
        # The region code.
        self.reg_id = reg_id
        # The task name.
        self.task_name = task_name
        # The execution status of the import task. Valid values:
        # - DOING: running
        # - FINISH: completed.
        self.task_status = task_status
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

