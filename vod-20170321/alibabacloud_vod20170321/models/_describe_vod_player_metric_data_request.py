# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodPlayerMetricDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        filters: str = None,
        interval: str = None,
        language: str = None,
        metrics: str = None,
        os: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        terminal_type: str = None,
        top: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.end_time = end_time
        self.filters = filters
        # This parameter is required.
        self.interval = interval
        self.language = language
        # This parameter is required.
        self.metrics = metrics
        self.os = os
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.terminal_type = terminal_type
        self.top = top

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

        if self.filters is not None:
            result['Filters'] = self.filters

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.language is not None:
            result['Language'] = self.language

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.os is not None:
            result['Os'] = self.os

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.terminal_type is not None:
            result['TerminalType'] = self.terminal_type

        if self.top is not None:
            result['Top'] = self.top

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TerminalType') is not None:
            self.terminal_type = m.get('TerminalType')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        return self

