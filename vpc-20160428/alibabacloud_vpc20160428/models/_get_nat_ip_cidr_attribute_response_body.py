# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNatIpCidrAttributeResponseBody(DaraModel):
    def __init__(
        self,
        nat_gateway_id: str = None,
        nat_ip_cidr: str = None,
        nat_ip_cidr_description: str = None,
        nat_ip_cidr_id: str = None,
        nat_ip_cidr_name: str = None,
        nat_ip_cidr_status: str = None,
        request_id: str = None,
    ):
        # The ID of the VPC NAT gateway instance to which the queried NAT IP address range belongs.
        self.nat_gateway_id = nat_gateway_id
        # The queried NAT IP address range.
        self.nat_ip_cidr = nat_ip_cidr
        # Description of the queried NAT IP address range.
        self.nat_ip_cidr_description = nat_ip_cidr_description
        # The instance ID of the queried NAT IP address range.
        self.nat_ip_cidr_id = nat_ip_cidr_id
        # The name of the queried NAT IP address range.
        self.nat_ip_cidr_name = nat_ip_cidr_name
        # The status of the queried NAT IP address segment. Values:
        # - Available: Available status.
        # - Deleting: In the process of being deleted.
        # - Creating: In the process of being created.
        self.nat_ip_cidr_status = nat_ip_cidr_status
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_ip_cidr is not None:
            result['NatIpCidr'] = self.nat_ip_cidr

        if self.nat_ip_cidr_description is not None:
            result['NatIpCidrDescription'] = self.nat_ip_cidr_description

        if self.nat_ip_cidr_id is not None:
            result['NatIpCidrId'] = self.nat_ip_cidr_id

        if self.nat_ip_cidr_name is not None:
            result['NatIpCidrName'] = self.nat_ip_cidr_name

        if self.nat_ip_cidr_status is not None:
            result['NatIpCidrStatus'] = self.nat_ip_cidr_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatIpCidr') is not None:
            self.nat_ip_cidr = m.get('NatIpCidr')

        if m.get('NatIpCidrDescription') is not None:
            self.nat_ip_cidr_description = m.get('NatIpCidrDescription')

        if m.get('NatIpCidrId') is not None:
            self.nat_ip_cidr_id = m.get('NatIpCidrId')

        if m.get('NatIpCidrName') is not None:
            self.nat_ip_cidr_name = m.get('NatIpCidrName')

        if m.get('NatIpCidrStatus') is not None:
            self.nat_ip_cidr_status = m.get('NatIpCidrStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

