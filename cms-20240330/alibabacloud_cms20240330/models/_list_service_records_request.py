# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceRecordsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        record_type: str = None,
        search: str = None,
    ):
        # The maximum number of entries to return. Maximum value: 200.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The type of the linked entry. Currently supported:
        # logCorrelation, which indicates application log association.
        # 
        # This parameter is required.
        self.record_type = record_type
        # The filter information for service-linked entries.
        self.search = search

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

        if self.record_type is not None:
            result['recordType'] = self.record_type

        if self.search is not None:
            result['search'] = self.search

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('recordType') is not None:
            self.record_type = m.get('recordType')

        if m.get('search') is not None:
            self.search = m.get('search')

        return self

