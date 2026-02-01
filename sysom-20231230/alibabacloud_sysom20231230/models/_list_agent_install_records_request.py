# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentInstallRecordsRequest(DaraModel):
    def __init__(
        self,
        current: int = None,
        instance_id: str = None,
        page_size: int = None,
        plugin_id: str = None,
        plugin_version: str = None,
        region: str = None,
        status: str = None,
    ):
        self.current = current
        self.instance_id = instance_id
        self.page_size = page_size
        self.plugin_id = plugin_id
        self.plugin_version = plugin_version
        self.region = region
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['current'] = self.current

        if self.instance_id is not None:
            result['instance_id'] = self.instance_id

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.plugin_id is not None:
            result['plugin_id'] = self.plugin_id

        if self.plugin_version is not None:
            result['plugin_version'] = self.plugin_version

        if self.region is not None:
            result['region'] = self.region

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('plugin_id') is not None:
            self.plugin_id = m.get('plugin_id')

        if m.get('plugin_version') is not None:
            self.plugin_version = m.get('plugin_version')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

