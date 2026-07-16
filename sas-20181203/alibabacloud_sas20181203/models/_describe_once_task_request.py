# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOnceTaskRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time_query: int = None,
        page_size: int = None,
        root_task_id: str = None,
        source: str = None,
        start_time_query: int = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The page number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The timestamp when the root task ends. Unit: milliseconds.
        self.end_time_query = end_time_query
        # The number of client tasks per page in a paged query. Default value: **20**.
        self.page_size = page_size
        # The root task ID.
        # > **TaskType** and **RootTaskId** cannot both be empty.
        self.root_task_id = root_task_id
        # The node source. Valid values include but are not limited to:
        # - **schedule**: automatic scheduling of vulnerability scanning
        # - **console**: one-click detection from the vulnerability scanning console
        self.source = source
        # The timestamp when the root task starts. Unit: milliseconds.
        self.start_time_query = start_time_query
        # The task ID.
        self.task_id = task_id
        # The node type. Valid values:
        # - **VUL_CHECK_TASK**: vulnerability scanning node
        # - **CLIENT_PROBLEM_CHECK**: client node
        # - **CLIENT_DEV_OPS**: cloud O&M node
        # - **ASSET_SECURITY_CHECK**: asset information collection node
        # > **TaskType** and **RootTaskId** cannot both be empty.
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

        if self.end_time_query is not None:
            result['EndTimeQuery'] = self.end_time_query

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.root_task_id is not None:
            result['RootTaskId'] = self.root_task_id

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time_query is not None:
            result['StartTimeQuery'] = self.start_time_query

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTimeQuery') is not None:
            self.end_time_query = m.get('EndTimeQuery')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RootTaskId') is not None:
            self.root_task_id = m.get('RootTaskId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTimeQuery') is not None:
            self.start_time_query = m.get('StartTimeQuery')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

