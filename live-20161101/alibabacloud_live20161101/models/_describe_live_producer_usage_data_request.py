# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveProducerUsageDataRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        instance: str = None,
        interval: str = None,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        split_by: str = None,
        start_time: str = None,
        type: str = None,
        app: str = None,
    ):
        # The streaming domain name of the cloud producer studio.
        # 
        # - Supports single or batch domain name queries. Separate multiple domain names with commas (,) for batch queries.
        # - If this parameter is left empty, merged data of all live streaming domain names is returned by default.
        self.domain_name = domain_name
        # The end time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The instance to query. Batch query is supported. Separate multiple instances with commas (,).
        # 
        # > If this parameter is left empty, merged data of all instances is returned by default.
        self.instance = instance
        # The time granularity of the queried data. Valid values: 3600 (1 hour) and 86400 (1 day). Unit: seconds.
        self.interval = interval
        self.owner_id = owner_id
        # The region to which the domain name belongs. If this parameter is left empty, merged data of all regions is returned by default. Batch query is supported. Separate multiple regions with commas (,).
        self.region = region
        # The region ID.
        self.region_id = region_id
        # The grouping key. You can specify one or more of the following: domain, region, instance, or type. Separate multiple values with commas (,). The specified fields will be grouped in the output.
        # 
        # 
        # > If this parameter is left empty, only aggregated data is returned.
        self.split_by = split_by
        # The start time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The producer type. Batch query is supported. Separate multiple types with commas (,). Valid values:
        # 
        # - **slidelive**: playlist-based.
        # 
        # - **universal**: general-purpose.
        # 
        # > If this parameter is left empty, merged data of all producer types is returned by default.
        self.type = type
        # The name of the application to which the stream belongs.
        self.app = app

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

        if self.instance is not None:
            result['Instance'] = self.instance

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

        if self.type is not None:
            result['Type'] = self.type

        if self.app is not None:
            result['app'] = self.app

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Instance') is not None:
            self.instance = m.get('Instance')

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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('app') is not None:
            self.app = m.get('app')

        return self

