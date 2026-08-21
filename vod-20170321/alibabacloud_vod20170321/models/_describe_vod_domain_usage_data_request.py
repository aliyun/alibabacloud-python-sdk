# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodDomainUsageDataRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        domain_name: str = None,
        end_time: str = None,
        field: str = None,
        interval: str = None,
        owner_id: int = None,
        start_time: str = None,
        type: str = None,
    ):
        # The region code. Default value: CN (the Chinese mainland). Valid values:
        # - **CN**: the Chinese mainland.
        # - **OverSeas**: outside the Chinese mainland.
        self.area = area
        # The accelerated domain name. If this parameter is left empty, the merged data of all accelerated domain names is returned by default. Batch queries are supported. Separate multiple domain names with commas (,).
        self.domain_name = domain_name
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The data type. Valid values:
        # - **bps**: bandwidth.
        # - **traf**: traffic.
        # 
        # This parameter is required.
        self.field = field
        # Forces the retrieval of data at the specified time granularity, in seconds. Valid values: **300** (5 minutes), **3600** (1 hour), and **86400** (1 day).
        # - **Interval**=**300**: You can query data for up to the last half year. The maximum time span for a single query is 3 days.
        # - **Interval**=**3600** or **86400**: You can query data for up to the last year.
        # - If **Interval** is not specified: The maximum time span for a single query is 1 month. If the query time range is 1 to 3 days, data is returned at hourly granularity. If the query time range is 4 days or more, data is returned at daily granularity.
        self.interval = interval
        self.owner_id = owner_id
        # The beginning of the time range to query. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of usage data to retrieve. Valid values:
        # 
        #  - **static**: static content.
        # - **dynamic**: dynamic content.
        # - **all**: all content.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.field is not None:
            result['Field'] = self.field

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

