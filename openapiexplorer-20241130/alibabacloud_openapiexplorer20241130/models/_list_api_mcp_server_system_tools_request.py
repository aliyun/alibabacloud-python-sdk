# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApiMcpServerSystemToolsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        skip: int = None,
    ):
        # The maximum number of entries to return on each page. The maximum value is 100. The default value is 20.
        self.max_results = max_results
        # The token to start the next query. Set this parameter to the NextToken value returned by the last API call.
        # 
        # > Do not specify this parameter for the first query. If a query does not return all results, pass the NextToken value from the previous response to the next query to continue.
        self.next_token = next_token
        # The number of entries to skip.
        self.skip = skip

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

        if self.skip is not None:
            result['skip'] = self.skip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('skip') is not None:
            self.skip = m.get('skip')

        return self

