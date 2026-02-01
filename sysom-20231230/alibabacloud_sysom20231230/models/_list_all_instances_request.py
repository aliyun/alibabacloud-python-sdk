# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAllInstancesRequest(DaraModel):
    def __init__(
        self,
        current: str = None,
        filters: str = None,
        instance_type: str = None,
        managed_type: str = None,
        max_results: int = None,
        next_token: str = None,
        page_size: str = None,
        plugin_id: str = None,
        region: str = None,
    ):
        self.current = current
        self.filters = filters
        self.instance_type = instance_type
        self.managed_type = managed_type
        self.max_results = max_results
        self.next_token = next_token
        self.page_size = page_size
        self.plugin_id = plugin_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['current'] = self.current

        if self.filters is not None:
            result['filters'] = self.filters

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.managed_type is not None:
            result['managedType'] = self.managed_type

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('filters') is not None:
            self.filters = m.get('filters')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('managedType') is not None:
            self.managed_type = m.get('managedType')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

