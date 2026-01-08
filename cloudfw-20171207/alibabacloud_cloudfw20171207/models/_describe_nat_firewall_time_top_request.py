# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNatFirewallTimeTopRequest(DaraModel):
    def __init__(
        self,
        interval: int = None,
        lang: str = None,
        limit: int = None,
        nat_gateway_id: str = None,
        sort: str = None,
        src_private_ip: str = None,
        src_public_ip: str = None,
        traffic_time: str = None,
    ):
        self.interval = interval
        self.lang = lang
        self.limit = limit
        self.nat_gateway_id = nat_gateway_id
        self.sort = sort
        self.src_private_ip = src_private_ip
        self.src_public_ip = src_public_ip
        # This parameter is required.
        self.traffic_time = traffic_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['Interval'] = self.interval

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.src_private_ip is not None:
            result['SrcPrivateIP'] = self.src_private_ip

        if self.src_public_ip is not None:
            result['SrcPublicIP'] = self.src_public_ip

        if self.traffic_time is not None:
            result['TrafficTime'] = self.traffic_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('SrcPrivateIP') is not None:
            self.src_private_ip = m.get('SrcPrivateIP')

        if m.get('SrcPublicIP') is not None:
            self.src_public_ip = m.get('SrcPublicIP')

        if m.get('TrafficTime') is not None:
            self.traffic_time = m.get('TrafficTime')

        return self

