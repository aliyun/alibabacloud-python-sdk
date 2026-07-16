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
        # AppKey information.
        # 
        # This parameter is required.
        self.app_key = app_key
        # >Notice: 
        # 
        # This parameter is only valid for early Android and iOS dual-platform application types. If your application is a dual-platform application, specify this parameter as iOS or ANDROID to query the number of devices for each type. By default, it queries ALL types.
        # 
        # 
        # 
        # The device type. Valid values:
        # 
        # - **iOS**: iOS devices
        # 
        # - **ANDROID**: Android devices
        # 
        # - **ALL**: All device types
        self.device_type = device_type
        # The end time of the query. The time format follows the ISO8601 standard and uses UTC time, in the format YYYY-MM-DDThh:mm:ssZ.
        # 
        # > The statistics end date is the end time\\"s day.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Query new devices or historical cumulative devices. Valid values:
        # 
        # - **NEW**: New devices
        # 
        # - **TOTAL**: Cumulative devices
        # 
        # This parameter is required.
        self.query_type = query_type
        # The start time of the query. The time format follows the ISO8601 standard and uses UTC time, in the format YYYY-MM-DDThh:mm:ssZ.
        # 
        # > The statistics start date is 00:00 UTC+8 on the start time\\"s day.
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

