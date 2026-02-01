# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClustersRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_status: str = None,
        cluster_type: str = None,
        current: int = None,
        id: str = None,
        name: str = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_status = cluster_status
        self.cluster_type = cluster_type
        self.current = current
        self.id = id
        self.name = name
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

        if self.cluster_status is not None:
            result['cluster_status'] = self.cluster_status

        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type

        if self.current is not None:
            result['current'] = self.current

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('cluster_status') is not None:
            self.cluster_status = m.get('cluster_status')

        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

