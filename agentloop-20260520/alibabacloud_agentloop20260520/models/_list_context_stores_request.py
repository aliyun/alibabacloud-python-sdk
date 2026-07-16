# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListContextStoresRequest(DaraModel):
    def __init__(
        self,
        context_store_name: str = None,
        context_type: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # Filters context stores by name. Exact match is supported. If this parameter is not specified, no filtering is applied.
        self.context_store_name = context_store_name
        # Filters context stores by type, such as experience or memory. If this parameter is not specified, no filtering is applied.
        self.context_type = context_type
        # The maximum number of context stores to return. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The pagination token. Set this parameter to the nextToken value returned in the previous response to retrieve the next page. Do not specify this parameter for the first request.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_store_name is not None:
            result['contextStoreName'] = self.context_store_name

        if self.context_type is not None:
            result['contextType'] = self.context_type

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contextStoreName') is not None:
            self.context_store_name = m.get('contextStoreName')

        if m.get('contextType') is not None:
            self.context_type = m.get('contextType')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

