# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHistoricalInstanceReportRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        media_type: str = None,
        start_time: int = None,
    ):
        # The end time of the Historical Data to retrieve, in UNIX timestamp format with millisecond precision. This parameter is optional. The default value is the current time. The time precision for statistics is hourly, snapped to the next full hour, and the interval is open. For example, if the start time is 11:12:20 and the end time is 11:45:50, the snapped input parameter Time Range becomes [11:00:00, 12:00:00), meaning greater than or equal to 11:00:00 and less than 12:00:00.
        self.end_time = end_time
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Media Type. The default value is Audio. Other valid values include Chat and Video.
        self.media_type = media_type
        # The start time of the Historical Data to retrieve, in UNIX timestamp format with millisecond precision. This parameter is optional. The default value is 00:00:00 of the current day. The earliest allowed time is 180 days before the current time. The time precision for statistics is hourly, snapped to the previous full hour, and the interval is closed.
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

