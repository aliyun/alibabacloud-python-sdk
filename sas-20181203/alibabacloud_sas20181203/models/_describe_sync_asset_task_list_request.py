# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSyncAssetTaskListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        start_time: int = None,
        task_name: str = None,
    ):
        # The page number of the page to return. Default value: 1, which indicates that the first page is returned.
        self.current_page = current_page
        # The end timestamp of the IDC scan task to query. Unit: milliseconds.
        self.end_time = end_time
        # The maximum number of entries per page in a paged query. Default value: 20. If the PageSize parameter is left empty, 20 entries are returned by default.
        # > Do not leave PageSize empty.
        self.page_size = page_size
        # The start timestamp of the IDC scan task to query. Unit: milliseconds.
        self.start_time = start_time
        # The task name.
        self.task_name = task_name

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

        if self.task_name is not None:
            result['TaskName'] = self.task_name

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

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

