# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpnRouteEntryResponseBody(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        next_hop: str = None,
        overlay_mode: str = None,
        request_id: str = None,
        route_dest: str = None,
        state: str = None,
        vpn_instance_id: str = None,
        weight: int = None,
    ):
        # The timestamp when the destination-based route was created. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The description of the destination-based route.
        self.description = description
        # The next hop of the destination-based route.
        self.next_hop = next_hop
        # The tunneling protocol. The value is set to **Ipsec**, which indicates the IPsec tunneling protocol.
        self.overlay_mode = overlay_mode
        # The request ID.
        self.request_id = request_id
        # The destination CIDR block of the destination-based route.
        self.route_dest = route_dest
        # The status of the destination-based route.
        # 
        # *   **published**: advertised to the VPC route table.
        # *   **normal**: not advertised to the VPC route table.
        self.state = state
        # The ID of the VPN gateway.
        self.vpn_instance_id = vpn_instance_id
        # The weight of the destination-based route. Valid values:
        # 
        # *   **100**: a high priority
        # *   **0**: a low priority
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.route_dest is not None:
            result['RouteDest'] = self.route_dest

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouteDest') is not None:
            self.route_dest = m.get('RouteDest')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('VpnInstanceId') is not None:
            self.vpn_instance_id = m.get('VpnInstanceId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

