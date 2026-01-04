# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVcoRouteEntriesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vco_route_entries: List[main_models.DescribeVcoRouteEntriesResponseBodyVcoRouteEntries] = None,
        vpn_route_counts: List[main_models.DescribeVcoRouteEntriesResponseBodyVpnRouteCounts] = None,
    ):
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count
        # The list of route entries.
        self.vco_route_entries = vco_route_entries
        # The information on route entries of the dual-tunnel IPsec connection.
        # 
        # >  This parameter is returned only for IPsec connections in dual-tunnel mode.
        self.vpn_route_counts = vpn_route_counts

    def validate(self):
        if self.vco_route_entries:
            for v1 in self.vco_route_entries:
                 if v1:
                    v1.validate()
        if self.vpn_route_counts:
            for v1 in self.vpn_route_counts:
                 if v1:
                    v1.validate()

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

        result['VcoRouteEntries'] = []
        if self.vco_route_entries is not None:
            for k1 in self.vco_route_entries:
                result['VcoRouteEntries'].append(k1.to_map() if k1 else None)

        result['VpnRouteCounts'] = []
        if self.vpn_route_counts is not None:
            for k1 in self.vpn_route_counts:
                result['VpnRouteCounts'].append(k1.to_map() if k1 else None)

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

        self.vco_route_entries = []
        if m.get('VcoRouteEntries') is not None:
            for k1 in m.get('VcoRouteEntries'):
                temp_model = main_models.DescribeVcoRouteEntriesResponseBodyVcoRouteEntries()
                self.vco_route_entries.append(temp_model.from_map(k1))

        self.vpn_route_counts = []
        if m.get('VpnRouteCounts') is not None:
            for k1 in m.get('VpnRouteCounts'):
                temp_model = main_models.DescribeVcoRouteEntriesResponseBodyVpnRouteCounts()
                self.vpn_route_counts.append(temp_model.from_map(k1))

        return self

class DescribeVcoRouteEntriesResponseBodyVpnRouteCounts(DaraModel):
    def __init__(
        self,
        route_count: int = None,
        route_entry_type: str = None,
        source: str = None,
    ):
        # The number of route entries.
        self.route_count = route_count
        # The route type. Valid values:
        # 
        # *   **custom**: destination-based route.
        # *   **bgp**: BGP route.
        self.route_entry_type = route_entry_type
        # The source of the BGP route. Valid values:
        # 
        # *   **CLOUD**: The current BGP route is learned by the IPsec connection from the transit router.
        # *   **VPN_BGP**: The current BGP route is learned by the IPsec connection from the data center.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_count is not None:
            result['RouteCount'] = self.route_count

        if self.route_entry_type is not None:
            result['RouteEntryType'] = self.route_entry_type

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteCount') is not None:
            self.route_count = m.get('RouteCount')

        if m.get('RouteEntryType') is not None:
            self.route_entry_type = m.get('RouteEntryType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

class DescribeVcoRouteEntriesResponseBodyVcoRouteEntries(DaraModel):
    def __init__(
        self,
        as_path: str = None,
        community: str = None,
        create_time: int = None,
        next_hop: str = None,
        next_hop_tunnel_id_list: List[str] = None,
        route_dest: str = None,
        route_entry_type: str = None,
        source: str = None,
        state: str = None,
        vpn_connection_id: str = None,
        weight: int = None,
    ):
        # The list of autonomous system (AS) numbers that the BGP route goes through.
        self.as_path = as_path
        # The community value carried by the BGP route.
        self.community = community
        # The timestamp when the route was created.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The next hop of the route.
        self.next_hop = next_hop
        # The list of next hops.
        # 
        # > - This parameter is returned only by dual-tunnel IPsec connections.
        # > - This parameter is returned only when the tunnel status is **Phase 2 Negotiation Successful**.
        self.next_hop_tunnel_id_list = next_hop_tunnel_id_list
        # The destination CIDR block of the route.
        self.route_dest = route_dest
        # The route type. Valid values:
        # 
        # *   **custom**: a destination-based route
        # *   **bgp**: a BGP route
        self.route_entry_type = route_entry_type
        # The source of the BGP route. Valid values:
        # 
        # *   **CLOUD**: indicates that the current BGP route is learned by the IPsec-VPN connection from the transit router.
        # *   **VPN_BGP**: indicates that the current BGP route is learned by the IPsec-VPN connection from the data center.
        self.source = source
        # The status of the route.
        # 
        # *   **published**: indicates that the current route is advertised to the transit router.
        # *   **Active**: indicates that the current BGP route is available.
        self.state = state
        # The ID of the IPsec-VPN connection.
        self.vpn_connection_id = vpn_connection_id
        # The weight of the destination-based route.
        # 
        # >  The current parameter has no effect.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.as_path is not None:
            result['AsPath'] = self.as_path

        if self.community is not None:
            result['Community'] = self.community

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.next_hop_tunnel_id_list is not None:
            result['NextHopTunnelIdList'] = self.next_hop_tunnel_id_list

        if self.route_dest is not None:
            result['RouteDest'] = self.route_dest

        if self.route_entry_type is not None:
            result['RouteEntryType'] = self.route_entry_type

        if self.source is not None:
            result['Source'] = self.source

        if self.state is not None:
            result['State'] = self.state

        if self.vpn_connection_id is not None:
            result['VpnConnectionId'] = self.vpn_connection_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')

        if m.get('Community') is not None:
            self.community = m.get('Community')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('NextHopTunnelIdList') is not None:
            self.next_hop_tunnel_id_list = m.get('NextHopTunnelIdList')

        if m.get('RouteDest') is not None:
            self.route_dest = m.get('RouteDest')

        if m.get('RouteEntryType') is not None:
            self.route_entry_type = m.get('RouteEntryType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('VpnConnectionId') is not None:
            self.vpn_connection_id = m.get('VpnConnectionId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

