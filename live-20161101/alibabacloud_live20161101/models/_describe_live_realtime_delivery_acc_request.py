# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveRealtimeDeliveryAccRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        log_store: str = None,
        owner_id: int = None,
        project: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The streaming domain.
        # - You can specify a single domain name or multiple domain names. Separate multiple domain names with commas (,).
        # - If this parameter is not specified, the merged data of all live streaming domain names is returned by default.
        self.domain_name = domain_name
        # The end time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # The end time must be later than the start time. The interval between the start time and end time cannot exceed one year.
        self.end_time = end_time
        # The time granularity of the queried data. Unit: seconds. Valid values:
        # 
        # - **300**
        # - **3600**
        # - **86400**
        # 
        # If this parameter is not specified or the specified value is not supported, the default value is 300 seconds when the time span does not exceed 3 days, 3600 seconds when the time span exceeds 3 days, and 86400 seconds when the time span exceeds 30 days.
        self.interval = interval
        # The Logstore for real-time log delivery. If this parameter is not specified, the merged data of all Logstores is returned by default.
        self.log_store = log_store
        self.owner_id = owner_id
        # The Project for real-time log delivery. If this parameter is not specified, the merged data of all Projects is returned by default.
        self.project = project
        # The region ID.
        self.region_id = region_id
        # The start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project is not None:
            result['Project'] = self.project

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

