# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExportTasksRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The page number for paging. Pages start from 1. If this parameter is not specified or is set to a value less than 1, the first page is returned. The query results are sorted in descending order of task creation time, with the most recently created tasks listed first. When polling a single task by TaskId, we recommend that you explicitly set this parameter to 1.
        self.page_number = page_number
        # The number of tasks to return on each page. Default value: 200. If this parameter is set to a value less than 1, the value 10 is used. When polling a single task by TaskId, set this parameter to 1 to avoid returning redundant tasks.
        self.page_size = page_size
        # Filters export tasks by task ID. The value is the TaskId returned by CreateExportTask, which is a 32-character UUID string without hyphens. This parameter requires an exact match and does not support fuzzy queries. If this parameter is not specified, all tasks under the current account that meet other conditions are returned.
        self.task_id = task_id
        # Filters export tasks by task type. The value is case-sensitive and must be one of the following valid values:
        # - WUYING_SERVER_LIST: Wuying host list.
        # - USER_USAGE_REPORT: User usage report.
        # - BROWSER_BOOKMARK_LIST: Cloud browser bookmark list.
        # - BROWSER_RESTRICTED_URL_LIST: Cloud browser URL whitelist.
        # 
        # If this parameter is not specified, tasks are not filtered by type, and all tasks under the current account that meet other conditions are returned. If an unrecognized value is passed, the server does not return a parameter error but cancels the type filter. Therefore, you must pass the exact valid values listed above. When querying a single task by TaskId, omit this parameter.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

