# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SpotStockInternalInfo(DaraModel):
    def __init__(
        self,
        available_quantity: int = None,
        cluster_id: str = None,
        hpn_zone: str = None,
        total_quantity: int = None,
    ):
        # The number of available Spot Instances.
        self.available_quantity = available_quantity
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The ID of the high-performance network (HPN) zone.
        self.hpn_zone = hpn_zone
        # The total number of Spot Instances.
        self.total_quantity = total_quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_quantity is not None:
            result['availableQuantity'] = self.available_quantity

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.hpn_zone is not None:
            result['hpnZone'] = self.hpn_zone

        if self.total_quantity is not None:
            result['totalQuantity'] = self.total_quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availableQuantity') is not None:
            self.available_quantity = m.get('availableQuantity')

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('hpnZone') is not None:
            self.hpn_zone = m.get('hpnZone')

        if m.get('totalQuantity') is not None:
            self.total_quantity = m.get('totalQuantity')

        return self

