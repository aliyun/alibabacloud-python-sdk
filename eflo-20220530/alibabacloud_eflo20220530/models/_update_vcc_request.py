# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVccRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        order_id: str = None,
        region_id: str = None,
        vcc_id: str = None,
        vcc_name: str = None,
    ):
        # The peak bandwidth of the Lingjun connection instance. Unit: Mbit/s. Valid values: 1000 to 400000
        self.bandwidth = bandwidth
        # The ID of the order placed on the instance.
        self.order_id = order_id
        # The region ID.
        self.region_id = region_id
        # The ID of the Lingjun connection instance.
        # 
        # This parameter is required.
        self.vcc_id = vcc_id
        # The name of the Lingjun connection instance.
        self.vcc_name = vcc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id

        if self.vcc_name is not None:
            result['VccName'] = self.vcc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')

        if m.get('VccName') is not None:
            self.vcc_name = m.get('VccName')

        return self

