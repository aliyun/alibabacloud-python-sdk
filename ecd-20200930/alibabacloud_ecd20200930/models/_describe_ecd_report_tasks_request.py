# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeEcdReportTasksRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        status: List[str] = None,
        sub_type: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_num = page_num
        # The number of entries returned per page. Maximum value: 200.
        self.page_size = page_size
        # The task status.
        # 
        # Valid values:
        # 
        # *   INIT: initializing
        # *   FAILED
        # *   RUNNING
        # *   EXPIRED
        # *   FINISHED
        self.status = status
        # The sub-type of the report export task.
        # 
        # Valid value:
        # 
        # *   DESKTOP: cloud computer
        self.sub_type = sub_type
        # The ID of the report export task.
        self.task_id = task_id
        # The type of the report.
        # 
        # Valid value:
        # 
        # *   RESOURCE_REPORT
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

