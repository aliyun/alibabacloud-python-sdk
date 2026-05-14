# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableWarehouseAutoScaleRequest(DaraModel):
    def __init__(
        self,
        max_cluster_count: str = None,
        name: str = None,
    ):
        self.max_cluster_count = max_cluster_count
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_cluster_count is not None:
            result['maxClusterCount'] = self.max_cluster_count

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxClusterCount') is not None:
            self.max_cluster_count = m.get('maxClusterCount')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

