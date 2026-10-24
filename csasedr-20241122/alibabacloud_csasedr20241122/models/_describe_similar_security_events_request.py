# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSimilarSecurityEventsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        task_id: int = None,
    ):
        # The page number of the returned results. Default value: **1**.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The maximum number of entries to return in a single query. This parameter is reserved for compatibility. The backend currently uses CurrentPage and PageSize for pagination.
        self.max_results = max_results
        # The token that is used to start the query. You can obtain the token from the result of the previous request.
        self.next_token = next_token
        # The Settings for the number of alerting events displayed on each page in a paged query. Default value: **20**, which indicates that 20 alerting events are displayed per paging.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the query task. You can call the [CreateSimilarSecurityEventsQueryTask](~~CreateSimilarSecurityEventsQueryTask~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

