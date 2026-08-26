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
        # The streaming domain to query.
        # 
        # - You can specify a single domain name or multiple domain names. Separate multiple domain names with commas (,).
        # - If this parameter is left empty, the merged data of all live streaming domain names is returned by default.
        self.domain_name = domain_name
        # The end time. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The monitoring session ID. If this parameter is left empty, the merged data of all monitoring sessions is returned by default. You can specify multiple IDs. Separate multiple IDs with commas (,).
        self.instance_id = instance_id
        # The time granularity for the query. Valid values: **3600** (hour) and **86400** (day).
        self.interval = interval
        self.owner_id = owner_id
        # The live center region. If this parameter is left empty, the merged data of all regions is returned by default. You can specify multiple regions. Separate multiple regions with commas (,).
        self.region = region
        # The region ID.
        self.region_id = region_id
        # The grouping key. Default value: **resolution**, which indicates grouping by resolution. Valid values: **domain**, **region**, **instance**, and **resolution**. You can specify multiple values. Separate multiple values with commas (,).
        self.split_by = split_by
        # The start time. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        # - The minimum data granularity is 1 hour.
        # - If this parameter is not specified, data of the last 24 hours is returned by default.
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

