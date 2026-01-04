# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListNatIpsResponseBody(DaraModel):
    def __init__(
        self,
        nat_ips: List[main_models.ListNatIpsResponseBodyNatIps] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The list of IP addresses of the NAT gateway.
        self.nat_ips = nat_ips
        # The token that is used for the next query. Valid values:
        # 
        # *   If the value of **NextToken** is not returned, it indicates that no next query is to be sent.
        # *   If the value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The number of IP addresses that are returned.
        self.total_count = total_count

    def validate(self):
        if self.nat_ips:
            for v1 in self.nat_ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NatIps'] = []
        if self.nat_ips is not None:
            for k1 in self.nat_ips:
                result['NatIps'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nat_ips = []
        if m.get('NatIps') is not None:
            for k1 in m.get('NatIps'):
                temp_model = main_models.ListNatIpsResponseBodyNatIps()
                self.nat_ips.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNatIpsResponseBodyNatIps(DaraModel):
    def __init__(
        self,
        ipv_4prefix: str = None,
        is_default: bool = None,
        nat_gateway_id: str = None,
        nat_ip: str = None,
        nat_ip_cidr: str = None,
        nat_ip_description: str = None,
        nat_ip_id: str = None,
        nat_ip_name: str = None,
        nat_ip_status: str = None,
    ):
        self.ipv_4prefix = ipv_4prefix
        # Indicates whether the IP address is the default IP address of the NAT gateway. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.is_default = is_default
        # The ID of the Virtual Private Cloud (VPC) NAT gateway to which the IP address is assigned.
        self.nat_gateway_id = nat_gateway_id
        # The IP address.
        self.nat_ip = nat_ip
        # The CIDR block to which the IP address belongs.
        self.nat_ip_cidr = nat_ip_cidr
        # The description of the IP address.
        self.nat_ip_description = nat_ip_description
        # The ID of the IP address.
        self.nat_ip_id = nat_ip_id
        # The name of the IP address.
        self.nat_ip_name = nat_ip_name
        # The status of the IP address. Valid values:
        # 
        # *   **Available**: available
        # *   **Deleted**: deleted
        # *   **Deleting**: deleting
        # *   **Creating**: creating
        # *   **Associated**: specified in an SNAT or DNAT entry
        # *   **Associating**: being specified in an SNAT or DNAT entry
        self.nat_ip_status = nat_ip_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4prefix is not None:
            result['Ipv4Prefix'] = self.ipv_4prefix

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Prefix') is not None:
            self.ipv_4prefix = m.get('Ipv4Prefix')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

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

        return self

