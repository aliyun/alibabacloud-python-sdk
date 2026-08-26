# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDelayedStreamingUsageRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        split_by: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # The streaming domain name to query.
        # - You can specify a single domain name or multiple domain names. Separate multiple domain names with commas (,).
        # - If this parameter is left empty, the aggregated data of all live streaming domain names is returned by default.
        self.domain_name = domain_name
        # The end of the time range to query. The end time must be later than the start time. The time span cannot exceed 10 hours. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The time granularity of the queried data. Unit: seconds. Valid values:
        # - 300
        # - 3600
        # - 86400
        # 
        # If this parameter is left empty or set to an unsupported value, the default value 3600 is used.
        self.interval = interval
        self.owner_id = owner_id
        # The live center to query. You can specify multiple regions. Separate multiple regions with commas (,). Valid values:
        # - cn-beijing: Beijing
        # - cn-shanghai: Shanghai
        # - cn-shenzhen: Shenzhen
        # - cn-qingdao: Qingdao
        # - ap-southeast-1: Singapore
        # - eu-central-1: Germany
        # - ap-northeast-1: Tokyo
        # - ap-southeast-5: Jakarta
        # 
        # If this parameter is left empty, the aggregated data of all regions is returned by default.
        self.region = region
        # The region ID.
        self.region_id = region_id
        # The grouping key. If this parameter is left empty, user data is aggregated. Valid values:
        # - domain: domain name. If the SplitBy (grouping key) parameter is set to domain, the Domain response parameter takes effect.
        # - region: live center region. If the SplitBy (grouping key) parameter is set to region, the Region response parameter takes effect.
        # - stream: stream name. If the SplitBy (grouping key) parameter is set to stream, the stream response parameter takes effect.
        # 
        # > You can query data only when the parameter corresponding to the grouping key is not empty. Otherwise, an error is returned. For example, when DomainName is empty, you cannot specify domain as the grouping key.
        self.split_by = split_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. By default, data of the last seven days is returned.
        self.start_time = start_time
        # The stream name. Separate multiple stream names with commas (,). By default, the data of all stream names is aggregated.
        self.stream_name = stream_name

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

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.split_by is not None:
            result['SplitBy'] = self.split_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

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

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

