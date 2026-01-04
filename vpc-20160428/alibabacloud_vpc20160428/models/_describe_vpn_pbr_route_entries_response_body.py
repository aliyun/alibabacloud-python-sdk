# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpnPbrRouteEntriesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpn_pbr_route_entries: main_models.DescribeVpnPbrRouteEntriesResponseBodyVpnPbrRouteEntries = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count
        # The list of policy-based routes.
        self.vpn_pbr_route_entries = vpn_pbr_route_entries

    def validate(self):
        if self.vpn_pbr_route_entries:
            self.vpn_pbr_route_entries.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vpn_pbr_route_entries is not None:
            result['VpnPbrRouteEntries'] = self.vpn_pbr_route_entries.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VpnPbrRouteEntries') is not None:
            temp_model = main_models.DescribeVpnPbrRouteEntriesResponseBodyVpnPbrRouteEntries()
            self.vpn_pbr_route_entries = temp_model.from_map(m.get('VpnPbrRouteEntries'))

        return self

class DescribeVpnPbrRouteEntriesResponseBodyVpnPbrRouteEntries(DaraModel):
    def __init__(
        self,
        vpn_pbr_route_entry: List[main_models.DescribeVpnPbrRouteEntriesResponseBodyVpnPbrRouteEntriesVpnPbrRouteEntry] = None,
    ):
        self.vpn_pbr_route_entry = vpn_pbr_route_entry

    def validate(self):
        if self.vpn_pbr_route_entry:
            for v1 in self.vpn_pbr_route_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VpnPbrRouteEntry'] = []
        if self.vpn_pbr_route_entry is not None:
            for k1 in self.vpn_pbr_route_entry:
                result['VpnPbrRouteEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpn_pbr_route_entry = []
        if m.get('VpnPbrRouteEntry') is not None:
            for k1 in m.get('VpnPbrRouteEntry'):
                temp_model = main_models.DescribeVpnPbrRouteEntriesResponseBodyVpnPbrRouteEntriesVpnPbrRouteEntry()
                self.vpn_pbr_route_entry.append(temp_model.from_map(k1))

        return self

class DescribeVpnPbrRouteEntriesResponseBodyVpnPbrRouteEntriesVpnPbrRouteEntry(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        next_hop: str = None,
        next_hop_tunnel_id: str = None,
        priority: int = None,
        route_dest: str = None,
        route_source: str = None,
        state: str = None,
        vpn_instance_id: str = None,
        weight: int = None,
    ):
        # The time when the policy-based route was created. Unit: millisecond.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The next hop of the policy-based route.
        self.next_hop = next_hop
        # The ID of the tunnel associated with the next hop of the policy-based route.
        # 
        # This parameter is returned only if the VPN gateway supports IPsec-VPN connections in dual-tunnel mode.
        self.next_hop_tunnel_id = next_hop_tunnel_id
        # The priority of the policy-based route.
        # 
        # A smaller value indicates a higher priority.
        self.priority = priority
        # The destination CIDR block of the policy-based route.
        self.route_dest = route_dest
        # The source CIDR block of the policy-based route.
        self.route_source = route_source
        # The status of the policy-based route. Valid values:
        # 
        # *   **published**: advertised to the VPC route table.
        # *   **normal**: not advertised to the VPC route table.
        self.state = state
        # The ID of the VPN gateway.
        self.vpn_instance_id = vpn_instance_id
        # The weight of the policy-based route.
        # 
        # For a VPN gateway that supports IPsec-VPN connections in single-tunnel mode, the weight of a policy-based route indicates the priority of the route.
        # 
        # *   **100**: a high priority If multiple policy-based routes with the same source CIDR block and destination CIDR block exist, the IPsec-VPN connection associated with the policy-based route is the active connection.
        # *   **0**: a low priority If multiple policy-based routes with the same source CIDR block and destination CIDR block exist, the IPsec-VPN connection associated with the policy-based route is the standby connection.
        # 
        # >  For a VPN gateway that does not support IPsec-VPN connections in single-tunnel mode, this parameter does not take effect.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.next_hop_tunnel_id is not None:
            result['NextHopTunnelId'] = self.next_hop_tunnel_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.route_dest is not None:
            result['RouteDest'] = self.route_dest

        if self.route_source is not None:
            result['RouteSource'] = self.route_source

        if self.state is not None:
            result['State'] = self.state

        if self.vpn_instance_id is not None:
            result['VpnInstanceId'] = self.vpn_instance_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('NextHopTunnelId') is not None:
            self.next_hop_tunnel_id = m.get('NextHopTunnelId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RouteDest') is not None:
            self.route_dest = m.get('RouteDest')

        if m.get('RouteSource') is not None:
            self.route_source = m.get('RouteSource')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('VpnInstanceId') is not None:
            self.vpn_instance_id = m.get('VpnInstanceId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

