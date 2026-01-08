# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallDropTrafficTrendRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        order: str = None,
        sort: str = None,
        source_ip: str = None,
        start_time: int = None,
        traffic_time: int = None,
    ):
        self.end_time = end_time
        self.order = order
        self.sort = sort
        self.source_ip = source_ip
        self.start_time = start_time
        self.traffic_time = traffic_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.order is not None:
            result['Order'] = self.order

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.traffic_time is not None:
            result['TrafficTime'] = self.traffic_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TrafficTime') is not None:
            self.traffic_time = m.get('TrafficTime')

        return self

