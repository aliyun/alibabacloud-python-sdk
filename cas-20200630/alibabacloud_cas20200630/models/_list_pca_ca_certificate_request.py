# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPcaCaCertificateRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        # The maximum number of entries to return on each page. The default value is 20.
        # 
        # Valid values: 1 to 2000.
        self.max_results = max_results
        # The token for the next page of results. Leave this parameter empty to start the query from the first page. If this parameter is not returned, all results have been returned.
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

