# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTasksRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        # The maximum number of entries to return per page. The valid range is 10 to 500. If this parameter is omitted or its value is less than 10, a default value of 10 is used. Values greater than 500 are treated as 500.
        self.max_results = max_results
        # A pagination token. To retrieve the next page of results, set this parameter to the `NextToken` value from the response of the previous API call. For more information, see the API description above.
        self.next_token = next_token
        # Specifies the status of tasks to query. If this parameter is omitted, the API returns tasks in all states. Valid values: `CREATED`, `RUNNING`, `COMPLETE`, `FAILED`, `EXPIRED`, and `CANCELED`.
        self.task_status = task_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

