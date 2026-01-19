# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRiskTagsLineChartRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        event_codes: str = None,
        lang: str = None,
        reg_id: str = None,
    ):
        # Start time of the query, in milliseconds (ms).
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # End time, accurate to milliseconds (ms).
        # 
        # This parameter is required.
        self.end_time = end_time
        # Event code
        self.event_codes = event_codes
        # Sets the language type for the request and response messages. Default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Region code
        self.reg_id = reg_id

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

        if self.event_codes is not None:
            result['EventCodes'] = self.event_codes

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventCodes') is not None:
            self.event_codes = m.get('EventCodes')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        return self

