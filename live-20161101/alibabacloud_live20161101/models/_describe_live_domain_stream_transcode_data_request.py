# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDomainStreamTranscodeDataRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        owner_id: int = None,
        precision: str = None,
        region_id: str = None,
        split: str = None,
        start_time: str = None,
    ):
        # The main streaming domain to query.
        # 
        # *   You can query one or more domain names. If you specify multiple domain names, separate them with commas (,).
        # *   If you leave this parameter empty, the data of all domain names within your Alibaba Cloud account is returned.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time granularity of the query. Unit: seconds. Valid values:
        # 
        # *   **3600**: 1 hour
        # *   **86400**: 1 day
        # 
        # >  If you do not specify this parameter, the time granularity of 1 hour is used by default.
        self.interval = interval
        self.owner_id = owner_id
        # The time precision of the query. Valid values:
        # 
        # *   **min** (default): in minutes.
        # *   **sec**: in seconds.
        self.precision = precision
        self.region_id = region_id
        # The key that is used to group data. Valid values:
        # 
        # *   **domain**: The DomainName parameter is available in the response only if Split is set to domain.
        # *   **region**: The Region parameter is available in the response only if Split is set to region.
        # *   **transcode_type**: The TanscodeType parameter is available in the response only if Split is set to transcode_type.
        # *   **resolution**: The Resolution parameter is available in the response only if Split is set to resolution.
        # *   **fps**: The Fps parameter is available in the response only if Split is set to fps.
        # 
        # You can specify one or more keys. If you specify multiple keys, separate them with commas (,).
        # 
        # Default value: `domain,region,transcode_type,resolution,fps`.
        self.split = split
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # *   The minimum query interval is 1 hour.
        # *   If you do not set this parameter, the transcoding length for the last 24 hours is returned.
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
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.precision is not None:
            result['Precision'] = self.precision

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.split is not None:
            result['Split'] = self.split

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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Precision') is not None:
            self.precision = m.get('Precision')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Split') is not None:
            self.split = m.get('Split')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

