# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLniPrivateIpAddressRequest(DaraModel):
    def __init__(
        self,
        ip_name: str = None,
        network_interface_id: str = None,
        region_id: str = None,
    ):
        # IP unique identifier
        # 
        # This parameter is required.
        self.ip_name = ip_name
        # Lingjun network interface controller ID
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_name is not None:
            result['IpName'] = self.ip_name

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

