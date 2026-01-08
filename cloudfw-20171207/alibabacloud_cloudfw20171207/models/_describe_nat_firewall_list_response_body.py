# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeNatFirewallListResponseBody(DaraModel):
    def __init__(
        self,
        nat_firewall_list: List[main_models.DescribeNatFirewallListResponseBodyNatFirewallList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The NAT firewalls.
        self.nat_firewall_list = nat_firewall_list
        # The request ID.
        self.request_id = request_id
        # The total number of NAT firewalls.
        self.total_count = total_count

    def validate(self):
        if self.nat_firewall_list:
            for v1 in self.nat_firewall_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NatFirewallList'] = []
        if self.nat_firewall_list is not None:
            for k1 in self.nat_firewall_list:
                result['NatFirewallList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nat_firewall_list = []
        if m.get('NatFirewallList') is not None:
            for k1 in m.get('NatFirewallList'):
                temp_model = main_models.DescribeNatFirewallListResponseBodyNatFirewallList()
                self.nat_firewall_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNatFirewallListResponseBodyNatFirewallList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        error_detail: str = None,
        member_uid: int = None,
        nat_gateway_id: str = None,
        nat_gateway_name: str = None,
        nat_route_entry_list: List[main_models.DescribeNatFirewallListResponseBodyNatFirewallListNatRouteEntryList] = None,
        proxy_id: str = None,
        proxy_name: str = None,
        proxy_network_interface_id: str = None,
        proxy_route_table_id: str = None,
        proxy_status: str = None,
        proxy_vswitch_id: str = None,
        region_id: str = None,
        strict_mode: int = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The UID of the Alibaba Cloud account.
        # 
        # >  The value of this parameter indicates the management account to which the member is added.
        self.ali_uid = ali_uid
        # The cause of the error.
        self.error_detail = error_detail
        # The UID of the member in Cloud Firewall.
        self.member_uid = member_uid
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The name of the NAT gateway.
        self.nat_gateway_name = nat_gateway_name
        # The default route entries of the NAT gateway.
        self.nat_route_entry_list = nat_route_entry_list
        # The ID of the NAT firewall.
        self.proxy_id = proxy_id
        # The name of the NAT firewall.
        self.proxy_name = proxy_name
        self.proxy_network_interface_id = proxy_network_interface_id
        self.proxy_route_table_id = proxy_route_table_id
        # The status of the NAT firewall. Valid values:
        # 
        # *   configuring
        # *   deleting
        # *   normal
        # *   abnormal
        # *   opening
        # *   closing
        # *   closed
        self.proxy_status = proxy_status
        self.proxy_vswitch_id = proxy_vswitch_id
        # The region ID of your Cloud Firewall.
        # 
        # >  For more information about the supported regions of Cloud Firewall, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_id = region_id
        # Indicates whether the strict mode is enabled. Valid values: 1, which specifies yes, and 0, which specifies no.
        self.strict_mode = strict_mode
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.nat_route_entry_list:
            for v1 in self.nat_route_entry_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_name is not None:
            result['NatGatewayName'] = self.nat_gateway_name

        result['NatRouteEntryList'] = []
        if self.nat_route_entry_list is not None:
            for k1 in self.nat_route_entry_list:
                result['NatRouteEntryList'].append(k1.to_map() if k1 else None)

        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id

        if self.proxy_name is not None:
            result['ProxyName'] = self.proxy_name

        if self.proxy_network_interface_id is not None:
            result['ProxyNetworkInterfaceId'] = self.proxy_network_interface_id

        if self.proxy_route_table_id is not None:
            result['ProxyRouteTableId'] = self.proxy_route_table_id

        if self.proxy_status is not None:
            result['ProxyStatus'] = self.proxy_status

        if self.proxy_vswitch_id is not None:
            result['ProxyVSwitchId'] = self.proxy_vswitch_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayName') is not None:
            self.nat_gateway_name = m.get('NatGatewayName')

        self.nat_route_entry_list = []
        if m.get('NatRouteEntryList') is not None:
            for k1 in m.get('NatRouteEntryList'):
                temp_model = main_models.DescribeNatFirewallListResponseBodyNatFirewallListNatRouteEntryList()
                self.nat_route_entry_list.append(temp_model.from_map(k1))

        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')

        if m.get('ProxyName') is not None:
            self.proxy_name = m.get('ProxyName')

        if m.get('ProxyNetworkInterfaceId') is not None:
            self.proxy_network_interface_id = m.get('ProxyNetworkInterfaceId')

        if m.get('ProxyRouteTableId') is not None:
            self.proxy_route_table_id = m.get('ProxyRouteTableId')

        if m.get('ProxyStatus') is not None:
            self.proxy_status = m.get('ProxyStatus')

        if m.get('ProxyVSwitchId') is not None:
            self.proxy_vswitch_id = m.get('ProxyVSwitchId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeNatFirewallListResponseBodyNatFirewallListNatRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        route_table_id: str = None,
    ):
        # The destination CIDR block of the default route.
        self.destination_cidr = destination_cidr
        # The next hop of the original NAT gateway.
        self.next_hop_id = next_hop_id
        # The network type of the next hop. The value is fixed as NatGateway.
        self.next_hop_type = next_hop_type
        # The route table to which the default route of the NAT gateway belongs.
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

