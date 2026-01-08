# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNatFirewallTrafficTrendRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        interval: int = None,
        nat_gateway_id: str = None,
        src_private_ip: str = None,
        src_public_ip: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp that is accurate to seconds.
        self.end_time = end_time
        # The time interval between the data entries to return. Unit: seconds. Valid values:
        # 
        # *   **60**: 1 minute
        # *   **1800**: 30 minutes
        self.interval = interval
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The private IP address of the source.
        self.src_private_ip = src_private_ip
        # The public IP address of the source.
        self.src_public_ip = src_public_ip
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.src_private_ip is not None:
            result['SrcPrivateIP'] = self.src_private_ip

        if self.src_public_ip is not None:
            result['SrcPublicIP'] = self.src_public_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('SrcPrivateIP') is not None:
            self.src_private_ip = m.get('SrcPrivateIP')

        if m.get('SrcPublicIP') is not None:
            self.src_public_ip = m.get('SrcPublicIP')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

