# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScansRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        query: str = None,
        status: str = None,
        task_name: str = None,
    ):
        # The maximum number of entries per page. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The pagination token. To query the first page, leave this parameter empty or do not specify it. To query subsequent pages, pass the nextToken value returned in the previous response. If the nextToken value in the response is empty, the last page is returned.
        self.next_token = next_token
        # The query string. You can perform a fuzzy match by project name or prompt.
        self.query = query
        # The status of the task. Valid values:
        # * running: The task is running.
        # * completed: The task is completed.
        # * failed: The task failed.
        self.status = status
        # The name of the task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.query is not None:
            result['query'] = self.query

        if self.status is not None:
            result['status'] = self.status

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

