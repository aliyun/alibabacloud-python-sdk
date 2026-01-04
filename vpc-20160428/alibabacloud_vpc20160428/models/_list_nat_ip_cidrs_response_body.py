# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListNatIpCidrsResponseBody(DaraModel):
    def __init__(
        self,
        nat_ip_cidrs: List[main_models.ListNatIpCidrsResponseBodyNatIpCidrs] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The CIDR blocks of the NAT gateway.
        self.nat_ip_cidrs = nat_ip_cidrs
        # The token that is used for the next query. Valid values:
        # 
        # *   If the value of **NextToken** is not returned, it indicates that no next query is to be sent.
        # *   If the value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The number of CIDR blocks that are returned.
        self.total_count = total_count

    def validate(self):
        if self.nat_ip_cidrs:
            for v1 in self.nat_ip_cidrs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NatIpCidrs'] = []
        if self.nat_ip_cidrs is not None:
            for k1 in self.nat_ip_cidrs:
                result['NatIpCidrs'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nat_ip_cidrs = []
        if m.get('NatIpCidrs') is not None:
            for k1 in m.get('NatIpCidrs'):
                temp_model = main_models.ListNatIpCidrsResponseBodyNatIpCidrs()
                self.nat_ip_cidrs.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNatIpCidrsResponseBodyNatIpCidrs(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        is_default: bool = None,
        nat_gateway_id: str = None,
        nat_ip_cidr: str = None,
        nat_ip_cidr_description: str = None,
        nat_ip_cidr_id: str = None,
        nat_ip_cidr_name: str = None,
        nat_ip_cidr_status: str = None,
    ):
        # The time when the CIDR block was created.
        self.creation_time = creation_time
        # Indicates whether the CIDR block is the default CIDR block of the NAT gateway. Valid values:
        # 
        # *   **true**: The CIDR block is the default CIDR block of the NAT gateway.
        # *   **false**: The CIDR block is not the default CIDR block of the NAT gateway.
        self.is_default = is_default
        # The ID of the VPC NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The CIDR block of the NAT gateway.
        self.nat_ip_cidr = nat_ip_cidr
        # The description of the CIDR block of the NAT gateway.
        self.nat_ip_cidr_description = nat_ip_cidr_description
        # The ID of the CIDR block of the NAT gateway.
        self.nat_ip_cidr_id = nat_ip_cidr_id
        # The name of the CIDR block of the NAT gateway.
        self.nat_ip_cidr_name = nat_ip_cidr_name
        # The status of the CIDR block of the NAT gateway. If **Available** is returned, it indicates that the CIDR block is available.
        self.nat_ip_cidr_status = nat_ip_cidr_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

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

        return self

