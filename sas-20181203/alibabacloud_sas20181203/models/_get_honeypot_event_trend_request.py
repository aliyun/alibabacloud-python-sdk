# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetHoneypotEventTrendRequest(DaraModel):
    def __init__(
        self,
        end_time_stamp: int = None,
        lang: str = None,
        risk_level_list: List[str] = None,
        src_ip: str = None,
        start_time_stamp: int = None,
    ):
        # End time, timestamp format.
        self.end_time_stamp = end_time_stamp
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The risk levels of the alert events.
        self.risk_level_list = risk_level_list
        # The source IP address of the attack.
        # 
        # This parameter is required.
        self.src_ip = src_ip
        # Start time, timestamp format.
        self.start_time_stamp = start_time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.start_time_stamp is not None:
            result['StartTimeStamp'] = self.start_time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')

        return self

