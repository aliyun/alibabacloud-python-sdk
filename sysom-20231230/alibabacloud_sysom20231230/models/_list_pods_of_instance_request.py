# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPodsOfInstanceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        current: int = None,
        instance: str = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.current = current
        self.instance = instance
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.current is not None:
            result['current'] = self.current

        if self.instance is not None:
            result['instance'] = self.instance

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

