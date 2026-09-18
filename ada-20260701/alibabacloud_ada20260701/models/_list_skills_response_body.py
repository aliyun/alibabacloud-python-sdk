# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class ListSkillsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        skills: List[Any] = None,
        total: int = None,
    ):
        # The number of entries per page for the current cursor-based pagination.
        self.max_results = max_results
        # The token for the next page. An empty string is returned if there is no next page.
        self.next_token = next_token
        # The current page number for compatible page-number-based pagination.
        self.page_number = page_number
        # The number of entries per page for compatible page-number-based pagination.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of Skill summaries. The current public contract does not define a fixed structure for list items. For common fields, see "Supplementary description of response elements".
        self.skills = skills
        # The total number of Skills that match the current visibility and filter conditions.
        self.total = total

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skills is not None:
            result['Skills'] = self.skills

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Skills') is not None:
            self.skills = m.get('Skills')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

