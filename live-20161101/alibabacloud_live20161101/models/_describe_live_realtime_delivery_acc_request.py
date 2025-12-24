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
        # 
        # *   You can query one or more domain names. If you specify multiple domain names, separate them with commas (,).
        # *   If you leave this parameter empty, the data of all domain names within your Alibaba Cloud account is returned.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # The end time must be later than the start time. The maximum time range that can be specified is one year.
        self.end_time = end_time
        # The time granularity of the query. Unit: seconds. Valid values:
        # 
        # *   **300**
        # *   **3600**
        # *   **86400**
        # 
        # If you specify an invalid value or do not specify this parameter, the default value is used. If the specified time range is no more than three days, the default value is 300. If the specified time range is more than three days and no more than 30 days, the default value is 3600. If the specified time range is more than 30 days, the default value is 86400.
        self.interval = interval
        # The name of the Logstore to which log entries are delivered. If you leave this parameter empty, the data of all Logstores is returned.
        self.log_store = log_store
        self.owner_id = owner_id
        # The name of the Log Service project that is used for real-time log delivery. If you leave this parameter empty, the data of all Log Service projects is returned.
        self.project = project
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
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

