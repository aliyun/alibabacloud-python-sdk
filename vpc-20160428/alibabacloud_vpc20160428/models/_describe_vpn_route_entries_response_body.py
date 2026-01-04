# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpnRouteEntriesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpn_route_counts: main_models.DescribeVpnRouteEntriesResponseBodyVpnRouteCounts = None,
        vpn_route_entries: main_models.DescribeVpnRouteEntriesResponseBodyVpnRouteEntries = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about route entries of the VPN gateway in dual-tunnel mode.
        # 
        # > This parameter is returned only if the VPN gateway supports IPsec-VPN connections in dual-tunnel mode.
        self.vpn_route_counts = vpn_route_counts
        # The route entry list.
        self.vpn_route_entries = vpn_route_entries

    def validate(self):
        if self.vpn_route_counts:
            self.vpn_route_counts.validate()
        if self.vpn_route_entries:
            self.vpn_route_entries.validate()

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

        if self.vpn_route_counts is not None:
            result['VpnRouteCounts'] = self.vpn_route_counts.to_map()

        if self.vpn_route_entries is not None:
            result['VpnRouteEntries'] = self.vpn_route_entries.to_map()

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

        if m.get('VpnRouteCounts') is not None:
            temp_model = main_models.DescribeVpnRouteEntriesResponseBodyVpnRouteCounts()
            self.vpn_route_counts = temp_model.from_map(m.get('VpnRouteCounts'))

        if m.get('VpnRouteEntries') is not None:
            temp_model = main_models.DescribeVpnRouteEntriesResponseBodyVpnRouteEntries()
            self.vpn_route_entries = temp_model.from_map(m.get('VpnRouteEntries'))

        return self

class DescribeVpnRouteEntriesResponseBodyVpnRouteEntries(DaraModel):
    def __init__(
        self,
        vpn_route_entry: List[main_models.DescribeVpnRouteEntriesResponseBodyVpnRouteEntriesVpnRouteEntry] = None,
    ):
        self.vpn_route_entry = vpn_route_entry

    def validate(self):
        if self.vpn_route_entry:
            for v1 in self.vpn_route_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VpnRouteEntry'] = []
        if self.vpn_route_entry is not None:
            for k1 in self.vpn_route_entry:
                result['VpnRouteEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpn_route_entry = []
        if m.get('VpnRouteEntry') is not None:
            for k1 in m.get('VpnRouteEntry'):
                temp_model = main_models.DescribeVpnRouteEntriesResponseBodyVpnRouteEntriesVpnRouteEntry()
                self.vpn_route_entry.append(temp_model.from_map(k1))

        return self

class DescribeVpnRouteEntriesResponseBodyVpnRouteEntriesVpnRouteEntry(DaraModel):
    def __init__(
        self,
        as_path: str = None,
        community: str = None,
        create_time: int = None,
        next_hop: str = None,
        next_hop_tunnel_id: str = None,
        route_dest: str = None,
        route_entry_type: str = None,
        source: str = None,
        state: str = None,
        vpn_instance_id: str = None,
        weight: int = None,
    ):
        # The AS path of the route entry.
        self.as_path = as_path
        # The community attributes of the route entry.
        self.community = community
        # The timestamp when the route entry was created.
        self.create_time = create_time
        # The next hop of the route entry.
        self.next_hop = next_hop
        # The ID of the tunnel associated with the next hop. 
        # 
        # 
        # > This parameter is returned only if the VPN gateway supports the dual-tunnel mode.
        self.next_hop_tunnel_id = next_hop_tunnel_id
        # The destination CIDR block of the route entry.
        self.route_dest = route_dest
        # The type of the route entry. Valid values:
        # 
        # *   **Custom**: custom
        # *   **System**: system
        self.route_entry_type = route_entry_type
        # The source of the BGP route. Valid values:
        # 
        # *   **CLOUD**: advertised from a cloud service associated with the VPN gateway.
        # *   **VPN_BGP**: indicates that the current route is learned by using BGP of the VPN gateway. For example, the BGP is used to learn the route of the on-premises data center.
        self.source = source
        # The status of the route entry. Valid values:
        # 
        # *   **published**: advertised
        # *   **normal**: not advertised
        self.state = state
        # The ID of the VPN gateway.
        self.vpn_instance_id = vpn_instance_id
        # The weight of the route entry. Valid values: **0** and **100**.
        # 
        # *   **0**: a low priority
        # *   **100**: a high priority
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

        if self.next_hop_tunnel_id is not None:
            result['NextHopTunnelId'] = self.next_hop_tunnel_id

        if self.route_dest is not None:
            result['RouteDest'] = self.route_dest

        if self.route_entry_type is not None:
            result['RouteEntryType'] = self.route_entry_type

        if self.source is not None:
            result['Source'] = self.source

        if self.state is not None:
            result['State'] = self.state

        if self.vpn_instance_id is not None:
            result['VpnInstanceId'] = self.vpn_instance_id

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

        if m.get('NextHopTunnelId') is not None:
            self.next_hop_tunnel_id = m.get('NextHopTunnelId')

        if m.get('RouteDest') is not None:
            self.route_dest = m.get('RouteDest')

        if m.get('RouteEntryType') is not None:
            self.route_entry_type = m.get('RouteEntryType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('VpnInstanceId') is not None:
            self.vpn_instance_id = m.get('VpnInstanceId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class DescribeVpnRouteEntriesResponseBodyVpnRouteCounts(DaraModel):
    def __init__(
        self,
        vpn_route_count: List[main_models.DescribeVpnRouteEntriesResponseBodyVpnRouteCountsVpnRouteCount] = None,
    ):
        self.vpn_route_count = vpn_route_count

    def validate(self):
        if self.vpn_route_count:
            for v1 in self.vpn_route_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VpnRouteCount'] = []
        if self.vpn_route_count is not None:
            for k1 in self.vpn_route_count:
                result['VpnRouteCount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpn_route_count = []
        if m.get('VpnRouteCount') is not None:
            for k1 in m.get('VpnRouteCount'):
                temp_model = main_models.DescribeVpnRouteEntriesResponseBodyVpnRouteCountsVpnRouteCount()
                self.vpn_route_count.append(temp_model.from_map(k1))

        return self

class DescribeVpnRouteEntriesResponseBodyVpnRouteCountsVpnRouteCount(DaraModel):
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
        # *   **custom** (default): destination-based route.
        # *   **bgp** : BGP route entry.
        self.route_entry_type = route_entry_type
        # The source of the BGP route. Valid values:
        # 
        # *   **CLOUD**: advertised from a cloud service associated with the VPN gateway.
        # *   **VPN_BGP**: indicates that the current route is learned by using BGP of the VPN gateway. For example, the BGP is used to learn the route of the on-premises data center.
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

