# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeScheduledTasksRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        scheduled_ids: List[str] = None,
        status: str = None,
        task_name: str = None,
    ):
        # The list of instance IDs.
        self.instance_ids = instance_ids
        # The maximum number of entries to return in this request.
        self.max_results = max_results
        # The pagination token that indicates the position from which to start reading. Leave this parameter empty to read from the beginning.
        self.next_token = next_token
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The scheduled task IDs used to filter results.
        self.scheduled_ids = scheduled_ids
        # The status used to filter results. Valid values: ACTIVE and DISABLED.
        self.status = status
        # The task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scheduled_ids is not None:
            result['ScheduledIds'] = self.scheduled_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScheduledIds') is not None:
            self.scheduled_ids = m.get('ScheduledIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

