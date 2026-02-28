# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnAssignPrivateIpAddressRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        ip_name: str = None,
        network_interface_id: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        subnet_id: str = None,
    ):
        # By default, popApi is not ignored and idempotent
        self.client_token = client_token
        # IP unique identifier
        # 
        # This parameter is required.
        self.ip_name = ip_name
        # Lingjun network interface controller ID
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        # The private IP address of the instance.
        self.private_ip_address = private_ip_address
        # Region
        # 
        # This parameter is required.
        self.region_id = region_id
        # Subnet
        # 
        # This parameter is required.
        self.subnet_id = subnet_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.ip_name is not None:
            result['IpName'] = self.ip_name

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        return self

