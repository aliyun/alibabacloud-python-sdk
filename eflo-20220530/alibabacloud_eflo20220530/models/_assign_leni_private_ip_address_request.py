# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssignLeniPrivateIpAddressRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        elastic_network_interface_id: str = None,
        private_ip_address: str = None,
        region_id: str = None,
    ):
        # The idempotent identifier.
        self.client_token = client_token
        # The description of the response code.
        self.description = description
        # Lingjun Elastic Network Interface ID.
        # 
        # This parameter is required.
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Elastic Network Interface secondary private network IP (automatically assigned by default).
        self.private_ip_address = private_ip_address
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

