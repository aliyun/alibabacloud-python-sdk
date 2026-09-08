# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceTrendingReportRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        media_type: str = None,
        start_time: int = None,
    ):
        # End UNIX timestamp. The default value is the current time. The format is a Unix timestamp in milliseconds.
        self.end_time = end_time
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Media type. The default value is Audio. Other valid values include Chat and Video.
        self.media_type = media_type
        # Start UNIX timestamp. The default value is the start time of the current day. The earliest allowed time is 180 days before the current time. The interval between the start time and end time cannot exceed 7 days. The format is a Unix timestamp in milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

