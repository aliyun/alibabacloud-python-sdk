# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationComponentPerformanceRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        component_id: str = None,
        end_time: str = None,
        interval: str = None,
        key: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The ID of the application component. You can obtain the ID from the Components parameter returned by the DescribeApplicationAttribute operation.
        # 
        # This parameter is required.
        self.component_id = component_id
        # The end time of the query. The end time must be later than or equal to the start time. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The sampling granularity of the performance data. Unit: seconds.
        self.interval = interval
        # The performance metrics to query. Separate multiple metrics with commas. You can specify up to 5 metrics.
        # 
        # This parameter is required.
        self.key = key
        # The start time of the query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of the performance data.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.key is not None:
            result['Key'] = self.key

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

