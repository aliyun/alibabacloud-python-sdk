# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class SwitchSecurityProxyRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        nat_route_entry_list: List[main_models.SwitchSecurityProxyRequestNatRouteEntryList] = None,
        proxy_id: str = None,
        route_action: str = None,
        switch: str = None,
    ):
        # The language of the request and response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The route entry list for routing to be redirected or un-redirected. Maximum number of entries: 10,000. When RouteAction (divert or undivert) is specified, a non-empty list must be provided and used according to the incremental semantics. Each entry must include the RouteTableId, DestinationCidr, NextHopId, and NextHopType fields, and the combination of RouteTableId and DestinationCidr must be unique. In the Gateway Load Balancer (GWLB) architecture, when committed together with Switch=open, this parameter is used to specify the route entry for which traffic redirection is enabled in the current request. If no list is provided, the saved list is used. If no active list exists, a parameter error is returned.
        self.nat_route_entry_list = nat_route_entry_list
        # The ID of the NAT firewall.
        # 
        # This parameter is required.
        self.proxy_id = proxy_id
        # Makes incremental traffic redirection changes to the route entry passed in this request. Other redirected route tables in the list are not affected. Valid values: divert (enables traffic redirection for the passed route entry) and undivert (shutdown of traffic redirection for the passed route entry). This parameter is active only when the firewall is in the traffic redirection state (normal). This parameter and Switch are mutually exclusive and cannot be both set to non-empty values at the same time. If this parameter is not specified or is set to an empty string, the incremental semantics are not used.
        self.route_action = route_action
        # The security protection switch. Valid values:
        # - open: Enabled.
        # - close: Disabled.
        # 
        # This parameter is required.
        self.switch = switch

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
        if self.lang is not None:
            result['Lang'] = self.lang

        result['NatRouteEntryList'] = []
        if self.nat_route_entry_list is not None:
            for k1 in self.nat_route_entry_list:
                result['NatRouteEntryList'].append(k1.to_map() if k1 else None)

        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id

        if self.route_action is not None:
            result['RouteAction'] = self.route_action

        if self.switch is not None:
            result['Switch'] = self.switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        self.nat_route_entry_list = []
        if m.get('NatRouteEntryList') is not None:
            for k1 in m.get('NatRouteEntryList'):
                temp_model = main_models.SwitchSecurityProxyRequestNatRouteEntryList()
                self.nat_route_entry_list.append(temp_model.from_map(k1))

        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')

        if m.get('RouteAction') is not None:
            self.route_action = m.get('RouteAction')

        if m.get('Switch') is not None:
            self.switch = m.get('Switch')

        return self

class SwitchSecurityProxyRequestNatRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        route_table_id: str = None,
    ):
        # The destination CIDR block of the route entry. When RouteAction is specified, only the default route 0.0.0.0/0 is supported. If other CIDR blocks are passed, a parameter error is returned.
        # 
        # This parameter is required.
        self.destination_cidr = destination_cidr
        # The ID of the NAT gateway to which the route entry pointed before traffic redirection. You can obtain the ID by calling the DescribeSecurityProxyResources operation. When RouteAction is specified, this value must be consistent with the NAT gateway involved in the current operation. When traffic redirection is disabled, you must still pass this NAT gateway ID instead of the current next hop ID of the firewall.
        # 
        # This parameter is required.
        self.next_hop_id = next_hop_id
        # The next hop type of the route entry before traffic redirection. When RouteAction is specified, this value is fixed to NatGateway and must be passed in pairs with NextHopId. If other values are passed, a parameter error is returned.
        # 
        # This parameter is required.
        self.next_hop_type = next_hop_type
        # The ID of the route table to which the route entry belongs. The route table must exist in the user\\"s VPC. This parameter and DestinationCidr are used together to locate a route. If the route does not exist, the task fails and a message indicating that the route entry does not exist is returned.
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

