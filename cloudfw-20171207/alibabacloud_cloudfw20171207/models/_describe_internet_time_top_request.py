# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInternetTimeTopRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        end_time: str = None,
        iptype: str = None,
        interval: int = None,
        lang: str = None,
        limit: str = None,
        nat_ip: str = None,
        order: str = None,
        sort: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        start_time: str = None,
        traffic_time: str = None,
        traffic_type: str = None,
    ):
        # This parameter is required.
        self.direction = direction
        self.end_time = end_time
        self.iptype = iptype
        self.interval = interval
        self.lang = lang
        self.limit = limit
        self.nat_ip = nat_ip
        self.order = order
        self.sort = sort
        # This parameter is required.
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.start_time = start_time
        self.traffic_time = traffic_time
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.nat_ip is not None:
            result['NatIP'] = self.nat_ip

        if self.order is not None:
            result['Order'] = self.order

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.source_code is not None:
            result['SourceCode'] = self.source_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.traffic_time is not None:
            result['TrafficTime'] = self.traffic_time

        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NatIP') is not None:
            self.nat_ip = m.get('NatIP')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TrafficTime') is not None:
            self.traffic_time = m.get('TrafficTime')

        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')

        return self

