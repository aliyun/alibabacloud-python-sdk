# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodPlayerCollectDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        interval: str = None,
        metrics: str = None,
        os: str = None,
        period: str = None,
        start_time: str = None,
        terminal_type: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.interval = interval
        # This parameter is required.
        self.metrics = metrics
        self.os = os
        self.period = period
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.terminal_type = terminal_type

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

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.os is not None:
            result['Os'] = self.os

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.terminal_type is not None:
            result['TerminalType'] = self.terminal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TerminalType') is not None:
            self.terminal_type = m.get('TerminalType')

        return self

