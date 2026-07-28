# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTerraformProviderVersionsRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        usage: str = None,
    ):
        # The keyword for searching versions. Fuzzy match is supported.
        self.keyword = keyword
        # The maximum number of records to retrieve in a single request.
        self.max_results = max_results
        # The pagination token for the next page. A value of null indicates that no more pages are available.
        self.next_token = next_token
        # The usage. Set to Explorer to retrieve meta information.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

