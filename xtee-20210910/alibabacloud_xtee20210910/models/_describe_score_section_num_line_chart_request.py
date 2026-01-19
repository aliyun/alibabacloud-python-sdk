# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScoreSectionNumLineChartRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        begin_time: str = None,
        by_pass_event_codes: str = None,
        end_time: str = None,
        main_event_codes: str = None,
        reg_id: str = None,
        shunt_event_codes: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Start timestamp, in milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # Bypass event code
        self.by_pass_event_codes = by_pass_event_codes
        # End timestamp, in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Main event code
        self.main_event_codes = main_event_codes
        # Region code
        self.reg_id = reg_id
        # Diversion event code
        self.shunt_event_codes = shunt_event_codes

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

        if self.by_pass_event_codes is not None:
            result['byPassEventCodes'] = self.by_pass_event_codes

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.main_event_codes is not None:
            result['mainEventCodes'] = self.main_event_codes

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.shunt_event_codes is not None:
            result['shuntEventCodes'] = self.shunt_event_codes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('byPassEventCodes') is not None:
            self.by_pass_event_codes = m.get('byPassEventCodes')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('mainEventCodes') is not None:
            self.main_event_codes = m.get('mainEventCodes')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('shuntEventCodes') is not None:
            self.shunt_event_codes = m.get('shuntEventCodes')

        return self

