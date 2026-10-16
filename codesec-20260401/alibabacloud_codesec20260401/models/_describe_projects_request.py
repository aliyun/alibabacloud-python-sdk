# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProjectsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        query: str = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # The number of entries per page. Default value: 10. Maximum value: 20.
        self.max_results = max_results
        # The pagination token. Do not specify this parameter or set it to an empty string for the first page. For subsequent pages, pass the nextToken value from the previous response without any modification. If the nextToken value in the response is empty, the last page has been reached.
        self.next_token = next_token
        # The keyword used for fuzzy match by project name or prompt.
        self.query = query
        # The field by which to sort the results. Default value: last_scan_time.
        # 
        # Valid values:
        # 
        # *   last_scan_time: the time when a task was last created.
        # *   created_at: the time when the project was created.
        # *   updated_at: the time when the project was last modified.
        self.sort_by = sort_by
        # The sort order. Default value: desc.
        # 
        # Valid values:
        # 
        # *   desc: descending order.
        # *   asc: ascending order.
        self.sort_order = sort_order

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

        if self.sort_by is not None:
            result['sortBy'] = self.sort_by

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        return self

