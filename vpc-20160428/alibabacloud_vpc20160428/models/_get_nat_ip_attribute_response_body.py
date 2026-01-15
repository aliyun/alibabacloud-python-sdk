# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNatIpAttributeResponseBody(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        nat_gateway_id: str = None,
        nat_ip: str = None,
        nat_ip_cidr: str = None,
        nat_ip_description: str = None,
        nat_ip_id: str = None,
        nat_ip_name: str = None,
        nat_ip_status: str = None,
        request_id: str = None,
    ):
        # The creation time of the queried NAT IP address.
        self.creation_time = creation_time
        # The ID of the VPC NAT gateway instance to which the queried NAT IP address belongs.
        self.nat_gateway_id = nat_gateway_id
        # The queried NAT IP address.
        self.nat_ip = nat_ip
        # The address range where the queried NAT IP address is located.
        self.nat_ip_cidr = nat_ip_cidr
        # Description of the queried NAT IP address.
        self.nat_ip_description = nat_ip_description
        # The ID of the queried NAT IP address instance.
        self.nat_ip_id = nat_ip_id
        # Name of the queried NAT IP address.
        self.nat_ip_name = nat_ip_name
        # The status of the queried NAT IP address. Values:
        # - **Available**: Available.
        #  - **Deleting**: Deleting.
        #  - **Creating**: Creating.
        self.nat_ip_status = nat_ip_status
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_ip is not None:
            result['NatIp'] = self.nat_ip

        if self.nat_ip_cidr is not None:
            result['NatIpCidr'] = self.nat_ip_cidr

        if self.nat_ip_description is not None:
            result['NatIpDescription'] = self.nat_ip_description

        if self.nat_ip_id is not None:
            result['NatIpId'] = self.nat_ip_id

        if self.nat_ip_name is not None:
            result['NatIpName'] = self.nat_ip_name

        if self.nat_ip_status is not None:
            result['NatIpStatus'] = self.nat_ip_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatIp') is not None:
            self.nat_ip = m.get('NatIp')

        if m.get('NatIpCidr') is not None:
            self.nat_ip_cidr = m.get('NatIpCidr')

        if m.get('NatIpDescription') is not None:
            self.nat_ip_description = m.get('NatIpDescription')

        if m.get('NatIpId') is not None:
            self.nat_ip_id = m.get('NatIpId')

        if m.get('NatIpName') is not None:
            self.nat_ip_name = m.get('NatIpName')

        if m.get('NatIpStatus') is not None:
            self.nat_ip_status = m.get('NatIpStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

