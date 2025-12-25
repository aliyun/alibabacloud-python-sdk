# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDeviceStatRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        device_type: str = None,
        end_time: str = None,
        query_type: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        self.device_type = device_type
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.query_type = query_type
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

