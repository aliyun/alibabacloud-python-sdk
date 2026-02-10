# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySecurityCheckScheduleConfigRequest(DaraModel):
    def __init__(
        self,
        days_of_week: str = None,
        end_time: int = None,
        lang: str = None,
        resource_owner_id: int = None,
        source_ip: str = None,
        start_time: int = None,
    ):
        # The days on which the automatic configuration check runs. You can specify multiple days. Separate multiple days with commas (,). Valid values:
        # 
        # *   **1**: Monday
        # *   **2**: Tuesday
        # *   **3**: Wednesday
        # *   **4**: Thursday
        # *   **5**: Friday
        # *   **6**: Saturday
        # *   **7**: Sunday
        # 
        # This parameter is required.
        self.days_of_week = days_of_week
        # The time period during which the automatic configuration check ends. Valid values:
        # 
        # *   **0**: 00:00 to 06:00
        # *   **6**: 06:00 to 12:00
        # *   **12**: 12:00 to 18:00
        # *   **18**: 18:00 to 24:00
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        self.resource_owner_id = resource_owner_id
        # The source IP address of the request.
        self.source_ip = source_ip
        # The time period during which the automatic configuration check starts. Valid values:
        # 
        # *   **0**: 00:00 to 06:00
        # *   **6**: 06:00 to 12:00
        # *   **12**: 12:00 to 18:00
        # *   **18**: 18:00 to 24:00
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

