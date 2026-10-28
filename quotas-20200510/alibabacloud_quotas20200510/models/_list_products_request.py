# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        # The maximum number of entries to return for this query.
        # 
        # Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which the query starts. An empty value indicates that the query starts from the beginning.
        self.next_token = next_token

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

