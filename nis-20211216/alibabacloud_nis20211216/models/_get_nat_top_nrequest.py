# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNatTopNRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        ip: str = None,
        nat_gateway_id: str = None,
        order_by: str = None,
        region_id: str = None,
        top_n: int = None,
    ):
        # The beginning of the time range to query in milliseconds. If you do not specify **EndTime**, the point in time specified by **BeginTime** is queried.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The end of the time range to query in milliseconds. The time range specified by **BeginTime** and **EndTime** cannot exceed **86400000** milliseconds (24 hours).
        self.end_time = end_time
        # Query ranking statistics for a specific IP address. If you specify this parameter, you do not need to specify **TopN** or **OrderBy**.
        self.ip = ip
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The metric that is used for real-time SNAT performance ranking. Valid values:
        # 
        # *   **InBps**: inbound data transfer. Unit: bit/s.
        # *   **OutBps**: outbound data transfer. Unit: bit/s.
        # *   **InPps**: inbound packet forwarding rate. Unit: packets per second.
        # *   **OutPps**: outbound packet forwarding rate. Unit: packets per second.
        # *   **NewSessionPerSecond**: new connection creation rate. Unit: connections per second.
        # *   **ActiveSessionCount**: number of concurrent connections. Unit: connections.
        self.order_by = order_by
        # The ID of the region in which the NAT gateway is deployed.
        self.region_id = region_id
        # The number of entries to return for real-time SNAT performance ranking. Valid values: **1 to 100**. Default value: **10**.
        self.top_n = top_n

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.top_n is not None:
            result['TopN'] = self.top_n

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        return self

