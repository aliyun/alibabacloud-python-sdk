# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMeterLiveBypassDurationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        interval: str = None,
        start_time: str = None,
    ):
        # The ID of the application. You can view the application ID on the [Applications](https://help.aliyun.com/document_detail/2355593.html) page in the ApsaraVideo Real-time Communication (ARTC) section of the ApsaraVideo Live console.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The end time must be later than the start time. The time range that can be specified is greater than or equal to 5 minutes and less than or equal to 31 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time granularity of the query. Unit: seconds. Valid values:
        # 
        # *   300
        # *   3600
        # *   86400
        # 
        # If you specify an invalid value or do not specify this parameter, the default value 3600 is used.
        self.interval = interval
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

