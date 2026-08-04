# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class ListServiceTaskResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_tasks: List[Dict[str, Any]] = None,
        total_count: int = None,
    ):
        # The maxResults value of the current request.
        self.max_results = max_results
        # The pagination token for the next page. An encrypted hexadecimal string is returned when a next page exists. An empty value or absence of this field indicates no more data. Pass this value as-is in the nextToken parameter for the next page request.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of tasks.
        self.service_tasks = service_tasks
        # The total number of entries that match the conditions.
        self.total_count = total_count

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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.service_tasks is not None:
            result['serviceTasks'] = self.service_tasks

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('serviceTasks') is not None:
            self.service_tasks = m.get('serviceTasks')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

