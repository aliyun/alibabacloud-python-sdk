# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSaasDataUnitUsageRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        region_id: str = None,
        service_id: str = None,
        start_time: str = None,
        time_unit: str = None,
    ):
        # The end time of the query in UTC. The format is yyyy-MM-ddTHH:mm:ssZ, and the seconds must be 00. The end time must be later than the start time and no later than the request time. The query range is not automatically truncated.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The region ID.
        self.region_id = region_id
        # The instance ID of the undeleted SaaS service. A standard DBInstanceId cannot override it.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The start time of the query in UTC. The format is yyyy-MM-ddTHH:mm:ssZ, and the seconds must be 00. The start time cannot be earlier than 30 days before the request time. The start time and the end time form a left-closed and right-open interval, and the span cannot exceed 7 days.
        # 
        # This parameter is required.
        self.start_time = start_time
        # Specifies the time granularity. Valid values: hour (UTC hour) and day (UTC day). Default value: hour. This parameter only determines the trend aggregation method and is not returned in the response.
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        return self

