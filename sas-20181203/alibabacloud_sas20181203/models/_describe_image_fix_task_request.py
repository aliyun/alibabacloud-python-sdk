# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageFixTaskRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        start_time: int = None,
        status: str = None,
    ):
        # The number of the page to return. Default value: **1**
        # 
        # This parameter is required.
        self.current_page = current_page
        # The timestamp when the task ends. Unit: milliseconds.
        self.end_time = end_time
        # The number of entries to return on each page. Default value: **20**
        # 
        # This parameter is required.
        self.page_size = page_size
        # The timestamp when the task starts. Unit: milliseconds.
        self.start_time = start_time
        # The status of the task. Valid values:
        # 
        # *   **1**: The task is running.
        # *   **2**: The task is successful.
        # *   **3**: The task failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

