# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDomainTimeShiftDataRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        owner_id: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The streaming domain to query.
        # 
        # > 
        # > - When you specify DomainName, make sure that the specified domain is a live streaming domain and that the user calling this operation has permissions on the specified domain.
        # > - You can specify a single domain or multiple domains. Separate multiple domains with commas (,).
        # > - If this parameter is left empty, the merged data of all live streaming domains is returned by default.
        self.domain_name = domain_name
        # The end time. The end time must be later than the start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format in UTC.
        self.end_time = end_time
        # The time granularity of the queried data. Unit: seconds. Valid values:
        # 
        # - 300.
        # - 3600.
        # - 86400.
        # 
        # If you do not specify this parameter or specify an unsupported value, the default value 300 is used.
        self.interval = interval
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format in UTC.
        # 
        # > - The minimum data granularity is 5 minutes.
        # > - If you do not specify this parameter, data of the last 24 hours is returned by default.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

