# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListGatewayWebsocketEventsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListGatewayWebsocketEventsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The business response code.
        self.code = code
        # The query results.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListGatewayWebsocketEventsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGatewayWebsocketEventsResponseBodyData(DaraModel):
    def __init__(
        self,
        basis: str = None,
        has_more: bool = None,
        items: List[Dict[str, Any]] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The data basis.
        self.basis = basis
        # Indicates whether there is a next page.
        self.has_more = has_more
        # The observability events.
        self.items = items
        # The actual number of results per page.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basis is not None:
            result['basis'] = self.basis

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.items is not None:
            result['items'] = self.items

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basis') is not None:
            self.basis = m.get('basis')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('items') is not None:
            self.items = m.get('items')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

