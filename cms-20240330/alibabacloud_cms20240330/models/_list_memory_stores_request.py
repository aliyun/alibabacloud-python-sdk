# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMemoryStoresRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        memory_store_name: str = None,
        next_token: str = None,
    ):
        # The maximum number of results to return. The maximum value is 200.
        self.max_results = max_results
        # The name of the memory store.
        self.memory_store_name = memory_store_name
        # The token for the next page of results.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.memory_store_name is not None:
            result['memoryStoreName'] = self.memory_store_name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('memoryStoreName') is not None:
            self.memory_store_name = m.get('memoryStoreName')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

