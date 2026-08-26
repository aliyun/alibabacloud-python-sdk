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
        # The streaming domain name to query.
        # 
        # - Supports single or batch domain queries. Separate multiple domain names with commas (,).
        # - If this parameter is left empty, the merged data of all live streaming domain names is returned by default.
        # - When you specify DomainName, make sure that the specified domain name is a live streaming domain name and that the caller has the required permissions on the domain name.
        self.domain_name = domain_name
        # The end time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format in UTC. Requirements:
        # 
        # - The end time must be later than the start time (StartTime).
        # - The maximum time span between the end time and the start time is 31 days. Requests that exceed 31 days fail and return an error.
        self.end_time = end_time
        # The time granularity of the queried data. Unit: seconds. Valid values:
        # 
        # - 60.
        # 
        # - 300.
        # 
        # - 3600.
        # 
        # - 86400.
        # 
        # >If this parameter is not specified or an unsupported value is specified, the default time granularity is 300 seconds for query spans within 31 days and 86400 seconds for query spans longer than 31 days.
        self.interval = interval
        self.owner_id = owner_id
        # The region. Valid values:
        # 
        # - **cn-beijing**: Beijing.
        # 
        # - **cn-shanghai**: Shanghai.
        # 
        # - **cn-shenzhen**: Shenzhen.
        # 
        # - **cn-qingdao**: Qingdao.
        # 
        # - **ap-southeast-1**: Singapore.
        # 
        # - **eu-central-1**: Germany.
        # 
        # - **ap-northeast-1**: Tokyo.
        # 
        # - **ap-southeast-5**: Jakarta.
        self.region = region
        # The region ID.
        self.region_id = region_id
        # The grouping key. Valid values:
        # 
        # - **domain**: groups query results by domain name.
        # - **record_fmt**: groups query results by recording type.
        # 
        # > You can specify one or more values. Separate multiple values with commas (,). Default value: `domain,record_fmt`. If this parameter is set to empty or `null`, the results are not grouped by the preceding keys.
        self.split_by = split_by
        # The start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format in UTC.
        # 
        # - The minimum data granularity is 5 minutes.
        # - If this parameter is not specified, data of the last 24 hours is returned by default.
        # 
        # >The start time can be set to a point in time within the last 90 days from the current time, accurate to the second.
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

