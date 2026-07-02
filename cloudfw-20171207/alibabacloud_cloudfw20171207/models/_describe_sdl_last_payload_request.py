# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSdlLastPayloadRequest(DaraModel):
    def __init__(
        self,
        dst_ip: str = None,
        end_time: int = None,
        lang: str = None,
        sensitive_category: str = None,
        src_ip: str = None,
        start_time: int = None,
    ):
        # The destination IP address.
        self.dst_ip = dst_ip
        # The end of the time range to query. Specify the value as a UNIX timestamp in seconds.
        self.end_time = end_time
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The type of sensitive credential.
        self.sensitive_category = sensitive_category
        # The source IP address.
        self.src_ip = src_ip
        # The beginning of the time range to query. Specify the value as a UNIX timestamp in seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.sensitive_category is not None:
            result['SensitiveCategory'] = self.sensitive_category

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SensitiveCategory') is not None:
            self.sensitive_category = m.get('SensitiveCategory')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

