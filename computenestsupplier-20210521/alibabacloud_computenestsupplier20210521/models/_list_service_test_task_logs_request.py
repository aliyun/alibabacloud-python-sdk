# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceTestTaskLogsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        sort_order: str = None,
        task_id: str = None,
    ):
        # The number of items to return per page when paginating results. The maximum is 100, and the default is 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # Sort Order. Possible values:
        # 
        # + Ascending: Ascending order
        # 
        # + Descending (default value): Descending order
        self.sort_order = sort_order
        # The task ID.
        self.task_id = task_id

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

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

