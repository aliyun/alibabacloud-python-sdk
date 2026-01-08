# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class CreateSecurityProxyRequest(DaraModel):
    def __init__(
        self,
        firewall_switch: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
        nat_route_entry_list: List[main_models.CreateSecurityProxyRequestNatRouteEntryList] = None,
        proxy_name: str = None,
        region_no: str = None,
        strict_mode: int = None,
        vpc_id: str = None,
        vswitch_auto: str = None,
        vswitch_cidr: str = None,
        vswitch_id: str = None,
    ):
        # The status of the NAT firewall. Valid values:
        # 
        # *   **open**: enabled
        # *   **close**: disabled
        self.firewall_switch = firewall_switch
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The routes to be switched to the NAT gateway.
        # 
        # This parameter is required.
        self.nat_route_entry_list = nat_route_entry_list
        # The name of the NAT firewall. The name must be 4 to 50 characters in length, and can contain letters, digits, and underscores (_). However, it cannot start with an underscore.
        # 
        # This parameter is required.
        self.proxy_name = proxy_name
        # The region ID of the virtual private cloud (VPC).
        # 
        # >  For more information about Cloud Firewall supported regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        # 
        # This parameter is required.
        self.region_no = region_no
        # Specifies whether to enable the strict mode. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.strict_mode = strict_mode
        # The ID of the VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The mode of the vSwitch that you want to use. Valid values:
        # 
        # *   **true**: automatic
        # *   **false**: manual
        self.vswitch_auto = vswitch_auto
        # The CIDR block of the vSwitch.
        self.vswitch_cidr = vswitch_cidr
        # The ID of the vSwitch. This parameter is required if you set the VswitchAuto parameter to true.
        self.vswitch_id = vswitch_id

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
        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        result['NatRouteEntryList'] = []
        if self.nat_route_entry_list is not None:
            for k1 in self.nat_route_entry_list:
                result['NatRouteEntryList'].append(k1.to_map() if k1 else None)

        if self.proxy_name is not None:
            result['ProxyName'] = self.proxy_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_auto is not None:
            result['VswitchAuto'] = self.vswitch_auto

        if self.vswitch_cidr is not None:
            result['VswitchCidr'] = self.vswitch_cidr

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        self.nat_route_entry_list = []
        if m.get('NatRouteEntryList') is not None:
            for k1 in m.get('NatRouteEntryList'):
                temp_model = main_models.CreateSecurityProxyRequestNatRouteEntryList()
                self.nat_route_entry_list.append(temp_model.from_map(k1))

        if m.get('ProxyName') is not None:
            self.proxy_name = m.get('ProxyName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchAuto') is not None:
            self.vswitch_auto = m.get('VswitchAuto')

        if m.get('VswitchCidr') is not None:
            self.vswitch_cidr = m.get('VswitchCidr')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class CreateSecurityProxyRequestNatRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        route_table_id: str = None,
    ):
        # The destination CIDR block of the default route.
        # 
        # This parameter is required.
        self.destination_cidr = destination_cidr
        # The next hop of the original NAT gateway.
        # 
        # This parameter is required.
        self.next_hop_id = next_hop_id
        # The network type of the next hop. Set the value to NatGateway.
        # 
        # This parameter is required.
        self.next_hop_type = next_hop_type
        # The route table to which the default route of the NAT gateway belongs.
        # 
        # This parameter is required.
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

