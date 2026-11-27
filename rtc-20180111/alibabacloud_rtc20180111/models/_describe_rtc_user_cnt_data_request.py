# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRtcUserCntDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        interval: str = None,
        owner_id: int = None,
        service_area: str = None,
        start_time: str = None,
    ):
        # The application ID. You can specify only one ID.
        # 
        # By default, all application IDs are queried.
        self.app_id = app_id
        # The end time of the queried data. The time is displayed in UTC. The format is yyyy-MM-ddTHH:mm:ssZ.
        # 
        # The end time must be later than the start time.
        self.end_time = end_time
        # The time granularity at which the data is queried. Unit: seconds.
        # 
        # Valid values: **3600** (one hour) or **86400** (one day). Default value: **3600**.
        self.interval = interval
        self.owner_id = owner_id
        # The service area. CN: China (default value).
        self.service_area = service_area
        # The start time of the queried data. The time is displayed in UTC. The format is yyyy-MM-ddTHH:mm:ssZ.
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.service_area is not None:
            result['ServiceArea'] = self.service_area

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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

