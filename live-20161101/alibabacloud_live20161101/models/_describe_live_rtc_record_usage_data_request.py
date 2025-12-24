# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveRtcRecordUsageDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        interval: str = None,
        record_mode: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.end_time = end_time
        self.interval = interval
        # This parameter is required.
        self.record_mode = record_mode
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.record_mode is not None:
            result['RecordMode'] = self.record_mode

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RecordMode') is not None:
            self.record_mode = m.get('RecordMode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

