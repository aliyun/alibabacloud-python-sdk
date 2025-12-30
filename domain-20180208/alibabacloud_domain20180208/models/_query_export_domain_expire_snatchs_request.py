# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryExportDomainExpireSnatchsRequest(DaraModel):
    def __init__(
        self,
        current_id: int = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.current_id = current_id
        self.max_results = max_results
        # This parameter is required.
        self.next_token = next_token
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_id is not None:
            result['CurrentId'] = self.current_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentId') is not None:
            self.current_id = m.get('CurrentId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

