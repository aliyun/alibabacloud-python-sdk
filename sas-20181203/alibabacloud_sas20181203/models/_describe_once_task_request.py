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
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The timestamp when the root task ends. Unit: milliseconds.
        self.end_time_query = end_time_query
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The ID of the root task.
        # 
        # > You must specify at least one of the **TaskType** and **RootTaskId** parameters.
        self.root_task_id = root_task_id
        # The source of the task. Valid values include the following values:
        # 
        # *   **schedule**: automatic scheduling of Cloud Security Scanner.
        # *   **console**: one-click detection in the Cloud Security Scanner console.
        self.source = source
        # The timestamp when the root task starts. Unit: milliseconds.
        self.start_time_query = start_time_query
        # The ID of the task.
        self.task_id = task_id
        # The type of the task. Valid values:
        # 
        # *   **CLIENT_PROBLEM_CHECK**: a task of the Security Center agent
        # *   **CLIENT_DEV_OPS**: an O\\&M task of Cloud Assistant
        # *   **ASSET_SECURITY_CHECK**: a task of asset information collection
        # 
        # > You must specify at least one of the **TaskType** and **RootTaskId** parameters.
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

