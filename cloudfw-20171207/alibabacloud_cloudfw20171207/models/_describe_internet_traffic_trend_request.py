# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInternetTrafficTrendRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        end_time: str = None,
        lang: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_private_ip: str = None,
        src_public_ip: str = None,
        start_time: str = None,
        traffic_type: str = None,
    ):
        # The direction of the internet traffic.
        # 
        # Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        self.direction = direction
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the content in the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The source code.
        # 
        # This parameter is required.
        self.source_code = source_code
        # The IP address of the access source.
        self.source_ip = source_ip
        # The private IP address of the source.
        self.src_private_ip = src_private_ip
        # The public IP address of the source.
        self.src_public_ip = src_public_ip
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of the traffic that is captured. Valid values:
        # 
        # *   **max** (default): peak traffic
        # *   **avg**: average traffic
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

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_code is not None:
            result['SourceCode'] = self.source_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.src_private_ip is not None:
            result['SrcPrivateIP'] = self.src_private_ip

        if self.src_public_ip is not None:
            result['SrcPublicIP'] = self.src_public_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SrcPrivateIP') is not None:
            self.src_private_ip = m.get('SrcPrivateIP')

        if m.get('SrcPublicIP') is not None:
            self.src_public_ip = m.get('SrcPublicIP')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')

        return self

