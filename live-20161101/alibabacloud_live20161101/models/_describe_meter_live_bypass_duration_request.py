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
        # The application ID. You can view the application ID on the [Application Management](https://help.aliyun.com/document_detail/2355593.html) page of ApsaraVideo Real-time Communication.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The end time of the query. The end time must be later than the start time. The query granularity must be ≥ 5 minutes and ≤ 31 days. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time granularity for querying data. Unit: seconds. Valid values:
        # 
        # - 300
        # - 3600
        # - 86400
        # 
        # If this parameter is not specified or set to an unsupported value, the default value 3600 is used.
        self.interval = interval
        # The start time of the query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
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

