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
        # The streaming domain of the production studio.
        # 
        # *   You can query one or more domain names. If you specify multiple domain names, separate them with commas (,).
        # *   If you leave this parameter empty, the data of all domain names within your Alibaba Cloud account is returned.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time.
        self.end_time = end_time
        # The production studio instance that you want to query. You can specify one or more production studio instances. Separate multiple instances with commas (,).
        # 
        # >  If you do not set this parameter, the usage data of all production studio instances is returned.
        self.instance = instance
        # The time granularity for a query. Valid values: 3600 and 86400. Unit: seconds.
        self.interval = interval
        self.owner_id = owner_id
        # The region in which the domain name resides. If you leave this parameter empty, the data of all regions is returned. You can specify multiple regions by separating them with commas (,).
        self.region = region
        self.region_id = region_id
        # The key that is used to group data. You can specify one or more keys. Separate multiple keys with commas (,). Valid values: domain, region, instance, and type. The data for a key that you specify by using the SplitBy parameter is returned by group.
        # 
        # >  If you do not set this parameter, the aggregated data is returned.
        self.split_by = split_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The type of the production studio. You can specify one or more production studio types. Separate multiple types with commas (,). Valid values:
        # 
        # *   **slidelive**: playlist-mode studio.
        # *   **universal**: general studio.
        # 
        # >  If you do not set this parameter, the usage data of all types of production studios is returned.
        self.type = type
        # The name of the application to which the live stream belongs.
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

