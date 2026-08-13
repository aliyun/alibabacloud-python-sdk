# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFirewallTrafficTrendRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        lang: str = None,
        start_time: int = None,
    ):
        # The end time of the query. Specify a UNIX timestamp in seconds. This parameter is required. If this parameter is not specified, ErrorTimeError (400) is returned.
        # 
        # > The query interval (EndTime − StartTime) cannot exceed 90 days. If the interval exceeds 90 days, ErrorTimeError is returned. If the value is later than the current time, it is silently adjusted to the current time.
        self.end_time = end_time
        # The language of the response message.
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The start time of the query. Specify a UNIX timestamp in seconds. This parameter is required. If this parameter is not specified, ErrorTimeError (400) is returned.
        # 
        # > The query interval (EndTime − StartTime) cannot exceed 90 days. If the interval exceeds 90 days, ErrorTimeError is returned. If the value is later than the current time, it is silently adjusted to the current time. If StartTime is later than EndTime, no error is returned, but the response contains empty data.
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

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

