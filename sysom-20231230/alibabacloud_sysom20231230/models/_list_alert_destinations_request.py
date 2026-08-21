# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlertDestinationsRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        current: int = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        page_size: int = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The current page number (starting from 1).
        self.current = current
        # The maximum number of records to retrieve in a single request.
        self.max_results = max_results
        # The name of the alert contact.
        self.name = name
        # The pagination token for the next request.
        self.next_token = next_token
        # The number of records per page.
        self.page_size = page_size
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.current is not None:
            result['current'] = self.current

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.name is not None:
            result['name'] = self.name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

