# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceStatusRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        current: int = None,
        instance: str = None,
        page_size: int = None,
        region: str = None,
        status: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The current page number (starting from 1). This field is present when pagination is used.
        self.current = current
        # The instance ID.
        self.instance = instance
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region ID.
        self.region = region
        # Filters the instance list by status. If this field is specified, only instances with the corresponding status are returned.
        self.status = status
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

        if self.instance is not None:
            result['instance'] = self.instance

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.region is not None:
            result['region'] = self.region

        if self.status is not None:
            result['status'] = self.status

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

