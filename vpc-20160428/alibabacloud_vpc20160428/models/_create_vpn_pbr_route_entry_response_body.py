# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpnPbrRouteEntryResponseBody(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        next_hop: str = None,
        overlay_mode: str = None,
        priority: int = None,
        request_id: str = None,
        route_dest: str = None,
        route_source: str = None,
        state: str = None,
        vpn_instance_id: str = None,
        weight: int = None,
    ):
        # The time when the policy-based route was created.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The description of the policy-based route.
        self.description = description
        # The next hop of the policy-based route.
        self.next_hop = next_hop
        # The tunneling protocol. The value is **Ipsec**.
        self.overlay_mode = overlay_mode
        # The priority of the policy-based route.
        self.priority = priority
        # The request ID.
        self.request_id = request_id
        # The destination CIDR block of the policy-based route.
        self.route_dest = route_dest
        # The source CIDR block of the policy-based route.
        self.route_source = route_source
        # The status of the policy-based route. Valid values:
        # 
        # *   **published**: advertised to the VPC route table.
        # *   **normal**: not advertised to the VPC route table.
        self.state = state
        # The VPN gateway ID.
        self.vpn_instance_id = vpn_instance_id
        # The weight of the policy-based route. Valid values:
        # 
        # *   **100**: The IPsec-VPN connection associated with the policy-based route serves as an active connection.
        # *   **0**: The IPsec-VPN connection associated with the policy-based route serves as a standby connection.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.overlay_mode is not None:
            result['OverlayMode'] = self.overlay_mode

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('OverlayMode') is not None:
            self.overlay_mode = m.get('OverlayMode')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

