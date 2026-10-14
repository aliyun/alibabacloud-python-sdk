# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWebReportTopIpRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        interval: int = None,
        query_type: str = None,
        start_time: int = None,
        top: int = None,
    ):
        self.domain = domain
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.interval = interval
        # This parameter is required.
        self.query_type = query_type
        # This parameter is required.
        self.start_time = start_time
        self.top = top

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.top is not None:
            result['Top'] = self.top

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        return self

