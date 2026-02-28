# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNetworkInterfaceRequest(DaraModel):
    def __init__(
        self,
        network_interface_id: str = None,
        region_id: str = None,
        subnet_id: str = None,
    ):
        # Lingjun network interface controller ID
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Subnet of Lingjun
        self.subnet_id = subnet_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        return self

