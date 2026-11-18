# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConsumerConsoleSummariesRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        gateway_id: str = None,
        max_results: int = None,
        name_like: str = None,
        next_token: str = None,
    ):
        # The filter condition. Valid values: all, granted, and disabled. Default value: all.
        self.filter = filter
        # The target AI gateway instance ID. Consumer identities are shared across the region, while authorizations are isolated by instance.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # The maximum number of entries to return on each page. Valid values: 1 to 100. This parameter is required. Token-based pagination is used instead of pageNumber and pageSize.
        # 
        # This parameter is required.
        self.max_results = max_results
        # The keyword for fuzzy search by consumer name. This parameter does not affect the total count.
        self.name_like = name_like
        # The pagination token returned from the previous page. Omit this parameter when querying the first page. An empty or omitted value indicates the last page.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.name_like is not None:
            result['nameLike'] = self.name_like

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

