# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigureNatGatewayRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        eip_allocation_id: str = None,
        eip_bandwidth: int = None,
        instance_id: str = None,
        nat_gateway_instance_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.eip_allocation_id = eip_allocation_id
        self.eip_bandwidth = eip_bandwidth
        # This parameter is required.
        self.instance_id = instance_id
        self.nat_gateway_instance_id = nat_gateway_instance_id

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

        if self.eip_allocation_id is not None:
            result['EipAllocationId'] = self.eip_allocation_id

        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nat_gateway_instance_id is not None:
            result['NatGatewayInstanceId'] = self.nat_gateway_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EipAllocationId') is not None:
            self.eip_allocation_id = m.get('EipAllocationId')

        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NatGatewayInstanceId') is not None:
            self.nat_gateway_instance_id = m.get('NatGatewayInstanceId')

        return self

