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
        # The main streaming domain to query.
        # 
        # *   You can query one or more domain names. If you specify multiple domain names, separate them with commas (,).
        # *   If you leave this parameter empty, the data of all domain names within your Alibaba Cloud account is returned.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The end time must be later than the start time. We recommend that you specify a time range that is less than or equal to 10 hours.
        self.end_time = end_time
        # The time granularity of the query. Unit: seconds. Valid values:
        # 
        # *   300
        # *   3600
        # *   86400
        # 
        # If you specify an invalid value or do not specify this parameter, the default value 3600 is used.
        self.interval = interval
        self.owner_id = owner_id
        # The ID of the region. Separate multiple region IDs with commas (,). Valid values:
        # 
        # *   cn-beijing: China (Beijing)
        # *   cn-shanghai: China (Shanghai)
        # *   cn-shenzhen: China (Shenzhen)
        # *   cn-qingdao: China (Qingdao)
        # *   ap-southeast-1: Singapore
        # *   eu-central-1: Germany (Frankfurt)
        # *   ap-northeast-1: Japan (Tokyo)
        # *   ap-southeast-5: Indonesia (Jakarta)
        # 
        # If you leave this parameter empty, data of all regions is aggregated and returned by default.
        self.region = region
        self.region_id = region_id
        # The key that is used to group data. If you leave this parameter empty, data is aggregated and returned. Valid values:
        # 
        # *   domain: The DomainName parameter in the response takes effect only if SplitBy is set to domain.
        # *   region: The Region parameter in the response takes effect only if SplitBy is set to region.
        # *   stream: The StreamName parameter in the response takes effect only if SplitBy is set to stream.
        # 
        # >  This parameter takes effect only if the parameter corresponding to the value of this parameter is not left empty. Otherwise, an error is returned. For example, you cannot set this parameter to domain if the DomainName parameter is left empty.
        self.split_by = split_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. By default, data in the last seven days is returned.
        self.start_time = start_time
        # The name of the stream. Separate multiple stream names with commas (,). By default, data of all streams is aggregated and returned.
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

