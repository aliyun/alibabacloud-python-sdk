# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSyncAssetTaskLogDetailRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        root_task_id: str = None,
        start_time: int = None,
        task_name: str = None,
    ):
        # The page number from which to start displaying query results. Default value: 1, which indicates that query results are displayed starting from page 1.
        self.current_page = current_page
        # The timestamp of the end time.
        self.end_time = end_time
        # The maximum number of entries to display on each page when you perform a paginated query. Default value: 20. If the PageSize parameter is left empty, 20 entries are returned by default.
        # > We recommend that you do not leave PageSize empty.
        self.page_size = page_size
        # The ID of the IDC scan task that you want to query. You can call the [DescribeSyncAssetTaskList](https://help.aliyun.com/document_detail/141932.html) operation to obtain the ID of an abnormal task.
        self.root_task_id = root_task_id
        # The timestamp of the start time.
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

        if self.root_task_id is not None:
            result['RootTaskId'] = self.root_task_id

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

        if m.get('RootTaskId') is not None:
            self.root_task_id = m.get('RootTaskId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

