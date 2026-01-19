# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventResultBarChartRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        begin_time: int = None,
        end_time: int = None,
        event_codes: str = None,
        reg_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Start time, accurate to milliseconds (ms).
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # End time, accurate to milliseconds (ms).
        # 
        # This parameter is required.
        self.end_time = end_time
        # Event code.
        self.event_codes = event_codes
        # Region code
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

