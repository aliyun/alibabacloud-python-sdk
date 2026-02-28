# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssignPrivateIpAddressRequest(DaraModel):
    def __init__(
        self,
        assign_mac: bool = None,
        client_token: str = None,
        description: str = None,
        network_interface_id: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        skip_config: bool = None,
        subnet_id: str = None,
    ):
        # Specifies whether to assign a mac address.
        self.assign_mac = assign_mac
        # By default, popApi is not ignored and idempotent
        self.client_token = client_token
        # The description of the variable.
        self.description = description
        # The ID of the network interface controller.
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        # The secondary private IP address.
        self.private_ip_address = private_ip_address
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The default value is false. If you set the value to true, the secondary private IP address application process can be accelerated.
        # 
        # >  For more information, submit a ticket.
        self.skip_config = skip_config
        # It belongs to the Lingjun subnet.
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
        if self.assign_mac is not None:
            result['AssignMac'] = self.assign_mac

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.skip_config is not None:
            result['SkipConfig'] = self.skip_config

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignMac') is not None:
            self.assign_mac = m.get('AssignMac')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SkipConfig') is not None:
            self.skip_config = m.get('SkipConfig')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        return self

