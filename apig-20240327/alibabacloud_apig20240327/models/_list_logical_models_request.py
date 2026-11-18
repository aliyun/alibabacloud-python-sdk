# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLogicalModelsRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the gateway instance. Specifies the gateway instance for which to query logical models.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # The keyword used to filter logical models.
        self.keyword = keyword
        # The maximum number of entries to return per page. Valid values: 1 to 100. This parameter is required. This operation uses token-based pagination with maxResults and nextToken instead of pageNumber and pageSize.
        # 
        # This parameter is required.
        self.max_results = max_results
        # The nextToken value returned in the response of the previous page. Omit this parameter for the first page. The last page does not return a nextToken value.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

