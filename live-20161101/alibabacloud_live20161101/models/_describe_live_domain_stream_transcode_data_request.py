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
        # The streaming domain of the streamer to query.
        # 
        # - You can query a single domain name or multiple domain names at a time. Separate multiple domain names with commas (,).
        # - If this parameter is left empty, the merged data of all live streaming domain names is returned by default.
        # - When you specify DomainName, make sure that the specified domain name is a live streaming domain name and that the user calling this operation has the permissions to operate on the specified domain name.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time granularity of the query. Unit: seconds. Valid values:
        # 
        # - **3600**: by hour.
        # - **86400**: by day.
        # 
        # > If this parameter is left empty, the default granularity is by hour.
        self.interval = interval
        self.owner_id = owner_id
        # The time precision of the query. Valid values:
        # - **min** (default): in minutes.
        # - **sec**: in seconds.
        self.precision = precision
        # The region ID.
        self.region_id = region_id
        # The grouping key. Valid values:
        # 
        # - **domain**: domain name. If the Split (grouping key) parameter is set to domain, the Domain response parameter takes effect.
        # - **region**: live center region. If the Split (grouping key) parameter is set to region, the Region response parameter takes effect.
        # - **transcode_type**: transcoding type. If the Split (grouping key) parameter is set to transcode_type, the TanscodeType response parameter takes effect.
        # - **resolution**: resolution. If the Split (grouping key) parameter is set to resolution, the Resolution response parameter takes effect.
        # - **fps**: frame rate. If the Split (grouping key) parameter is set to fps, the Fps response parameter takes effect.
        # 
        # You can specify one or more values. Separate multiple values with commas (,).
        # 
        # Default value: `domain,region,transcode_type,resolution,fps`, which means all grouping keys are applied.
        self.split = split
        # The beginning of the time range to query. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format in UTC.
        # 
        # - The minimum data time granularity is 1 hour.
        # - If this parameter is left empty, data from the last 24 hours is read by default.
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

