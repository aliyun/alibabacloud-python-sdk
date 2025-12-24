# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDomainMonitoringUsageDataRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        instance_id: str = None,
        interval: str = None,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        split_by: str = None,
        start_time: str = None,
    ):
        # The main streaming domain to query.
        # 
        # *   You can query one or more domain names. If you specify multiple domain names, separate them with commas (,).
        # *   If you leave this parameter empty, the data of all domain names within your Alibaba Cloud account is returned.
        self.domain_name = domain_name
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The ID of the monitoring session. If you leave this parameter empty, data of all monitoring sessions is queried by default. Separate multiple session IDs with commas (,).
        self.instance_id = instance_id
        # The time granularity. Valid values: **3600** and **86400**. 3600 specifies that data is queried by hour and 86400 specifies that data is queried by day.
        self.interval = interval
        self.owner_id = owner_id
        # The region of the live center. If you leave this parameter empty, data of all regions is queried by default. Separate multiple regions with commas (,).
        self.region = region
        self.region_id = region_id
        # The key that is used to group data. Valid values: **domain**, **region**, **instance**, and **resolution**. Default value: **resolution**. resolution specifies that data is grouped by resolution. Separate multiple values with commas (,).
        self.split_by = split_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
        # 
        # *   The time must be in UTC.
        # *   The minimum data granularity is 1 hour.
        # *   If you leave this parameter empty, data in the previous 24 hours is queried.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.split_by is not None:
            result['SplitBy'] = self.split_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

