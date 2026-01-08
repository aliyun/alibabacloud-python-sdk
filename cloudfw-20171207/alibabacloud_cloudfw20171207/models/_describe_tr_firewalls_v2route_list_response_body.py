# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeTrFirewallsV2RouteListResponseBody(DaraModel):
    def __init__(
        self,
        firewall_route_detail_list: List[main_models.DescribeTrFirewallsV2RouteListResponseBodyFirewallRouteDetailList] = None,
        request_id: str = None,
    ):
        # The route tables of Cloud Firewall.
        self.firewall_route_detail_list = firewall_route_detail_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.firewall_route_detail_list:
            for v1 in self.firewall_route_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FirewallRouteDetailList'] = []
        if self.firewall_route_detail_list is not None:
            for k1 in self.firewall_route_detail_list:
                result['FirewallRouteDetailList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.firewall_route_detail_list = []
        if m.get('FirewallRouteDetailList') is not None:
            for k1 in m.get('FirewallRouteDetailList'):
                temp_model = main_models.DescribeTrFirewallsV2RouteListResponseBodyFirewallRouteDetailList()
                self.firewall_route_detail_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTrFirewallsV2RouteListResponseBodyFirewallRouteDetailList(DaraModel):
    def __init__(
        self,
        tr_firewall_route_destination: str = None,
        tr_firewall_route_nexthop: str = None,
        tr_firewall_route_policy_id: str = None,
        tr_firewall_route_table_id: str = None,
    ):
        # The destination address of the route.
        self.tr_firewall_route_destination = tr_firewall_route_destination
        # The ID of the next hop for the route.
        self.tr_firewall_route_nexthop = tr_firewall_route_nexthop
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id
        # The ID of the route table to which the route entry belongs.
        self.tr_firewall_route_table_id = tr_firewall_route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tr_firewall_route_destination is not None:
            result['TrFirewallRouteDestination'] = self.tr_firewall_route_destination

        if self.tr_firewall_route_nexthop is not None:
            result['TrFirewallRouteNexthop'] = self.tr_firewall_route_nexthop

        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id

        if self.tr_firewall_route_table_id is not None:
            result['TrFirewallRouteTableId'] = self.tr_firewall_route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrFirewallRouteDestination') is not None:
            self.tr_firewall_route_destination = m.get('TrFirewallRouteDestination')

        if m.get('TrFirewallRouteNexthop') is not None:
            self.tr_firewall_route_nexthop = m.get('TrFirewallRouteNexthop')

        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')

        if m.get('TrFirewallRouteTableId') is not None:
            self.tr_firewall_route_table_id = m.get('TrFirewallRouteTableId')

        return self

