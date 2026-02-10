# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeOnceTaskLeafRecordPageRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        relate_info: bool = None,
        source: str = None,
        start_time: int = None,
        status_list: List[str] = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The number of the page to return.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end timestamp of the sub-task.
        self.end_time = end_time
        # The number of entries to return on each page. Default value: 20
        # 
        # This parameter is required.
        self.page_size = page_size
        # Specifies whether extension information is associated.
        # 
        # This parameter is required.
        self.relate_info = relate_info
        # The source of the request.
        self.source = source
        # The start timestamp of the sub-task.
        self.start_time = start_time
        # The status information.
        self.status_list = status_list
        # The ID of the sub-task.
        self.task_id = task_id
        # The type of the sub-task. Valid values:
        # 
        # *   **IMAGE_SCAN**: image scan task
        # *   **IMAGE_REGISTRY_PULL**: image asset synchronization task
        # 
        # This parameter is required.
        self.task_type = task_type

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

        if self.relate_info is not None:
            result['RelateInfo'] = self.relate_info

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RelateInfo') is not None:
            self.relate_info = m.get('RelateInfo')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

