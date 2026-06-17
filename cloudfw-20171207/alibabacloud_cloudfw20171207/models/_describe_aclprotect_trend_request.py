# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeACLProtectTrendRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        firewall_type: str = None,
        interval: int = None,
        lang: str = None,
        source_ip: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. The value is a timestamp in seconds.
        self.end_time = end_time
        # The type of the firewall. Valid values:
        # 
        # - **internet** (default): internet firewall
        # 
        # - **vpc**: VPC firewall
        # 
        # - **nat**: NAT firewall
        self.firewall_type = firewall_type
        # The time granularity for aggregating trend data, in seconds. Valid values:
        # 
        # - **60**: 1 minute
        # 
        # - **1800**: 30 minutes
        # 
        # - **3600**: 1 hour
        # 
        # - **86400** (default): 1 day
        self.interval = interval
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # This parameter is deprecated.
        self.source_ip = source_ip
        # The beginning of the time range to query. The value is a timestamp in seconds.
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

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

