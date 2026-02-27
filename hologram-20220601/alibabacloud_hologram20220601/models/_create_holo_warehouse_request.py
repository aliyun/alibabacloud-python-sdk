# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHoloWarehouseRequest(DaraModel):
    def __init__(
        self,
        cluster_count: int = None,
        cpu: str = None,
        name: str = None,
    ):
        self.cluster_count = cluster_count
        # The specifications of the virtual warehouse. The number of vCPUs must be an integer multiple of 16 CPUs. Minimum value: 16.
        # 
        # This parameter is required.
        self.cpu = cpu
        # The name of the virtual warehouse.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_count is not None:
            result['clusterCount'] = self.cluster_count

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterCount') is not None:
            self.cluster_count = m.get('clusterCount')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

