# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDomainRecordUsageDataRequest(DaraModel):
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
    ):
        # The main streaming domain to query.
        # 
        # *   You can query one or more domain names. If you specify multiple domain names, separate them with commas (,).
        # *   If you leave this parameter empty, the data of all domain names within your Alibaba Cloud account is returned.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC. Value requirements:
        # 
        # *   The end time is later than the start time.
        # *   The time range between the start time and end time is up to 31 days. If the time range is more than 31 days, the request fails and an error is reported.
        self.end_time = end_time
        # The time granularity of the query. Unit: seconds. Valid values:
        # 
        # *   60
        # *   300
        # *   3600
        # *   86400
        # 
        # > If you do not specify this parameter or specify an invalid value: The time granularity of the query for a time range that is less than or equal to 31 days is 300 seconds by default. The time granularity of the query for a time range that is more than 31 days is 86400 seconds by default.
        self.interval = interval
        self.owner_id = owner_id
        # The ID of the region. Valid values:
        # 
        # *   **cn-beijing**: China (Beijing)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **cn-qingdao**: China (Qingdao)
        # *   **ap-southeast-1**: Singapore
        # *   **eu-central-1**: Germany (Frankfurt)
        # *   **ap-northeast-1**: Japan (Tokyo)
        # *   **ap-southeast-5**: Indonesia (Jakarta)
        self.region = region
        self.region_id = region_id
        # The key that is used to group data. Valid values:
        # 
        # *   **domain**: groups results by domain name.
        # *   **record_fmt**: groups results by recording type.
        # 
        # >  You can select one option or both. If you want to select both options, separate them with a comma (,). The default value is `domain,record_fmt`. If you leave this parameter empty or set the value to `null`, this parameter is ignored.
        self.split_by = split_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # *   The minimum data granularity is 5 minutes.
        # *   If you do not specify this parameter, the data in the last 24 hours is returned.
        # 
        # > The earliest start time that you can specify is 90 days back from the current time, accurate to seconds.
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

