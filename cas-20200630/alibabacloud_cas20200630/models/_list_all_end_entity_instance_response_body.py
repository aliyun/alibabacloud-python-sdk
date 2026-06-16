# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class ListAllEndEntityInstanceResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[Dict[str, Any]] = None,
        max_results: int = None,
        next_token: str = None,
        page_count: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The page number of the instance list.
        self.current_page = current_page
        # The list of instances.
        self.list = list
        # The maximum number of entries returned in this call.
        self.max_results = max_results
        # The token that you can use to retrieve the next page of results. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The total number of pages.
        self.page_count = page_count
        # The request ID.
        self.request_id = request_id
        # The maximum number of entries displayed on each page of a paged query.
        self.show_size = show_size
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.list is not None:
            result['List'] = self.list

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('List') is not None:
            self.list = m.get('List')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

